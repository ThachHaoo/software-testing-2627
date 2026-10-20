#!/usr/bin/env python3
"""
Trích prompt log từ transcript Claude Code (.jsonl) sang Markdown theo format HW01.

Script KHÔNG dùng AI: chỉ đọc transcript và chép nguyên văn prompt + output.
Các cột cần đánh giá của sinh viên (Section, Mục đích, Xử lý) lấy từ file ghi chú
TOML do sinh viên tự viết; chỗ nào chưa có thì để `[...]`.

Cách dùng:
  python extract_prompt_log.py SESSION.jsonl [SESSION2.jsonl ...] \
      --notes HW02/appendix/prompt_log_notes.toml \
      --extra HW02/appendix/prompt_log_extra.toml \
      --since 2026-10-12 --title "Prompt Log – HW02" \
      --name "Lê Tấn Hiệp" --mssv 23120255 \
      -o HW02/appendix/A_prompt_log.md

  # Liệt kê lượt (không ghi file) để biết số #n trước khi viết ghi chú:
  python extract_prompt_log.py SESSION.jsonl --list

Transcript của Claude Code nằm ở:
  Windows : %USERPROFILE%\\.claude\\projects\\<thư-mục-dự-án>\\<session-id>.jsonl
  macOS/Linux: ~/.claude/projects/<thư-mục-dự-án>/<session-id>.jsonl

File ghi chú (TOML, Python 3.11+ đọc được không cần cài thêm):
  [1]
  section  = "Toàn bài"
  muc_dich = "Đưa context bài tập cho AI"
  xu_ly    = "Đọc và gửi tiếp đề bài"
  ai_output_file = "appendix/ai-outputs/xxx.md"   # tuỳ chọn
  dinh_kem = "file đề bài"                         # tuỳ chọn, ghi đè tên file tự nhận

File lượt ngoài Claude Code (Gemini, ChatGPT…), cùng được đánh số theo thời gian:
  [[entry]]
  time   = "2026-10-20T09:15"        # giờ địa phương
  tool   = "Gemini Flash"
  prompt = '''...'''
  output = '''...'''
"""
import argparse
import glob
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None

LOCAL_TZ = dt.timezone(dt.timedelta(hours=7))  # Asia/Saigon

MODEL_RE = re.compile(r"claude-(opus|sonnet|haiku|fable|mythos)-(\d+)(?:-(\d{1,2}))?(?!\d)")

SYS_BLOCK = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
ATTACH_RE = re.compile(r"\[Attachment from earlier in this conversation: file [0-9a-f-]+(?: \((?P<name>[^)]+)\))?[^\]]*\]")
UPLOAD_RE = re.compile(r'@"[^"]*?/(?:[0-9a-f]{8}-)?(?P<name>[^/"]+)"')
SKIP_PREFIXES = (
    "Base directory for this skill",                     # nội dung skill được nạp
    "The files from earlier in this conversation",       # thông báo hệ thống giao file
    "Caveat: The messages below were generated",
    "<command-name>", "<local-command-stdout>",          # lệnh cục bộ (/add-dir, /compact…): không gửi cho AI
    "This session is being continued from a previous conversation",  # tóm tắt do hệ thống nén ngữ cảnh tạo
)
NO_MODEL = "Claude (không rõ model)"
# skill/slash command gửi cho AI: <command-message>x</command-message><command-name>/x</command-name><command-args>y</command-args>
CMD_RE = re.compile(r"<command-message>.*?</command-message>\s*<command-name>(?P<name>[^<]*)</command-name>"
                    r"\s*(?:<command-args>(?P<args>.*?)</command-args>)?", re.S)
PASTE_TAG = re.compile(r"</?pasted_content\b[^>]*>")
# lệnh dựng sẵn của Claude Code chạy cục bộ, không phải prompt gửi cho AI (dạng <command-message> cũng có)
LOCAL_CMD = re.compile(r"^/(compact|clear|add-dir|model|config|cost|help|status|memory|resume|exit|login|logout|context|skills|fast)\b")


def model_label(model_id: str) -> str:
    """claude-opus-5-5 -> Claude Opus 5.5; claude-sonnet-4-6 -> Claude Sonnet 4.6."""
    m = MODEL_RE.search(model_id or "")
    if not m:
        return model_id or "Claude"
    ver = m.group(2) + (f".{m.group(3)}" if m.group(3) else "")
    return f"Claude {m.group(1).capitalize()} {ver}"


def parse_ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(LOCAL_TZ)


def text_of(content):
    """Trả về (text, has_tool_result) từ content của message user."""
    if isinstance(content, str):
        return content, False
    parts, tool = [], False
    for b in content:
        if b.get("type") == "text":
            parts.append(b.get("text", ""))
        elif b.get("type") == "tool_result":
            tool = True
    return "\n".join(parts), tool


def clean_prompt(raw: str):
    """Bỏ khối hệ thống; tách tên file đính kèm; slash command → "/x y"; bỏ thẻ pasted_content, giữ nội dung."""
    attachments = [m.group("name") for m in ATTACH_RE.finditer(raw) if m.group("name")]
    attachments += [m.group("name") for m in UPLOAD_RE.finditer(raw)]
    txt = SYS_BLOCK.sub("", raw)
    txt = ATTACH_RE.sub("", txt)
    txt = UPLOAD_RE.sub("", txt)
    txt = CMD_RE.sub(lambda m: " ".join(x for x in (m.group("name").strip(), (m.group("args") or "").strip()) if x), txt)
    txt = PASTE_TAG.sub("", txt)
    return txt.strip(), attachments


def load_session(path: Path):
    """Gom transcript thành danh sách lượt {time, tool, prompt, attachments, output, files}."""
    turns, cur, pending_attach = [], None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("isSidechain"):  # bỏ hội thoại của subagent
            continue
        t = d.get("type")
        if t == "user":
            raw, is_tool = text_of(d["message"].get("content", ""))
            if is_tool and not raw.strip():
                continue
            if d.get("isMeta") or raw.lstrip().startswith(SKIP_PREFIXES):
                continue
            prompt, att = clean_prompt(raw)
            if LOCAL_CMD.match(prompt):
                continue
            if not prompt:  # tin nhắn chỉ để giao file: giữ tên file cho lượt kế tiếp
                pending_attach += att
                continue
            cur = {"time": parse_ts(d["timestamp"]), "tool": NO_MODEL, "models": [], "prompt": prompt,
                   "attachments": pending_attach + att, "output": [], "files": []}
            pending_attach = []
            turns.append(cur)
        elif t == "assistant" and cur is not None:
            msg = d.get("message", {})
            label = model_label(msg.get("model", ""))
            if msg.get("model") and not msg["model"].startswith("<") and label not in cur["models"]:
                cur["models"].append(label)
            cur["tool"] = " + ".join(cur["models"]) or NO_MODEL
            for b in msg.get("content", []):
                if b.get("type") == "text" and b.get("text", "").strip():
                    cur["output"].append(b["text"].strip())
                elif b.get("type") == "tool_use":
                    inp = b.get("input", {})
                    if b.get("name") in ("Write",) and inp.get("file_path"):
                        cur["files"].append(inp["file_path"])
                    if b.get("name") == "SendUserMessage" and inp.get("message"):
                        cur["output"].append(inp["message"].strip())
                    if b.get("name") == "SendUserFile":
                        cur["files"] += inp.get("files", [])
    return turns


def load_toml(path):
    if not path:
        return {}
    if tomllib is None:
        sys.exit("Cần Python 3.11+ để đọc file .toml")
    p = Path(path)
    return tomllib.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def fence(body: str) -> str:
    longest = max((len(m) for m in re.findall(r"`{3,}", body)), default=2)
    f = "`" * max(3, longest + 1)
    return f"{f}\n{body}\n{f}"


def render(turns, notes, args):
    tools = sorted({m for t in turns for m in t["tool"].split(" + ")})
    out = [f"# {args.title}",
           f"**Họ tên:** {args.name} | **MSSV:** {args.mssv} | **Công cụ AI:** {', '.join(tools)}",
           "",
           "> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script "
           "`tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.",
           "", "---", ""]
    for i, t in enumerate(turns, 1):
        n = notes.get(str(i), {})
        out.append(f"## #{i} | {t['time']:%H:%M %d/%m/%Y} | {t['tool']} | {n.get('section', '[...]')}")
        out.append(f"**Mục đích:** {n.get('muc_dich', '[...]')}")
        out += ["", "**Prompt:**", fence(t["prompt"])]
        if n.get("dinh_kem"):
            out.append(f"*Đính kèm:* {n['dinh_kem']}")
        elif t["attachments"]:
            out.append("*Đính kèm:* " + ", ".join(f"`{a}`" for a in dict.fromkeys(t["attachments"])))
        out += ["", "**Output:**"]
        if n.get("ai_output_file"):
            out.append(f"File do AI tạo, lưu nguyên bản tại `{n['ai_output_file']}`.")
        out.append(fence("\n\n".join(t["output"]) or "(không có output dạng văn bản)"))
        if t["files"]:
            out.append("*File AI ghi/gửi trong lượt này:* " + ", ".join(f"`{Path(f).name}`" for f in dict.fromkeys(t["files"])))
        out += ["", f"**Xử lý:** {n.get('xu_ly', '[...]')}", "", "---", ""]
    by_tool = {}
    for i, t in enumerate(turns, 1):
        for m in t["tool"].split(" + "):
            by_tool.setdefault(m, []).append(i)
    parts = [f"{k} {len(v)} lượt (#{', #'.join(map(str, v))})" for k, v in by_tool.items()]
    mixed = sum(1 for t in turns if " + " in t["tool"])
    note = f" {mixed} lượt có output từ hơn một model nên được đếm ở cả hai." if mixed else ""
    out.append(f"**Tổng:** {len(turns)} lượt; " + "; ".join(parts) + "." + note)
    return "\n".join(out) + "\n"


def main():
    for s in (sys.stdout, sys.stderr):  # Windows console không mặc định UTF-8
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser()
    ap.add_argument("sessions", nargs="+", help="file .jsonl hoặc mẫu glob, vd ...\\*.jsonl")
    ap.add_argument("--notes")
    ap.add_argument("--extra")
    ap.add_argument("--since", help="YYYY-MM-DD, bỏ các lượt trước ngày này")
    ap.add_argument("--until", help="YYYY-MM-DD, bỏ các lượt sau ngày này")
    ap.add_argument("--title", default="Prompt Log")
    ap.add_argument("--name", default="Lê Tấn Hiệp")
    ap.add_argument("--mssv", default="23120255")
    ap.add_argument("--list", action="store_true", help="chỉ liệt kê lượt")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    paths = sorted({Path(f) for pat in args.sessions for f in (glob.glob(pat) or [pat])})
    turns = [t for s in paths for t in load_session(s)]
    for e in load_toml(args.extra).get("entry", []):
        turns.append({"time": dt.datetime.fromisoformat(e["time"]).replace(tzinfo=LOCAL_TZ),
                      "tool": e["tool"], "prompt": e["prompt"].strip(), "attachments": e.get("attachments", []),
                      "output": [e["output"].strip()], "files": []})
    for t in turns:
        t["tool"] = t.get("tool") or NO_MODEL
    # phiên tiếp nối (resume/fork) chép lại lịch sử phiên cũ → bỏ lượt trùng giờ + prompt, giữ bản có nhiều output hơn
    uniq = {}
    for t in turns:
        k = (t["time"], t["prompt"])
        if k not in uniq or len("".join(t["output"])) > len("".join(uniq[k]["output"])):
            uniq[k] = t
    turns = list(uniq.values())
    turns.sort(key=lambda t: t["time"])
    if args.since:
        turns = [t for t in turns if t["time"].date() >= dt.date.fromisoformat(args.since)]
    if args.until:
        turns = [t for t in turns if t["time"].date() <= dt.date.fromisoformat(args.until)]

    if args.list:
        for i, t in enumerate(turns, 1):
            first = t["prompt"].splitlines()[0][:90]
            print(f"#{i:<3} {t['time']:%H:%M %d/%m/%Y}  {t['tool']:<16} {first}")
        return

    md = render(turns, {str(k): v for k, v in load_toml(args.notes).items() if k != "entry"}, args)
    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"Đã ghi {len(turns)} lượt vào {args.out}")
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
