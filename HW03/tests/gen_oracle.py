"""Sinh oracle.ts từ oracle.src.json + Expected trong ../checklist/checklist.json.

    python HW03/tests/gen_oracle.py

h = sha1(expected)[0:8]. Chạy lại SAU KHI đã sửa oracle.src.json cho Expected mới; không chạy chỉ để làm hết lỗi "oracle cũ".
"""
import hashlib, json
from pathlib import Path

here = Path(__file__).resolve().parent
src = json.loads((here / "oracle.src.json").read_text(encoding="utf-8"))
items = {i["id"]: i for i in json.loads((here.parent / "checklist" / "checklist.json").read_text(encoding="utf-8"))["items"]}
lines = [
    "// SINH TỰ ĐỘNG bằng gen_oracle.py từ oracle.src.json — không sửa tay.",
    "// h = sha1(expected)[0:8] của item trong checklist.json lúc sinh.",
    "export type Oracle = { h: string; mixed?: string; only?: string[]; why?: string; [k: string]: any };",
    "export const ORACLE: Record<string, Oracle> = {",
]
for k, v in src.items():
    if k.startswith("_"):
        continue
    if k not in items:
        raise SystemExit(f"{k} không có trong checklist.json")
    h = hashlib.sha1(items[k]["expected"].encode("utf-8")).hexdigest()[:8]
    lines.append(f"  {json.dumps(k)}: {json.dumps({'h': h, **v}, ensure_ascii=False)},")
lines.append("};")
(here / "oracle.ts").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"oracle.ts: {len(lines) - 5} item")
