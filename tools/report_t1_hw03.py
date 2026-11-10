"""Điền bảng T1/T3 của HW03 vào report từ checklist.json (không viết lời phân tích).

    python tools/report_t1_hw03.py [--print]

Ghi đè nội dung giữa <!-- REPORT:T1:<khối>:START --> … END --> trong HW03/23120255_HW03_Report.md.
Khối: checklist_table (3.3), execution + checklist_summary (3.5), failed_items (3.6), cross_platform (4.1), overlay (4.3).
Marker chưa có → báo, không tự chèn.
"""
import argparse, datetime as dt, json, re, sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1] / "HW03"
VALS = ["Passed", "Failed", "N/A", "Blocked"]
DIRS = {"P1": "P1_chrome", "P2": "P2_firefox", "P3": "P3_android"}
SCREENS = [("M1", "Đăng nhập"), ("M2", "Quên mật khẩu (B1, B2)"), ("M3", "Hồ sơ"), ("M4", "Lịch sử đơn"), ("M5", "Navbar khi đã đăng nhập")]
M5_REF = {"P1": "P1_M4_1", "P2": "P2_M4_1", "P3": "P3_M3_1"}   # R-M5: dùng lại ảnh có navbar đã đăng nhập


def res(it, P):
    return "N/A" if P not in it.get("nen_tang", []) else it.get("ket_qua", {}).get(P, "")


def cell(s, n=110):
    s = str(s).replace("|", "/").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def summary(doc):
    items, plats = doc["items"], list(doc["meta"]["platforms"])
    c = {P: Counter(res(i, P) for i in items) for P in plats}
    src = {P: Counter(i.get("nguon_kq", {}).get(P) for i in items if P in i.get("nen_tang", [])) for P in plats}
    out = ["| Chỉ số | " + " | ".join(f"{P} – {doc['meta']['platforms'][P]}" for P in plats) + " |", "|---|" + "---|" * len(plats)]
    out.append("| Item thiết kế | " + " | ".join(str(len(items)) for _ in plats) + " |")
    out.append("| Đã chạy (trừ N/A) | " + " | ".join(str(len(items) - c[P]["N/A"]) for P in plats) + " |")
    for v in VALS:
        out.append(f"| {v} | " + " | ".join(str(c[P][v]) for P in plats) + " |")
    out.append("| Tỉ lệ Passed / đã chạy | " + " | ".join(f"{100 * c[P]['Passed'] / max(1, len(items) - c[P]['N/A']):.1f}%".replace(".", ",") for P in plats) + " |")
    out.append("| Kết quả từ lượt tay / lượt auto | " + " | ".join(f"{src[P]['tay']} / {src[P]['auto']}" for P in plats) + " |")
    out += ["", "| IA | Số item | " + " | ".join(f"Failed {P}" for P in plats) + " |", "|---|---|" + "---|" * len(plats)]
    for ia in sorted({i["ia"] for i in items}):
        its = [i for i in items if i["ia"] == ia]
        out.append(f"| {ia} | {len(its)} | " + " | ".join(str(sum(res(i, P) == "Failed" for i in its)) for P in plats) + " |")
    runs = sorted({Path(r).name for i in items for r in i.get("run", {}).values() if r})
    out += ["", "Lượt gộp: " + ", ".join(f"`runs/{r}`" for r in runs) + ". Verdict: lượt tay trên trình duyệt thật; item không có trong lượt tay lấy lượt auto (V1, Q1). Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"


def cross(doc):
    items, plats = doc["items"], list(doc["meta"]["platforms"])
    out = ["**Item có kết quả khác nhau giữa các nền tảng**", "", "| Item | Mục kiểm tra | " + " | ".join(plats) + " | Ghi chú (notes theo nền tảng) |", "|---|---|" + "---|" * len(plats) + "---|"]
    for i in items:
        r = [res(i, P) for P in plats]
        if len({x for x in r if x != "N/A"}) > 1:   # khác nhau thật (bỏ N/A theo thiết kế)
            notes = "; ".join(f"{P}{' (auto)' if i.get('nguon_kq', {}).get(P) == 'auto' else ''}: {cell(re.sub(r'^\[auto – [^\]]*\] (Lỗi: Error: )?', '', i.get('notes_nt', {}).get(P, '')), 90)}"
                              for P in plats if res(i, P) not in ("Passed", "N/A"))
            out.append(f"| {i['id']} | {cell(i['muc_kiem_tra'], 60)} | " + " | ".join(r) + f" | {notes} |")
    out += ["", "**Lệch lượt auto ↔ lượt tay (cùng item, cùng nền tảng) – lấy lượt tay (V1)**", "", "| Item | Nền tảng | Auto | Tay | Nguyên nhân lệch |", "|---|---|---|---|---|"]
    for i in items:
        for P in plats:
            l = i.get("lech_auto_tay", {}).get(P)
            if l:
                out.append(f"| {i['id']} | {P} | {i['auto_status'][P]} | {i['ket_qua'][P]} | {cell(l.split(': ', 1)[-1], 160)} |")
    return "\n".join(out) + "\n"


def overview(plats):
    out = ["| Màn | " + " | ".join(plats) + " |", "|---|" + "---|" * len(plats)]
    ev = ROOT / "checklist" / "evidence"
    for code, name in SCREENS:
        row = []
        for P in plats:
            if code == "M5":
                f = ev / DIRS[P] / f"{M5_REF[P]}.png"
                row.append(f"dùng lại `{M5_REF[P]}`" + ("" if f.exists() else " (chưa có)"))
            else:
                fs = sorted(x.stem for x in (ev / DIRS[P]).glob(f"{P}_{code}_*.png"))
                row.append(", ".join(f"`{x}`" for x in fs) or "**chưa có**")
        out.append(f"| {code} – {name} | " + " | ".join(row) + " |")
    return out


NGUON = {"AI": "AI", "Both": "AI + SV sửa", "SV": "SV"}


def table(doc):
    plats = list(doc["meta"]["platforms"])
    out = ["| ID | IA | Màn hình | Item | Căn cứ | Loại nguồn | Nguồn | Ưu tiên | " + " | ".join(plats) + " | Ghi chú |",
           "|---|---|---|---|---|---|---|---|" + "---|" * len(plats) + "---|"]
    for i in doc["items"]:
        r = [res(i, P) for P in plats]
        note = []
        g = i.get("gia_dinh")
        if g:
            note.append("giả định " + (", ".join(g) if isinstance(g, list) else str(g)))
        if i.get("na"):
            note.append("N/A: " + cell(i["na"], 50))
        if "Failed" in r:
            note.append("xem 3.6")
        elif "Blocked" in r:
            note.append("Blocked – notes ở Excel")
        out.append(f"| {i['id']} | {i['ia']} | {cell(i['man_hinh'], 40)} | {cell(i['muc_kiem_tra'], 80)} | {cell(i.get('can_cu', ''), 60)} | "
                   f"{i.get('loai_nguon', '')} | {NGUON.get(i['nguon'], i['nguon'])} | {i.get('uu_tien', '')} | " + " | ".join(r) + f" | {'; '.join(note)} |")
    n = Counter(NGUON.get(i["nguon"], i["nguon"]) for i in doc["items"])
    lo = Counter(i.get("loai_nguon") for i in doc["items"])
    ia = Counter(i["ia"] for i in doc["items"])
    out += ["", f"{len(doc['items'])} item · IA: " + ", ".join(f"{k} {v}" for k, v in sorted(ia.items())) + " · loại nguồn: " + ", ".join(f"{k} {v}" for k, v in lo.items())
            + " · nguồn: " + ", ".join(f"{k} {v}" for k, v in n.items()) + ". Expected đầy đủ, tiền điều kiện, notes: `checklist/checklist.md` và Excel sheet Checklist. Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"


def _hdr(md):
    h = {}
    for line in md.read_text(encoding="utf-8").splitlines()[:10]:
        m = re.match(r"- ([^:]+): ?(.*)", line)
        if m:
            h[m.group(1).strip()] = m.group(2).strip()
    return h


def execution(doc):
    plats = list(doc["meta"]["platforms"])
    runs = ROOT / "checklist" / "runs"
    rows = []
    for P in plats:
        files = sorted({Path(r).name for i in doc["items"] for r in [i.get("auto_run", {}).get(P, ""), i.get("run", {}).get(P, "")] if r})
        for f in files:
            if f.endswith(".json"):
                j = json.loads((runs / f).read_text(encoding="utf-8"))
                t = dt.datetime.fromisoformat(j["run_at"].replace("Z", "+00:00")) + dt.timedelta(hours=7)
                n = sum(1 for i in doc["items"] if i.get("nguon_kq", {}).get(P) == "auto")
                rows.append((t.strftime("%Y-%m-%d %H:%M"), P, "auto (Playwright)", f"`runs/{f}`", j.get("env", ""), t.strftime("%H:%M %d/%m/%Y"), str(n)))
            else:
                h = _hdr(runs / f.replace(".csv", ".md"))
                se = next((v for k, v in h.items() if k.startswith("Bắt đầu")), "")
                n = sum(1 for i in doc["items"] if i.get("nguon_kq", {}).get(P) == "tay")
                m = re.match(r"(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4})", se)
                key = f"{m.group(5)}-{m.group(4)}-{m.group(3)} {m.group(1)}:{m.group(2)}" if m else "9999"
                rs = h.get("Restart backend lúc")
                rows.append((key, P, "tay", f"`runs/{f.replace('.csv', '.md')}`", f"{h.get('Trình duyệt / phiên bản', '')} · {h.get('OS / thiết bị', '')}",
                             se + (f" (restart backend: {rs})" if rs else ""), str(n)))
    rows.sort()
    out = ["| # | Nền tảng | Lượt | File | Môi trường | Thời gian (lượt tay: nguyên văn file lượt; auto: run_at giờ VN) | Số item lấy kết quả từ lượt này |", "|---|---|---|---|---|---|---|"]
    for k, r in enumerate(rows, 1):
        out.append(f"| {k} | " + " | ".join(cell(x, 130) for x in r[1:]) + " |")
    out += ["", "Thứ tự: lượt auto P1 → P2 → P3 (lệnh `npm run p1|p2|p3` đã gồm restart backend), sau đó chạy tay P1 → P2 → P3 trên trình duyệt/thiết bị thật, restart backend trước mỗi lượt tay. "
            "Thời gian lượt tay chép nguyên văn file lượt (run_check R4: giờ P1 chưa khớp nhau). Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"


def _map_failed():
    dup, grp = {}, {}
    for line in (ROOT / "bugs" / "failed_list.md").read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 7 and re.fullmatch(r"(CL|SV)-\d+", c[1]):
            dup[c[1]] = c[6].replace("**", "")
    for line in (ROOT / "bugs" / "bug_groups.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (G-\d+) \| `(BUG-\d+)\.md` \| [^|]* \| ([^|]*) \|", line)
        if m:
            for iid in re.findall(r"(?:CL|SV)-\d+", m.group(3)):
                grp[iid] = f"{m.group(1)} → {m.group(2)}"
    return dup, grp


def failed(doc):
    plats = list(doc["meta"]["platforms"])
    dup, grp = _map_failed()
    out = ["| ID | Màn hình | Item | Failed trên | Notes (theo nền tảng) | Ảnh | Issue trùng / nhóm bug |", "|---|---|---|---|---|---|---|"]
    n = 0
    for i in doc["items"]:
        fp = [P for P in plats if res(i, P) == "Failed"]
        if not fp:
            continue
        n += 1
        notes = "<br>".join(f"{P}{' (auto)' if i.get('nguon_kq', {}).get(P) == 'auto' else ''}: "
                            + cell(re.sub(r"^\[auto – [^\]]*\] (Lỗi: Error: )?", "", i.get("notes_nt", {}).get(P, "")).replace("Lỗi: Error: ", ""), 140) for P in fp)
        ev = "<br>".join(f"`{Path(e).name}`" for P in fp for e in (i.get("evidence", {}).get(P) or [])[:2])
        link = grp.get(i["id"], "")
        d = dup.get(i["id"], "")
        if d and d != "MỚI":
            link = d + (f"; {link}" if link else "")
        if any(i.get("lap_bug", {}).get(P) is False for P in fp):
            link = (link + "; " if link else "") + "không lập bug (5/6a)"
        out.append(f"| {i['id']} | {cell(i['man_hinh'], 40)} | {cell(i['muc_kiem_tra'], 70)} | {', '.join(fp)} | {notes} | {ev} | {link} |")
    out += ["", f"{n} item Failed trên ít nhất 1 nền tảng. Notes chép từ lượt chạy (auto: số đo Playwright). Ảnh: `checklist/evidence/<Px>_*/` (lượt tay), `checklist/evidence/auto/` (lượt auto); bảng này hiện tối đa 2 ảnh/nền tảng. "
            "Đối chiếu trùng đầy đủ: `bugs/failed_list.md`, `bugs/dup_check.md`; nhóm bug: `bugs/bug_groups.md`. Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"


def overlay(doc):
    plats = list(doc["meta"]["platforms"])
    ev = ROOT / "checklist" / "evidence"
    out = ["| Nền tảng | Thư mục | Ảnh item (lượt tay) | Ảnh tổng quan màn |", "|---|---|---|---|"]
    for P in plats:
        fs = sorted(x.name for x in (ev / DIRS[P]).glob("*.png"))
        ov = [f for f in fs if re.match(rf"{P}_M\d", f)]
        out.append(f"| {P} – {doc['meta']['platforms'][P]} | `checklist/evidence/{DIRS[P]}/` | {len(fs) - len(ov)} | {len(ov)} |")
    out += ["", "**Ảnh tổng quan Task 3 (mỗi màn × nền tảng)**", ""] + overview(plats)
    out += ["", "Overlay (O2): `23120255 - Lê Tấn Hiệp - 23120255@student.hcmus.edu.vn`; P1/P2 bằng Sticky Notes trên ảnh chụp toàn màn hình (thấy tên trình duyệt + URL), P3 thêm chữ bằng trình sửa ảnh ngay sau khi chụp. "
            "Ảnh lượt auto (`evidence/auto/`, ảnh phần tử Playwright chụp) không có overlay, chỉ là bằng chứng phụ. Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"



def put(text, block, body):
    pat = re.compile(rf"(<!-- REPORT:T1:{block}:START -->\n)(?:.*?\n)?(<!-- REPORT:T1:{block}:END -->)", re.S)
    if not pat.search(text):
        return text, False
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text, count=1), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    doc = json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))
    blocks = {"checklist_table": table(doc), "execution": execution(doc), "checklist_summary": summary(doc),
              "failed_items": failed(doc), "cross_platform": cross(doc), "overlay": overlay(doc)}
    if a.print:
        for k, v in blocks.items():
            print(f"--- {k}\n{v}")
        return
    rp = ROOT / "23120255_HW03_Report.md"
    text = rp.read_text(encoding="utf-8")
    for k, v in blocks.items():
        text, ok = put(text, k, v)
        print(f"{k}: {'đã ghi' if ok else 'CHƯA CÓ MARKER'}")
    rp.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
