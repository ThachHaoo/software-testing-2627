"""Sinh khung bugs/BUG-58…85.md theo mẫu HW02 (`git show d0d0e05:HW02/bugs/BUG-22.md`) từ nhóm SV đã chốt
(`tools/bug_groups_hw03.py`), `checklist.json`, file lượt chạy và SRS. Chỉ chép dữ kiện; chữ SV để `<SV viết>`.

    python tools/bug_skeleton_hw03.py [--force]

Không ghi đè file đã có chữ SV: file bị bỏ qua nếu một trong các dòng mẫu `<SV viết>` / `🔒` đã bị thay
(kiểm theo mẫu cũ 5/6a: đủ 6 dòng 🔒; mẫu mới: đủ 8 chỗ `<SV viết>`). --force: ghi đè cả file có chữ SV (KHÔNG dùng).
Quyết định: PFX = b → tiền tố tiêu đề GitHub `[HW03-C2-<số BUG>]` (chỉ dùng trên GitHub); DUP = a (giữ mức trùng).
"""
import argparse, datetime as dt, json, re, subprocess, sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).parent))
from bug_groups_hw03 import ENV, FIRST_BUG, GROUPS  # noqa: E402
from failed_list_hw03 import DUP  # noqa: E402

ROOT = REPO / "HW03"
SUT_DIR = REPO.parent / "eshop-sut"
SUT_COMMIT = "de0f48f"
SV = "`<SV viết>`"
PLACE_NEW = 8   # Tiêu đề, Severity, Priority, Tiền điều kiện, Các bước, Actual, Nhận định (+ dòng chú thích Expected)


def srs_lines():
    txt = subprocess.run(["git", "-C", str(SUT_DIR), "show", f"{SUT_COMMIT}:README.md"], capture_output=True, check=True).stdout.decode("utf-8")
    return txt.splitlines()


def refs(can_cu):
    """'FR-03.6 (README.md:58, 34); FR-10 (README.md:160–161)' → [('FR-03.6', [58, 34]), ('FR-10', [160, 161])]"""
    out = []
    for code, inside in re.findall(r"([A-Z]+-\d+(?:\.\d+)?)\s*\(README\.md:([^)]*)\)", can_cu):
        ns = []
        for part in inside.split(","):
            part = part.strip()
            m = re.match(r"(\d+)\s*[–-]\s*(\d+)$", part)
            ns += list(range(int(m.group(1)), int(m.group(2)) + 1)) if m else [int(part)]
        out.append((code, ns))
    return out


def run_time(P, run_path):
    f = ROOT / "checklist" / "runs" / Path(run_path).name
    if f.suffix == ".json":
        j = json.loads(f.read_text(encoding="utf-8"))
        t = dt.datetime.fromisoformat(j["run_at"].replace("Z", "+00:00")) + dt.timedelta(hours=7)
        return f"`runs/{f.name}`, {t:%H:%M %d/%m/%Y}"
    md = f.with_suffix(".md")
    for line in md.read_text(encoding="utf-8").splitlines()[:10]:
        if line.startswith("- Bắt đầu"):
            return f"`runs/{md.name}`, {line.split(':', 1)[1].strip()}"
    return f"`runs/{md.name}`"


def spec_line(iid, lines):
    for k, l in enumerate(lines, 1):
        if l.startswith(f"test('{iid} "):
            return f"`HW03/tests/C2.spec.ts:{k}`"
    return None


def has_sv_text(p):
    s = p.read_text(encoding="utf-8")
    if "🔒" in s or "Nhóm dữ kiện:** G-" in s.split("\n## ")[0]:
        return s.count("🔒") < 6        # mẫu cũ 5/6a
    return s.count("<SV viết>") < PLACE_NEW


def build(bug, g, fact, its, items, srs, spec):
    plats = ["P1", "P2", "P3"]

    def failed(it):
        return [P for P in plats if it.get("ket_qua", {}).get(P) == "Failed" and it.get("lap_bug", {}).get(P) is not False]
    num = bug.split("-")[1]
    fp = sorted({P for x in its for P in failed(items[x])})
    L = [f"# {bug}", "", f"- **ID:** {bug}", f"- **Tiêu đề:** {SV}", f"- **Severity:** {SV}", f"- **Priority:** {SV}",
         f"- Tiền tố GitHub: [HW03-C2-{num}]", "", "## Môi trường", "",
         f"- SUT: `ttbhanh/eshop-sut` @ `85af3ba` (chạy từ fork `tkob-team/eshop-sut` @ `{SUT_COMMIT}` = 85af3ba + .gitignore, không đổi mã)",
         "- Máy: Windows 11 Home (Asus Vivobook X1505VA), backend `node server.js` :3000 (CSDL seed lại mỗi lần khởi động), web http://localhost:5173 (frontend-web)"]
    for P in fp:
        for x in its:
            it = items[x]
            if P in failed(it):
                L.append(f"- {ENV[(P, it.get('nguon_kq', {}).get(P))]} · {x}: lượt {run_time(P, it.get('run', {}).get(P, ''))}")
    L += ["- Màn hình: " + "; ".join(f"{x} – {items[x]['man_hinh']}" for x in its),
          "- Chi tiết: `HW03/env/environment.md`, thứ tự lượt chạy ở report §3.5", "", "## Tiền điều kiện", "", SV, "", "## Các bước tái hiện", "", SV, "",
          "## Expected (trích căn cứ)", ""]
    for x in its:
        it = items[x]
        L.append(f"- {x} – căn cứ: {it.get('can_cu', '')}")
        for code, ns in refs(it.get("can_cu", "")):
            for n in ns:
                L.append(f"  - {code}, README.md:{n} (AI chép nguyên văn): {srs[n - 1].strip().removeprefix("- ")}")
        for gd in ([it["gia_dinh"]] if isinstance(it.get("gia_dinh"), str) else it.get("gia_dinh") or []):
            L.append(f"  - Giả định trong checklist (AI chép nguyên văn): {gd}")
    L += ["- Expected của bug: " + SV, "", "## Actual", "", SV, "", "## Bằng chứng", ""]
    for x in its:
        it = items[x]
        for P in failed(it):
            ev = it.get("evidence", {}).get(P) or []
            L.append(f"- {x} {P} ({it.get('nguon_kq', {}).get(P)}): " + (", ".join(f"`../checklist/{e}`" for e in ev) or "–"))
    L += ["", "## Item liên quan", ""]
    for x in its:
        it = items[x]
        d = DUP.get(x)
        rel = f" · {d[0].lower()} " + ", ".join(f"#{n}" for n in d[1]) + f" ({d[2]})" if d else ""
        L.append(f"- {x} – {it['muc_kiem_tra']} – Failed: {', '.join(failed(it))}{rel}")
    L += [f"- Nhóm dữ kiện: {g} trong `HW03/bugs/bug_groups.md` ({fact}); kiểm trùng: `HW03/bugs/dup_check.md`", "",
          "## Yêu cầu", "", "(AI điền từ `bug_groups.md`, SV duyệt)", ""]
    for x in its:
        it = items[x]
        L.append(f"- **{it.get('can_cu', '')}:** {it['muc_kiem_tra']} ({x})")
    L += ["", "## Ghi chú cô lập", "", "### Dữ kiện (AI chép)", ""]
    for x in its:
        it = items[x]
        for P in failed(it):
            note = re.sub(r"^\[auto – [^\]]*\] ", "", it.get("notes_nt", {}).get(P, "")).strip()
            L.append(f"- Actual nguyên văn {x} {P} ({it.get('nguon_kq', {}).get(P)}): `{note}`")
        L += [f"- Nguồn bước tái hiện {x}: tiền điều kiện (checklist): {it.get('tien_dieu_kien') or '–'} · cách kiểm: {it.get('che_do_ghi_chu') or it.get('che_do', '–')}"
              f" · test tự động: {spec_line(x, spec) or '– (chạy tay, xem `HW03/checklist/RUN.md`)'}"]
    L += ["", "### Nhận định", "", SV, "", "## Link GitHub Issue", "", "`<sau khi tạo issue>`", "", "---", "",
          "Mô tả bug do SV viết (AI-01 §11); AI chỉ điền phần dữ kiện (Môi trường, căn cứ, Bằng chứng, Item liên quan, Yêu cầu, Dữ kiện).", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    items = {i["id"]: i for i in json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))["items"]}
    srs = srs_lines()
    spec = (ROOT / "tests" / "C2.spec.ts").read_text(encoding="utf-8").splitlines()
    made, skipped = [], []
    for k, (g, fact, its) in enumerate(GROUPS):
        bug = f"BUG-{FIRST_BUG + k}"
        p = ROOT / "bugs" / f"{bug}.md"
        if p.exists() and has_sv_text(p) and not a.force:
            skipped.append(bug)
            continue
        p.write_text(build(bug, g, fact, its, items, srs, spec), encoding="utf-8")
        made.append(bug)
    print(f"sinh {len(made)} khung ({made[0] if made else '–'} … {made[-1] if made else '–'}); bỏ qua (có chữ SV): {skipped or 'không'}")


if __name__ == "__main__":
    main()
