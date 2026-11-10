#!/usr/bin/env python3
"""Gom item Failed MỚI thành nhóm dữ kiện G-xx → bug_groups.md, và (tuỳ chọn) khung BUG-<n>.md CHỈ chứa dữ kiện chép lại.

Usage: python bug_groups.py --config groups.json [--skeleton]   (hoặc run(cfg, skeleton) từ wrapper – ví dụ tools/bug_groups_hw03.py)

- groups do AI đề xuất theo dữ kiện quan sát giống nhau (cùng phần tử / cùng hành vi, khác màn/nền tảng); NGƯỜI DÙNG
  xác nhận/tách/gộp. Script dừng nếu nhóm không phủ đúng tập item MỚI (Failed, lap_bug ≠ false, dup ≠ TRÙNG) hoặc lặp item.
- Khung BUG: item, nền tảng, môi trường, nguồn bước (chép nguyên văn tien_dieu_kien / che_do_ghi_chu / dòng test – KHÔNG phải
  Steps), Expected chép, Actual chép notes, ảnh. Tiêu đề / Mô tả / Steps / Severity / Priority / Nhận định để trống cho người dùng.
  --skeleton không ghi đè khung đã có (người dùng có thể đã viết).

Config:
  checklist     đường dẫn checklist.json
  bugs_dir      thư mục ghi BUG-<n>.md
  groups_md     đường dẫn bug_groups.md
  dup           như failed_list.py
  groups        [["G-01", "dữ kiện chung", ["CL-10", "CL-12"]], ...]
  env           {"P1|tay": "Cốc Cốc 160 / Windows 11 – chạy tay", "P1|auto": "...", ...}
  sut           dòng mô tả SUT (repo @ commit, URL)
  first_bug     số BUG đầu tiên (nối tiếp bug cũ)
  spec_files    [["đường dẫn thật", "nhãn hiển thị"], ...]  – tìm dòng `test('<ID> ` để trỏ tới test tự động
  image_prefix  tiền tố đường dẫn ảnh từ bugs_dir (vd "../checklist/")
  owner         người viết bug (mặc định "SV")
  title, generator   tiêu đề bug_groups.md và tên script sinh
"""
import argparse, json, re, sys
from pathlib import Path


def strip(n):
    return re.sub(r"^\[auto – [^\]]*\] ", "", n or "")


def run(cfg, skeleton=False):
    doc = json.loads(Path(cfg["checklist"]).read_text(encoding="utf-8"))
    items = {i["id"]: i for i in doc["items"]}
    plats = list(doc["meta"]["platforms"])
    dup = {k: tuple(v) for k, v in cfg.get("dup", {}).items()}
    groups = [tuple(g) for g in cfg["groups"]]
    env = {tuple(k.split("|")): v for k, v in cfg["env"].items()}
    who = cfg.get("owner", "SV")
    img = cfg.get("image_prefix", "")
    specs = [(Path(p).read_text(encoding="utf-8").splitlines(), label) for p, label in cfg.get("spec_files", [])]

    def spec_line(iid):
        for lines, label in specs:
            for k, l in enumerate(lines, 1):
                if l.startswith(f"test('{iid} "):
                    return f"`{label}:{k}`"
        return None

    def failed(it):
        return [P for P in plats if it.get("ket_qua", {}).get(P) == "Failed" and it.get("lap_bug", {}).get(P) is not False]

    new = {iid for iid, it in items.items() if failed(it) and dup.get(iid, ("MỚI",))[0] != "TRÙNG"}
    grouped = [x for _, _, its in groups for x in its]
    dupl = {x for x in grouped if grouped.count(x) > 1}
    if set(grouped) != new or dupl:
        sys.exit(f"Nhóm chưa khớp danh sách MỚI: thiếu {sorted(new - set(grouped))}, thừa {sorted(set(grouped) - new)}, lặp {sorted(dupl)}")

    md = [cfg.get("title", f"# Nhóm dữ kiện bug (đề xuất, {who} xác nhận 🔒)"), "",
          f"Sinh bằng `{cfg.get('generator', 'bug_groups.py')}` từ `checklist.json` + `failed_list.md`. {len(new)} item Failed MỚI / trùng một phần → **{len(groups)} nhóm**. "
          "Gom theo dữ kiện quan sát giống nhau (cùng phần tử hoặc cùng hành vi, khác màn/nền tảng); AI không kết luận nguyên nhân. "
          f"{who} tách/gộp nhóm, rồi viết BUG từ khung tương ứng. Expected/Actual chép nguyên văn từ checklist (Actual = notes chạy tay hoặc số đo auto).", "",
          "| Nhóm | Khung | Dữ kiện chung | Item | Nền tảng Failed | Trùng / liên quan |", "|---|---|---|---|---|---|"]
    detail, made = [], []
    for k, (g, fact, its) in enumerate(groups):
        bug = f"BUG-{cfg['first_bug'] + k}"
        ps = sorted({P for x in its for P in failed(items[x])})
        rel = "; ".join(f"{x}: {dup[x][0].lower()} " + ", ".join(f"#{n}" for n in dup[x][1]) for x in its if x in dup)
        md.append(f"| {g} | `{bug}.md` | {fact} | {', '.join(its)} | {', '.join(ps)} | {rel or '–'} |")
        detail.append(f"## {g} → `{bug}.md` – {fact}\n")
        body = []
        for x in its:
            it = items[x]
            f = failed(it)
            detail.append(f"### {x} – {it['muc_kiem_tra']} ({it['man_hinh']})\n")
            detail.append(f"- Căn cứ: {it.get('can_cu', '')}")
            detail.append(f"- Expected (chép): {it['expected']}")
            for P in f:
                ev = ", ".join(f"`{e}`" for e in it.get("evidence", {}).get(P, [])) or "–"
                detail.append(f"- Actual {P} ({it.get('nguon_kq', {}).get(P)}): {strip(it['notes_nt'].get(P, ''))} · ảnh: {ev}")
            detail.append("")
            body += [f"### {x} – {it['muc_kiem_tra']}", "", f"- Màn hình: {it['man_hinh']}", f"- Căn cứ: {it.get('can_cu', '')}",
                     f"- Nền tảng Failed: {', '.join(f)}" + (f" · trùng một phần/liên quan: {', '.join('#' + str(n) for n in dup[x][1])} ({dup[x][2]})" if x in dup else ""),
                     "", "**Môi trường**", ""] + [f"- {env[(P, it.get('nguon_kq', {}).get(P))]}" for P in f] + [f"- SUT: {cfg['sut']}", "",
                     f"**Nguồn bước tái hiện (chép nguyên văn – {who} viết lại thành Steps)**", "",
                     f"- Tiền điều kiện (checklist): {it.get('tien_dieu_kien') or '–'}",
                     f"- Cách kiểm (checklist): {it.get('che_do_ghi_chu') or '–'}",
                     f"- Test tự động: {spec_line(x) or '– (item chạy tay, xem `checklist/RUN.md`)'}", "",
                     "**Expected (chép từ checklist)**", "", f"> {it['expected']}", "", "**Actual (chép notes / số đo)**", ""]
            for P in f:
                body.append(f"- {P} ({it.get('nguon_kq', {}).get(P)}): {strip(it['notes_nt'].get(P, ''))}")
            body += ["", "**Ảnh**", ""] + [f"- {P}: " + (", ".join(f"`{img}{e}`" for e in it.get("evidence", {}).get(P, [])) or "–") for P in f] + [""]
        if skeleton:
            p = Path(cfg["bugs_dir"]) / f"{bug}.md"
            if p.exists():
                print(f"giữ {p.name} (đã có)")
                continue
            head = [f"# {bug}", "", f"- **ID:** {bug}", f"- **Nhóm dữ kiện:** {g} ({', '.join(its)})",
                    f"- **Tiêu đề:** 🔒 {who} viết", f"- **Mô tả:** 🔒 {who} viết", f"- **Steps to reproduce:** 🔒 {who} viết (từ nguồn bước bên dưới)",
                    f"- **Severity:** 🔒 {who} chọn", f"- **Priority:** 🔒 {who} chọn", f"- **Nhận định:** 🔒 {who} viết", "- **GitHub Issue:** (sau khi tạo)", "",
                    "---", "", "## Dữ kiện (AI chép từ `checklist.json`, không sửa)", ""]
            p.write_text("\n".join(head + body), encoding="utf-8")
            made.append(p.name)
    Path(cfg["groups_md"]).write_text("\n".join(md + [""] + detail), encoding="utf-8")
    print(f"{len(new)} item MỚI → {len(groups)} nhóm; khung mới: {len(made)} ({made[0] if made else '–'} … {made[-1] if made else '–'})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--skeleton", action="store_true")
    a = ap.parse_args()
    run(json.loads(Path(a.config).read_text(encoding="utf-8")), a.skeleton)


if __name__ == "__main__":
    main()
