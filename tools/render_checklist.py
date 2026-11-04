"""Giữ tương thích: script đã chuyển sang skill gui-checklist-testing.

    python tools/render_checklist.py HW03/checklist/checklist.json -o HW03/checklist/checklist.md
"""
import runpy, sys
from pathlib import Path

sys.argv[0] = str(Path(__file__).resolve().parents[1] / ".claude/skills/gui-checklist-testing/scripts/render_checklist.py")
runpy.run_path(sys.argv[0], run_name="__main__")
