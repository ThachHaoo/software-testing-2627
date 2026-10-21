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
  # Kèm commit đầu tiên sau mỗi lượt, ghi ra file (-o) để gom khoá khoảng:
  python extract_prompt_log.py SESSION.jsonl --list --commits -o HW02/appendix/prompt_log_turns.txt

Transcript của Claude Code nằm ở:
  Windows : %USERPROFILE%\\.claude\\projects\\<thư-mục-dự-án>\\<session-id>.jsonl
  macOS/Linux: ~/.claude/projects/<thư-mục-dự-án>/<session-id>.jsonl

File ghi chú (TOML, Python 3.11+ đọc được không cần cài thêm). Khoá là giờ của lượt (in bởi --list;
lượt thứ k trong cùng phút thêm "#k"), hoặc số thứ tự [n] (cách cũ; khoá giờ được ưu tiên).
Đổi khoá số sang khoá giờ: thêm --migrate-notes.
  ["2026-10-12 21:20"]
  section  = "Toàn bài"
  muc_dich = "Đưa context bài tập cho AI"
  xu_ly    = "Đọc và gửi tiếp đề bài"
  ai_output_file = "appendix/ai-outputs/xxx.md"   # tuỳ chọn
  dinh_kem = "file đề bài"                         # tuỳ chọn, ghi đè tên file tự nhận
Khoá khoảng (hai đầu tính cả, theo phút) áp cho mọi lượt trong khoảng; khoá giờ/số ghi đè từng trường:
  ["2026-10-19 16:00 .. 2026-10-19 17:30"]
  section  = "A_FR01 bước 1"

File lượt ngoài Claude Code (Gemini, ChatGPT…), cùng được đánh số theo thời gian:
  [[entry]]
  time   = "2026-10-20T09:15"        # giờ địa phương
  tool   = "Gemini Flash"
  source = "Chép tay từ giao diện …"   # tuỳ chọn, hiện thành dòng "*Nguồn:*" dưới tiêu đề lượt
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


def time_keys(turns):
    """Khoá giờ cho ghi chú: "2026-10-19 16:10"; lượt thứ k trong cùng phút → "2026-10-19 16:10#k".
    Không đổi khi thêm/bớt lượt ở chỗ khác, khác với số thứ tự #n."""
    keys, seen = [], {}
    for t in turns:
        base = f"{t['time']:%Y-%m-%d %H:%M}"
        seen[base] = seen.get(base, 0) + 1
        keys.append(base if seen[base] == 1 else f"{base}#{seen[base]}")
    return keys


RANGE_SEP = ".."


def parse_ranges(notes):
    """Khoá khoảng "YYYY-MM-DD HH:MM .. YYYY-MM-DD HH:MM" → [(đầu, cuối, ghi chú)], hai đầu tính cả."""
    ranges = []
    for k, v in notes.items():
        if RANGE_SEP not in k:
            continue
        try:
            a, b = (dt.datetime.strptime(x.strip(), "%Y-%m-%d %H:%M") for x in k.split(RANGE_SEP))
        except ValueError:
            sys.exit(f'Khoá khoảng sai cú pháp: ["{k}"] — cần "YYYY-MM-DD HH:MM .. YYYY-MM-DD HH:MM"')
        if a > b:
            sys.exit(f'Khoá khoảng ngược: ["{k}"]')
        ranges.append((a, b, v))
    return ranges


def note_for(notes, keys, i, turns=None, ranges=()):
    """Ưu tiên khoá giờ, sau đó số thứ tự (1-based). Khoá khoảng cho giá trị mặc định từng trường;
    khoá giờ/số ghi đè từng trường. Nhiều khoảng chứa cùng lượt → khoảng hẹp nhất (bằng nhau: khoảng ghi trước)."""
    single = notes.get(keys[i - 1]) or notes.get(str(i), {})
    if not ranges:
        return single
    t = turns[i - 1]["time"].replace(tzinfo=None, second=0, microsecond=0)
    hits = [r for r in ranges if r[0] <= t <= r[1]]
    if not hits:
        return single
    return {**min(hits, key=lambda r: r[1] - r[0])[2], **single}


def warn_unmatched(notes, keys, turns, ranges):
    """In ra stderr mọi khoá ghi chú không khớp lượt nào (kể cả khoá gõ sai cú pháp)."""
    times = [t["time"].replace(tzinfo=None, second=0, microsecond=0) for t in turns]
    used_ranges = {id(r[2]) for r in ranges if any(r[0] <= x <= r[1] for x in times)}
    for k, v in notes.items():
        if RANGE_SEP in k:
            ok = id(v) in used_ranges
        else:
            ok = k in keys or (k.isdigit() and 1 <= int(k) <= len(turns))
        if not ok:
            print(f'Cảnh báo: khoá ghi chú ["{k}"] không khớp lượt nào', file=sys.stderr)


def commits_after(turns, repo="."):
    """Với mỗi lượt: commit đầu tiên có giờ commit sau giờ lượt → (hash ngắn, message) hoặc None."""
    import subprocess
    r = subprocess.run(["git", "-C", repo, "log", "--all", "--format=%h%x09%cI%x09%s"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(f"git log lỗi: {r.stderr.strip()}")
    cs = []
    for line in r.stdout.splitlines():
        h, ts, msg = line.split("\t", 2)
        cs.append((dt.datetime.fromisoformat(ts).astimezone(LOCAL_TZ), h, msg))
    cs.sort()
    out = []
    for t in turns:
        nxt = next((c for c in cs if c[0] > t["time"]), None)
        out.append((nxt[1], f"{nxt[0]:%H:%M %d/%m}", nxt[2]) if nxt else None)
    return out


def migrate_notes(path, turns):
    """Đổi tiêu đề bảng [n] trong file notes thành ["<khoá giờ>"]; giữ nguyên nội dung và chú thích."""
    keys = time_keys(turns)
    p = Path(path)
    txt = p.read_text(encoding="utf-8")

    def sub(m):
        n = int(m.group(1))
        if not 1 <= n <= len(keys):
            sys.exit(f"[{n}] vượt quá {len(keys)} lượt hiện có — không đổi file")
        return f'["{keys[n - 1]}"]'
    new, cnt = re.subn(r"(?m)^\[(\d+)\]\s*$", sub, txt)
    p.write_text(new, encoding="utf-8")
    print(f"Đổi {cnt} khoá số sang khoá giờ trong {path}")


def render(turns, notes, args):
    keys = time_keys(turns)
    ranges = parse_ranges(notes)
    warn_unmatched(notes, set(keys), turns, ranges)
    tools = sorted({m for t in turns for m in t["tool"].split(" + ")})
    out = [f"# {args.title}",
           f"**Họ tên:** {args.name} | **MSSV:** {args.mssv} | **Công cụ AI:** {', '.join(tools)}",
           "",
           "> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script "
           "`tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.",
           "", "---", ""]
    for i, t in enumerate(turns, 1):
        n = note_for(notes, keys, i, turns, ranges)
        out.append(f"## #{i} | {t['time']:%H:%M %d/%m/%Y} | {t['tool']} | {n.get('section', '[...]')}")
        if t.get("source"):
            out.append(f"*Nguồn:* {t['source']}")
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
    ap.add_argument("--list", action="store_true", help="chỉ liệt kê lượt (kèm khoá giờ dùng trong notes)")
    ap.add_argument("--commits", action="store_true", help="cùng --list: in kèm commit đầu tiên sau mỗi lượt")
    ap.add_argument("--migrate-notes",action="store_true", help="đổi khoá [n] trong --notes sang khoá giờ rồi thoát")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    paths = sorted({Path(f) for pat in args.sessions for f in (glob.glob(pat) or [pat])})
    turns = [t for s in paths for t in load_session(s)]
    for e in load_toml(args.extra).get("entry", []):
        turns.append({"time": dt.datetime.fromisoformat(e["time"]).replace(tzinfo=LOCAL_TZ),
                      "tool": e["tool"], "prompt": e["prompt"].strip(), "attachments": e.get("attachments", []),
                      "output": [e["output"].strip()], "files": [], "source": e.get("source", "")})
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

    if args.migrate_notes:
        if not args.notes:
            sys.exit("Cần --notes")
        migrate_notes(args.notes, turns)
        return

    if args.commits and not args.list:
        sys.exit("--commits chỉ dùng cùng --list")
    if args.list:
        cms = commits_after(turns) if args.commits else [None] * len(turns)
        lines = []
        for i, (t, k, c) in enumerate(zip(turns, time_keys(turns), cms), 1):
            first = t["prompt"].splitlines()[0][:80] if t["prompt"] else ""
            line = f'#{i:<3} ["{k}"]  {t["tool"]:<16} {first}'
            if args.commits:
                line += f"\n      → commit kế tiếp: {c[0]} ({c[1]}) {c[2]}" if c else "\n      → commit kế tiếp: (chưa có)"
            lines.append(line)
        txt = "\n".join(lines) + "\n"
        if args.out:
            hdr = ("# Danh sách lượt (sinh bởi tools/extract_prompt_log.py --list"
                   + (" --commits" if args.commits else "") + "). Dùng để gom khoá khoảng trong prompt_log_notes.toml.\n"
                   "# Commit kế tiếp = commit đầu tiên có giờ commit sau giờ lượt (git log --all).\n\n")
            Path(args.out).write_text(hdr + txt, encoding="utf-8")
            print(f"Đã ghi danh sách {len(turns)} lượt vào {args.out}")
        else:
            sys.stdout.write(txt)
        return

    md = render(turns, {str(k): v for k, v in load_toml(args.notes).items() if k != "entry"}, args)
    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"Đã ghi {len(turns)} lượt vào {args.out}")
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
