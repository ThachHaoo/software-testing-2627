#!/usr/bin/env python3
"""Gộp mọi lượt chạy (auto Playwright + chạy tay) của một checklist vào checklist.json theo quy tắc V1.

Usage: python merge_runs.py --config merge.json [--dry-run]
       (hoặc import và gọi run(cfg) từ wrapper của bài – ví dụ tools/merge_hw03.py)

Quy trình:
1. Lượt tay dạng bảng Markdown (`| ID | status | notes | ảnh |`, người chạy viết, KHÔNG sửa) → CSV cạnh nó
   (id,status,notes,evidence). Tên ảnh ánh xạ sang tên chuẩn `<Px>_<ID>_<k>.png` trong `evidence/<thư mục Px>/`;
   ảnh không còn → bỏ + cảnh báo. Lượt tay dạng .csv dùng nguyên.
2. merge_platform.py: lượt auto → auto_status/auto_notes/auto_evidence; lượt tay → ket_qua/notes_nt/evidence.
3. Item không có trong lượt tay → ket_qua = auto_status, notes "[auto – <env>] …", nguon_kq[Px] = "auto".
4. Có cả hai mà khác nhau → giữ lượt tay (V1), lech_auto_tay[Px] = "auto X ≠ tay Y → lấy tay (V1): <nguyên nhân>".
5. override (quyết định của người dùng, áp sau cùng nên chạy lại vẫn giữ): đổi ket_qua (vd lỗi harness → Blocked),
   nối câu vào notes (không sửa chữ người chạy), lap_bug=false (loại khỏi danh sách lập bug).

Config (JSON hoặc dict):
  checklist        đường dẫn checklist.json
  runs_dir         thư mục file lượt
  evidence_dir     thư mục evidence/ (chứa thư mục con từng nền tảng)
  platform_dirs    {"P1": "P1_chrome", ...}
  auto             {"P1": "P1_auto_….json", ...}            (tuỳ chọn)
  manual           {"P1": "P1_manual_….md" | "….csv", ...}   (tuỳ chọn; .md có thể bỏ đuôi)
  auto_env         {"P1": "Chrome 157 qua Playwright", ...}
  cause            {"CL-08|P2": "nguyên nhân lệch", ...}
  override         {"CL-30|P3": {"ket_qua": "Blocked", "them": "…", "lap_bug": false}, ...}
  id_prefixes      ["CL", "SV"]   (mặc định)
  evidence_prefix  tiền tố đường dẫn ảnh ghi vào json (mặc định "evidence")
"""
import argparse, csv, json, re, subprocess, sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

MERGE = Path(__file__).resolve().parent / "merge_platform.py"


def _key(k):
    return tuple(k.split("|")) if isinstance(k, str) else tuple(k)


def std_name(name, prefixes):
    pre = "|".join(prefixes)
    m = re.search(rf"(P\d)_((?:{pre})-?\d{{2}}|M\d)[-_](\d+)", name, re.I)
    if not m:
        return None
    iid = m[2].upper()
    if iid[:2] in prefixes and "-" not in iid:
        iid = iid[:2] + "-" + iid[2:]
    return f"{m[1].upper()}_{iid}_{int(m[3])}.png"


def to_csv(src, P, cfg):
    pre = "|".join(cfg.get("id_prefixes", ["CL", "SV"]))
    ev_dir = Path(cfg["evidence_dir"]) / cfg["platform_dirs"][P]
    ev_pre = cfg.get("evidence_prefix", "evidence")
    rows, warn = [], []
    for line in src.read_text(encoding="utf-8").splitlines():
        m = re.match(rf"^\|\s*((?:{pre})-\d{{2}})\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m[2].split("|")]
        status, notes, imgs = cells[0], " | ".join(cells[1:-1]), cells[-1]
        ev = []
        for x in re.split(r"[,;]\s*", imgs):
            if not x:
                continue
            n = std_name(x, cfg.get("id_prefixes", ["CL", "SV"]))
            if n and (ev_dir / n).exists():
                ev.append(f"{ev_pre}/{cfg['platform_dirs'][P]}/{n}")
            else:
                warn.append(f"{P} {m[1]}: ảnh '{x}' không có trong evidence/ – bỏ")
        rows.append({"id": m[1], "status": status, "notes": notes, "evidence": ";".join(ev)})
    out = src.with_suffix(".csv")
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, ["id", "status", "notes", "evidence"])
        w.writeheader()
        w.writerows(rows)
    return out, warn


def merge(json_path, run_file, P, dry):
    cmd = [sys.executable, str(MERGE), str(json_path), str(run_file), "--platform", P] + (["--dry-run"] if dry else [])
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr)
    for l in r.stdout.splitlines():
        if l.startswith("WARN"):
            print("  ", l)


def run(cfg, dry=False):
    jp, runs = Path(cfg["checklist"]), Path(cfg["runs_dir"])
    auto, manual = cfg.get("auto", {}), cfg.get("manual", {})
    for P in cfg["platform_dirs"]:
        if P in auto:
            merge(jp, runs / auto[P], P, dry)
        if P in manual:
            src = runs / manual[P]
            if src.suffix.lower() != ".csv":
                src = src if src.suffix.lower() == ".md" else src.with_name(src.name + ".md")
                src, warn = to_csv(src, P, cfg)
                for w in warn:
                    print("WARN ", w)
            merge(jp, src, P, dry)
    if dry:
        return
    cause = {_key(k): v for k, v in cfg.get("cause", {}).items()}
    override = {_key(k): v for k, v in cfg.get("override", {}).items()}
    env = cfg.get("auto_env", {})
    doc = json.loads(jp.read_text(encoding="utf-8"))
    filled, lech = 0, []
    for it in doc["items"]:
        for P in it.get("nen_tang", []):
            au, tay = it.get("auto_status", {}).get(P), it.get("ket_qua", {}).get(P)
            if tay and it.get("run", {}).get(P, "").endswith(".csv"):
                it.setdefault("nguon_kq", {})[P] = "tay"
                if au and au != tay:
                    c = cause.get((it["id"], P), "CHƯA RÕ – người chạy ghi nguyên nhân")
                    it.setdefault("lech_auto_tay", {})[P] = f"auto {au} ≠ tay {tay} → lấy tay (V1): {c}"
                    lech.append(f"{it['id']} {P}")
            elif au:
                it.setdefault("ket_qua", {})[P] = au
                it.setdefault("notes_nt", {})[P] = f"[auto – {env.get(P, 'Playwright')}] " + it.get("auto_notes", {}).get(P, "")
                it.setdefault("evidence", {})[P] = it.get("auto_evidence", {}).get(P, [])
                it.setdefault("run", {})[P] = it.get("auto_run", {}).get(P, "")
                it.setdefault("nguon_kq", {})[P] = "auto"
                filled += 1
    items = {i["id"]: i for i in doc["items"]}
    for (iid, P), o in override.items():
        it = items[iid]
        if "ket_qua" in o:
            it["ket_qua"][P] = o["ket_qua"]
        if o.get("them") and o["them"] not in it.get("notes_nt", {}).get(P, ""):
            old = it.setdefault("notes_nt", {}).get(P, "")
            it["notes_nt"][P] = (old + " · " if old else "") + "[" + o["them"] + "]"
        if "lap_bug" in o:
            it.setdefault("lap_bug", {})[P] = o["lap_bug"]
    jp.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    miss = [f"{i['id']} {P}" for i in doc["items"] for P in i.get("nen_tang", []) if not i.get("ket_qua", {}).get(P)]
    print(f"ket_qua từ auto: {filled} ô; lệch auto↔tay: {len(lech)} ({', '.join(lech)}); thiếu kết quả: {len(miss)} {miss}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    run(json.loads(Path(a.config).read_text(encoding="utf-8")), a.dry_run)


if __name__ == "__main__":
    main()
