#!/usr/bin/env python3
"""Hook Stop của Claude Code: sau mỗi lượt trả lời,
1) chép transcript của phiên vào <repo>/.transcripts/ (bản sao dự phòng, gitignore),
2) chạy tools/extract_prompt_log.py để cập nhật prompt log của bài đang làm (tools/hw.toml).

Không bao giờ chặn Claude: mọi lỗi chỉ ghi vào .transcripts/hook.log và thoát 0.
Transcript có thể ghi trễ so với lượt hiện tại; lượt cuối sẽ có ở lần chạy sau
hoặc khi chạy tay: python tools/hooks/on_stop.py --manual
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time
import tomllib
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])


MANUAL = "--manual" in sys.argv
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def log(msg):
    d = ROOT / ".transcripts"
    d.mkdir(exist_ok=True)
    with open(d / "hook.log", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    if MANUAL:
        print(msg)


def local_session_dirs():
    """Thư mục transcript Claude Code của repo này: ~/.claude/projects/<đường dẫn repo, ký tự lạ -> '-'>."""
    base = Path.home() / ".claude" / "projects"
    if not base.exists():
        return []
    key = re.sub(r"[^A-Za-z0-9]", "-", str(ROOT)).lower()
    return [d for d in base.iterdir() if d.is_dir() and (d.name.lower() == key or d.name.lower().endswith(ROOT.name.lower()))]


def main():
    cfg = tomllib.loads((ROOT / "tools" / "hw.toml").read_text(encoding="utf-8"))
    tdir = ROOT / cfg.get("transcripts", ".transcripts")
    tdir.mkdir(exist_ok=True)

    if MANUAL:
        # chạy tay: gom mọi transcript Claude Code của repo này
        for d in local_session_dirs():
            for src in d.glob("*.jsonl"):
                shutil.copy2(src, tdir / src.name)
                log(f"chép {src}")
    else:
        try:
            payload = json.load(sys.stdin)
        except Exception:
            payload = {}
        src = payload.get("transcript_path")
        if src and Path(src).exists():
            shutil.copy2(src, tdir / Path(src).name)

    sessions = sorted(str(p) for p in tdir.glob("*.jsonl"))
    if not sessions:
        log(f"chưa có transcript nào trong {tdir} (Claude Code chưa có lượt trả lời nào, hoặc chưa chép transcript của phiên claude.ai vào đây)")
        return
    cmd = [sys.executable, str(ROOT / "tools" / "extract_prompt_log.py"), *sessions,
           "--title", cfg.get("title", "Prompt Log"), "--name", cfg.get("name", ""), "--mssv", cfg.get("mssv", ""),
           "-o", str(ROOT / cfg["log"])]
    for key, flag in (("notes", "--notes"), ("extra", "--extra"), ("since", "--since"), ("until", "--until")):
        if cfg.get(key):
            val = str(ROOT / cfg[key]) if key in ("notes", "extra") else cfg[key]
            cmd += [flag, val]
    (ROOT / cfg["log"]).parent.mkdir(parents=True, exist_ok=True)
    # Windows: ép tiến trình con in UTF-8, nếu không stdout sẽ theo code page (cp1252/cp1258) và vỡ khi giải mã
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    out, err = (r.stdout or "").strip(), (r.stderr or "").strip()
    log(out + (f" | lỗi (mã {r.returncode}): {err}" if r.returncode else (f" | {err}" if err else "")))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # không chặn Claude
        log(f"lỗi: {e!r}")
    sys.exit(0)
