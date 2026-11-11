"""Sinh khung AI-02 (Audit), AI-03 (Disclosure) cho HW03 và khối Mandatory Disclosure (report §11). Không dùng AI.

    python tools/forms_hw03.py

- Artifact AI tạo: danh mục DƯỚI ĐÂY + git (commit tạo, commit sửa sau đó).
- Cột #n: các lượt trong `appendix/prompt_log_turns.txt` (sinh bằng extract_prompt_log.py --list --commits, cùng since/exclude với log)
  có giờ > commit liền trước (git log --all) và ≤ giờ commit tạo artifact = "dải lượt trước commit";
  rỗng (nhiều commit liền nhau trong một lượt) → lượt cuối có giờ ≤ commit.
- Verdict / Lý do / cam đoan / chữ ký / phần đánh giá: `<SV viết>` hoặc `[...]` — AI không điền.
- Số lượt theo model: dòng "**Tổng:**" của HW03/appendix/A_prompt_log.md lúc chạy (chạy lại sau lần trích cuối).
- Mẫu định dạng: HW02/ai-forms (không chép số liệu HW02). AI-05 không sinh ở đây.
"""
import datetime as dt, re, subprocess, sys
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO = Path(__file__).resolve().parents[1]
HW = REPO / "HW03"
SV = "`<SV viết>`"
TBD = "–"
HEAD = ["**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**",
        "**CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)**", "**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**", ""]
SIGN = ["## Chữ ký", "", "| Mục | Giá trị |", "|---|---|", "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |",
        "| Lớp / Khoá: | Software Testing - 23_3 |", "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |",
        "| Giảng viên: | Thầy Lâm Quang Vũ, Thầy Trần Duy Hoàng, Cô Trần Thị Bích Hạnh, Thầy Trương Phước Lộc, Thầy Hồ Tuấn Thanh |",
        "| Ngày: | [...] |", "| Chữ ký: | [...] |", ""]
REFS = ["## Tham khảo", "", "- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.",
        "- ISTQB Foundation Level Syllabus (latest version).", "- Hardman, P. (2025). A Post-AI Learning Taxonomy.",
        "- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.", ""]

# (mã, artifact, [đường dẫn trong repo], ghi chú output)
ART = [
    ("H1", "Harness HW03: `HW03/CLAUDE.md`, kế hoạch nộp `report_plan.md` (không nộp), khung report/README", ["HW03/CLAUDE.md", "HW03/report_plan.md"], "khung bài, quyết định, khai Audit"),
    ("T1", "Khảo sát control C2 (`c2_inventory.md`)", ["HW03/checklist/c2_inventory.md"], "inventory màn Đăng nhập, Quên MK, Hồ sơ, Lịch sử đơn, navbar"),
    ("T2", "Checklist nháp 3 nguồn – bản đóng băng v1 (bước 1)", ["HW03/appendix/ai-outputs/T1_checklist_ai_v1.json"], "65 item"),
    ("T3", "Khung trống `sv_items.md` + kiểm cấu trúc item SV (`sv_items_check.md`)", ["HW03/checklist/sv_items_check.md"], "khung trống; nội dung item SV do SV viết"),
    ("T4", "Câu trả lời \"vì sao AI bỏ sót\" (sau khi SV commit item)", ["HW03/checklist/ai_gap_answer.md"], "SV-01…SV-06"),
    ("T5", "Playwright C2 + oracle khoá sha1 + reporter + seed đơn", ["HW03/tests/C2.spec.ts", "HW03/tests/lib.ts", "HW03/tests/oracle.src.json", "HW03/tests/gen_oracle.py",
                                                                     "HW03/tests/reporter.ts", "HW03/tests/playwright.config.ts", "HW03/tests/global-setup.ts", "HW03/tests/seed_orders.py"], "59 item auto, 3 project P1/P2/P3"),
    ("T6", "`RUN.md` (phần chạy tay) + mẫu file lượt + `dom_probe.js`", ["HW03/checklist/RUN.md", "HW03/tests/gen_run.py", "HW03/checklist/dom_probe.js", "HW03/checklist/RUN_retake.md"], "15/15/13 item chạy tay"),
    ("T7", "Kiểm ảnh/kết quả chạy tay (`run_check.md`), nén + đổi tên ảnh", ["HW03/checklist/run_check.md", "tools/compress_hw03.py"], "R1–R12, L1–L8"),
    ("T8", "Gộp lượt auto + tay vào `checklist.json` (V1, override theo quyết định SV) + `checklist.md`", ["tools/merge_hw03.py"], "kết quả P1/P2/P3"),
    ("T9", "Excel 3 sheet", ["HW03/excel/23120255_HW03_Checklist.xlsx"], "Test Cases / Checklist / Test Summary Report"),
    ("T10", "Danh sách Failed + đối chiếu trùng issue theo tiêu đề (`failed_list.md`, `issues.json`, `issue_dup_FR02.md`)", ["HW03/bugs/failed_list.md", "HW03/bugs/issues.json", "HW03/checklist/issue_dup_FR02.md", "tools/failed_list_hw03.py"], "trùng 14 / một phần 4 / MỚI 28"),
    ("T11", "Nhóm dữ kiện bug + khung BUG-58…85 (chỉ dữ kiện)", ["HW03/bugs/bug_groups.md", "tools/bug_groups_hw03.py"], "28 nhóm (SV chốt), 28 khung"),
    ("T12", "Danh sách ảnh thiếu (`missing_photos.md`)", ["HW03/checklist/missing_photos.md"], "đối chiếu RUN.md/report"),
    ("B1", "Kiểm trùng 179 issue nhóm (`dup_check.md`; AI đề xuất mức, SV quyết)", ["HW03/bugs/dup_check.md"], "trùng / một phần / mới theo item Failed"),
    ("B2", "Khung BUG-58…85 theo mẫu HW02 (chỉ dữ kiện) + script `bug_skeleton_hw03.py`", ["tools/bug_skeleton_hw03.py"], "28 file khung; Tiêu đề/Steps/Severity… để SV viết"),
    ("B3", "Kiểm dữ kiện 28 bug + tái hiện Steps SV bằng Playwright (`bug_check.md`, `repro_bugs.spec.ts`)", ["HW03/bugs/bug_check.md", "HW03/tests/repro_bugs.spec.ts", "HW03/tests/repro.config.ts", "HW03/bugs/repro/repro_P1.json", "HW03/bugs/repro/repro_P2.json"], "sạch 14 / còn điểm 14; P1, P2"),
    ("B4", "Kiểm lại 14 bug SV sửa (`bug_check2.md`)", ["HW03/bugs/bug_check2.md"], "đã xử lý 6 / còn điểm 8"),
    ("B5", "Tạo 28 GitHub Issue bằng `gh issue create --body-file` (file SV viết) + ghi link vào BUG-xx, README, report", ["HW03/README.md"], "#247–#274 trên tkob-team/eshop-sut", "bf715c0"),
    ("B6", "Sửa body issue #266 + comment theo lệnh SV (`issue_edits.md`)", ["HW03/bugs/issue_edits.md"], "nhật ký lệnh `gh issue edit`/comment"),
    ("B7", "Ảnh trang Issues `[HW03-C2]` (Playwright chụp) chèn report §6", ["HW03/bugs/issues_page_HW03-C2_1.png", "HW03/bugs/issues_page_HW03-C2_2.png"], "25 + 3 issue"),
    ("U1", "Gói usability nháp – bản đóng băng (plan 9 phần, participant kit, phiếu quan sát)", ["HW03/appendix/ai-outputs/T2_plan_v1.md", "HW03/appendix/ai-outputs/T2_participant_kit_v1.md", "HW03/appendix/ai-outputs/T2_observation_sheet_v1.md"], "chưa dùng trong phiên thật"),
    ("U2", "Môi trường usability từ xa (script phiên, tunnel, đưa SUT về main) + sửa plan mục 5–6", ["tools/usability_session.ps1", "tools/sut_main.ps1", "tools/restart_backend.ps1", "HW03/usability/plan.md"], "nhánh local `usability-tunnel` trong eshop-sut (không nộp)"),
    ("U3", "Google Form SEQ + SUS + 4 câu hỏi mở (Apps Script – phiên thảo luận claude.ai)", ["HW03/usability/plan.md"], "form trên Google, không có file trong repo; CSV trả lời không commit", "2485116"),
    ("U4", "Kịch bản điều phối `moderator_script.md` (phiên thảo luận nháp, Claude Code commit nguyên văn)", ["HW03/usability/moderator_script.md"], "phiên ~10 phút"),
    ("U5", "Phiếu phiên S00…S07.json AI chép từ notes SV + CSV (`usability_fill_hw03.py`)", ["tools/usability_fill_hw03.py", "HW03/usability/sessions/S00.json"], "nhãn \"AI chép, SV duyệt\"; thời gian/hoàn thành/trợ giúp SV điền"),
    ("U6", "Đối chiếu 7 pain point §5.8 ↔ issue nhóm (chỉ đọc, trả lời trong phiên)", ["HW03/23120255_HW03_Report.md"], "bảng trùng / liên quan / chưa có; SV tự ghi vào report", "afc81da", "#184"),
    ("S1", "Agent Skill `gui-checklist-testing` (SKILL.md, reference, asset, 8 script)", ["HW03/skills/gui-checklist-testing"], "chép từ `.claude/skills/`"),
    ("S2", "Agent Skill `usability-evaluation` (SKILL.md, reference, asset, 6 script)", ["HW03/skills/usability-evaluation"], "chưa dùng trên phiên thật"),
    ("S3", "`skills/VideoLinks.md` + đề xuất demo (`demo_plan.md`, không nộp)", ["HW03/skills/VideoLinks.md", "HW03/skills/demo_plan.md"], "link `<SV điền>`"),
    ("R1", "Bảng report T1/T3 (§3.3, §3.5, §3.6, §4.1, §4.3)", ["tools/report_t1_hw03.py"], "khối giữa marker REPORT:T1"),
    ("R4", "AI nháp report §3.2, §4.2 (📝 AI nháp – SV duyệt/sửa)", ["HW03/23120255_HW03_Report.md"], "chỉ dùng dữ kiện trong repo", "ad992bc"),
    ("R2", "Test summary README + report §8 (11/11 thêm dòng U1 từ phiếu phiên)", ["tools/summary_hw03.py"], "khối SUMMARY"),
    ("R3", "Khung AI-02, AI-03, khối Mandatory Disclosure §11", ["tools/forms_hw03.py"], "file này"),
    ("E1", "Mô tả môi trường (`env/environment.md`)", ["HW03/env/environment.md"], "phiên bản trình duyệt/OS/thiết bị"),
]


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True, text=True, encoding="utf-8").stdout.strip()


def created(paths):
    """Commit đầu tiên thêm file chính (đường dẫn đầu); không có thì file sớm nhất trong danh sách."""
    out = git("log", "--diff-filter=A", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", "--", paths[0]).splitlines()
    if out:
        h, d, s = out[-1].split("|", 2)
        return (None, h, d, s)
    best = None
    for p in paths:
        out = git("log", "--diff-filter=A", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", "--follow", "--", p).splitlines()
        if out:
            h, d, s = out[-1].split("|", 2)
            key = dt.datetime.strptime(d, "%d/%m/%Y %H:%M")
            if best is None or key < best[0]:
                best = (key, h, d, s)
    return best


def fixed(h):
    """Commit tạo chỉ định tay (artifact không có file riêng hoặc file đã tồn tại trước)."""
    h2, d, s = git("log", "-1", "--format=%h|%ad|%s", "--date=format:%d/%m/%Y %H:%M", h).split("|", 2)
    return (None, h2, d, s)


_TURNS = None


def turns_before(h):
    """#n của các lượt có giờ trong (commit liền trước, commit h] theo git log --all (phút)."""
    global _TURNS
    if _TURNS is None:
        f = HW / "appendix" / "prompt_log_turns.txt"
        _TURNS = [(int(m.group(1)), m.group(2)[:16]) for m in re.finditer(r'^#(\d+)\s+\["([^"]+)"\]', f.read_text(encoding="utf-8"), re.M)] if f.exists() else []
        _TURNS.sort()
    times = sorted(set(git("log", "--all", "--format=%ad", "--date=format:%Y-%m-%d %H:%M").splitlines()))
    t = git("log", "-1", "--format=%ad", "--date=format:%Y-%m-%d %H:%M", h)
    prev = max((x for x in times if x < t), default="")
    ns = [n for n, k in _TURNS if prev < k <= t]
    if not ns:  # nhiều commit liền nhau trong cùng lượt → lượt cuối cùng có giờ ≤ commit
        ns = [n for n, k in _TURNS if k <= t][-1:]
    if not ns:
        return TBD
    rs, a = [], ns[0]
    for x, y in zip(ns, ns[1:] + [None]):
        if y != x + 1:
            rs.append(f"#{a}" if a == x else f"#{a}–#{x}")
            a = y
    return ", ".join(rs)


def later(paths, first):
    out = git("log", "--format=%h %s", f"{first}..HEAD", "--", *paths).splitlines()
    return list(reversed(out))


def totals():
    log = (HW / "appendix" / "A_prompt_log.md").read_text(encoding="utf-8")
    m = re.search(r"^\*\*Tổng:\*\* (.+)$", log, re.M)
    line = m.group(1) if m else ""
    n = re.match(r"(\d+) lượt", line)
    parts = re.findall(r"(Claude [^;]+?) (\d+) lượt \(([^)]*)\)", line)
    when = dt.datetime.fromtimestamp((HW / "appendix" / "A_prompt_log.md").stat().st_mtime).strftime("%H:%M %d/%m/%Y")
    return (int(n.group(1)) if n else 0), parts, when


def rows():
    out = []
    for code, name, paths, note, *fix in ART:
        c = fixed(fix[0]) if fix else created(paths)
        if not c:
            out.append((code, name, "chưa commit", note, "–"))
            continue
        _, h, d, s = c
        lt = later(paths, h)
        mod = "; ".join(f"`{x.split(' ', 1)[0]}` {x.split(' ', 1)[1]}" for x in lt[:4]) + (f"; … (+{len(lt) - 4})" if len(lt) > 4 else "") if lt else "không có"
        out.append((code, name, f"Claude Code · {d} · `{h}` ({s}) · {fix[1] if len(fix) > 1 else turns_before(h)}", f"{note} · " + ", ".join(f"`{p}`" for p in paths[:3]) + (" …" if len(paths) > 3 else ""), mod))
    return out


def kept():
    """Giữ ô em đã điền ở AI-02 (bảng 3.2, mục 4) khi chạy lại script."""
    f = HW / "ai-forms" / "AI-02_Audit_Report_23120255.md"
    if not f.exists():
        return {}
    t = f.read_text(encoding="utf-8")
    out = {}
    sec = t.split("### 3.2", 1)[-1].split("## 4.", 1)
    for line in sec[0].splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 4 and re.fullmatch(r"[A-Z]\d+", c[0]) and (c[2] != SV or c[3] != SV):
            out[c[0]] = (c[2], c[3])
    if len(sec) > 1:
        kl = sec[1].split("## 5.", 1)[0].split("\n", 1)[-1].strip()
        if kl and kl != SV:
            out["_kl"] = kl
    return out


def ai02(tot):
    n, parts, when = tot
    tools = "; ".join(f"{p[0]} {p[1]} lượt" for p in parts)
    L = HEAD + ["# AI Audit Report — Mẫu 5 mục cho mỗi Artifact", "", "*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW#01–HW#06, Seminar).*", "",
                "## 1. Thông tin Sinh viên", "", "| Mục | Giá trị |", "|---|---|", "| Họ tên sinh viên (in hoa): | LÊ TẤN HIỆP |", "| MSSV: | 23120255 |",
                "| Lớp / Khoá: | Software Testing - 23_3 |", "| Mã bài tập: | HW03-AI – GUI & Usability on EShop |", "| Ngày làm bài: | 04/11/2026 – [...] |",
                f"| Công cụ AI đã dùng: | Claude (Anthropic) qua Claude Code và claude.ai — {tools} (tổng {n} lượt theo dòng Tổng của `appendix/A_prompt_log.md`, bản trích {when}) |",
                "| Có sử dụng AI: | [x] Có [ ] Không |", "", "**Tuyên bố sử dụng AI (đề):** xem report chính §11 Mandatory Disclosure.", "",
                "## 2. Hướng dẫn", "", "- Mỗi artifact do AI tạo là 1 hàng. Mục (1) Prompt + công cụ + thời gian + mã `#n`, (2) Output, (5) Bản SV sửa ở bảng 3.1; mục (3) Verdict và (4) Lý do ở bảng 3.2 (em viết).",
                "- Prompt và output nguyên văn: `appendix/A_prompt_log.md` theo mã `#n`; output dạng file đóng băng: `appendix/ai-outputs/`.",
                f"- Cột #n để \"{TBD}\" tới lần trích prompt log cuối (gồm transcript phiên claude.ai).", "",
                "## 3. Bảng Audit — 1 hàng / artifact", "", "### 3.1 Mục (1), (2), (5)", "",
                "| Mã | Artifact | (1) Tool · thời gian · commit tạo · #n | (2) Output (trích + đường dẫn) | (5) Commit sửa sau đó (git log) |", "|---|---|---|---|---|"]
    R = rows()
    for r in R:
        L.append("| " + " | ".join(r) + " |")
    L += ["", f"*{len(R)} artifact. Sinh bằng `tools/forms_hw03.py` từ danh mục trong script + `git log` (commit tạo = commit đầu tiên thêm file chính – đường dẫn đầu ở cột (2)). Cột (5) chỉ liệt kê commit, không diễn giải.*", "",
          "### 3.2 Mục (3), (4) – em điền", "", "*Verdict: VALID / INVALID / INCOMPLETE. Lý do: 1–2 câu, dẫn ISTQB/slide. #n để mở `appendix/A_prompt_log.md`.*", "",
          "| Mã | #n | (3) Verdict | (4) Lý do |", "|---|---|---|---|"]
    keep = kept()
    for code, name, c1, *_ in R:
        v, ly = keep.get(code, (SV, SV))
        L.append(f"| {code} | {c1.rsplit(' · ', 1)[-1]} | {v} | {ly} |")
    L += ["", "## 4. Kết luận chung", "", keep.get("_kl", SV), "", "## 5. AI Critique", "", "Xem report chính `23120255_HW03_Report.md` §10.", ""] + SIGN + REFS
    return "\n".join(L)


def unknown_lines(parts):
    """Mỗi lượt không rõ model một dòng; notes đã có khoá giờ đơn → trỏ tới notes, chưa có → <SV viết>."""
    turns = {}
    f = HW / "appendix" / "prompt_log_turns.txt"
    if f.exists():
        turns = {int(m.group(1)): m.group(2) for m in re.finditer(r'^#(\d+)\s+\["([^"]+)"\]', f.read_text(encoding="utf-8"), re.M)}
    notes = (HW / "appendix" / "prompt_log_notes.toml").read_text(encoding="utf-8")
    out = []
    for name, _, ids in parts:
        if "không rõ" not in name:
            continue
        for x in re.findall(r"#(\d+)", ids):
            k = turns.get(int(x), "?")
            has = re.search(r'^\["' + re.escape(k) + r'"\]', notes, re.M)
            out.append(f"  - #{x} (`{k}`): " + ("xem notes khoá này" if has else SV))
    return out


def ai03(tot):
    n, parts, when = tot
    L = HEAD + ["# Biểu mẫu Khai báo Sử dụng AI", "", "*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*", "",
                "## 1. Thông tin Môn học & Sinh viên", "", "| Mục | Giá trị |", "|---|---|", "| Môn học: | CSC13003 – Kiểm chứng Phần mềm |",
                "| Mã bài tập: | HW03-AI |", "| Tên bài tập: | GUI & Usability on EShop |", "| Cấp độ AI (1–5): | Cấp 4 |", "| Ngày: | [...] |",
                "| Họ tên sinh viên: | Lê Tấn Hiệp |", "| MSSV: | 23120255 |", "", "## 2. Câu hỏi Khai báo", "", "### 1. Công cụ AI đã dùng:", ""]
    for name, k, ids in parts:
        extra = f" ({ids})" if "không rõ" in name else ""
        L.append(f"- **{name}** – {k} lượt{extra}")
    L += [f"- Tổng {n} lượt theo dòng \"Tổng\" của `appendix/A_prompt_log.md` (bản trích {when}; chạy lại sau lần trích cuối). Danh sách mã `#n` từng model ở dòng đó.",
          "- Các lượt \"Claude (không rõ model)\": transcript không ghi model; giữ nguyên trong log. Lý do từng lượt (em ghi, nguồn `appendix/prompt_log_notes.toml`):",
          *unknown_lines(parts),
          "- Kênh: Claude Code (chạy lệnh, sửa file, commit trong repo) và claude.ai (phiên thảo luận, lập lệnh, review).", "",
          "### 2. Giai đoạn nào của bài tập có dùng AI:", "", "`<SV điền>` (tick: brainstorm / outline / viết nháp / phản hồi / sửa chữa / code / phân tích dữ liệu / thiết kế đồ hoạ / khác)", "",
          "### 3. Prompt / nhiệm vụ chính cho AI:", "", "`<SV điền>` (chọn 2–3 lượt tiêu biểu theo mã `#n` trong `appendix/A_prompt_log.md`)", "",
          "### 4. Phần cụ thể AI đóng góp:", "", "Theo bảng artifact của AI-02 (mục 3.1): " + "; ".join(f"{c} {a}" for c, a, *_ in ART) + ".", "",
          "**Phần AI KHÔNG đóng góp (em tự làm):** `<SV điền>`", "",
          "**Danh mục AI không được làm (CLAUDE.md mục 3, HW03/CLAUDE.md mục 5):** không viết/nháp mô tả bug và nội dung issue; không gợi ý item khi em đang tự bổ sung (T1 bước 2); "
          "không viết AI Critique, phân tích \"vì sao AI bỏ sót\" trong report, verdict Audit; không tạo/ghép ảnh overlay; không điền dữ liệu người tham gia, SUS/SEQ.", "",
          "### 5. Cách em rà soát / chỉnh sửa / xác minh đầu ra AI:", "", SV, "",
          "### 6. Trích dẫn tool AI sử dụng:", ""]
    k = 1
    for name, *_ in parts:
        if "không rõ" in name:
            continue
        L += [f"[{k}] Anthropic. (2026). *{name}* [Large language model]. https://claude.ai", ""]
        k += 1
    L += [f"[{k}] Anthropic. (2026). *Claude Code* [Software]. https://claude.com/claude-code", "", "## 3. Cam đoan Trung thực", "",
          "*Bằng việc ký tên dưới đây, em cam đoan thông tin khai báo ở trên là chính xác và đầy đủ.* [...]", ""] + SIGN + REFS
    return "\n".join(L)


def disclosure():
    L = ["📝 AI nháp – SV xác nhận", "", "*\"I use AI tools for the following tasks,\"*", ""]
    items = [
        "Dựng harness bài làm (`HW03/CLAUDE.md`, kế hoạch nộp, script gộp/sinh bảng trong `tools/`), Agent Skill `gui-checklist-testing` và `usability-evaluation` (`skills/`).",
        "Khảo sát control C2 và nháp checklist 65 item theo 3 nguồn (SRS / control / heuristic); bản nháp đóng băng ở `appendix/ai-outputs/T1_checklist_ai_v1.json` trước khi em review.",
        "Trả lời \"vì sao AI bỏ sót\" sau khi em đã commit item của mình (`checklist/ai_gap_answer.md`).",
        "Viết test Playwright cho 59 item auto (P1, P2, P3), `RUN.md` cho phần chạy tay, `dom_probe.js`; kiểm ảnh/kết quả chạy tay (`checklist/run_check.md`), nén ảnh, gộp lượt auto + tay, Excel.",
        "Đối chiếu item Failed với issue nhóm (`bugs/failed_list.md`, `bugs/dup_check.md`), đề xuất nhóm dữ kiện bug, dựng khung `BUG-58…85` chỉ chứa dữ kiện.",
        "Nháp gói usability (plan 9 phần, participant kit, phiếu quan sát; đóng băng ở `appendix/ai-outputs/T2_*`) và script môi trường usability từ xa.",
        "Sinh bảng cho report/README (§3.3, §3.5, §3.6, §4.1, §4.3, §8), nháp §3.2, §4.2 (đánh dấu 📝 AI nháp), khung AI-02, AI-03.",
    ]
    L += [f"{k}. {t}" for k, t in enumerate(items, 1)]
    L += ["", "Em xem xét và sửa: `<SV viết>`", "", "Em tự làm hoàn toàn: `<SV viết>`", "",
          "Prompt log: trích tự động bằng `tools/extract_prompt_log.py` (hook `tools/hooks/on_stop.py`); Section / Mục đích / Xử lý do em ghi. Danh mục artifact AI: `ai-forms/AI-02_Audit_Report_23120255.md`.",
          "", "*Sinh bằng `tools/forms_hw03.py` từ `report_plan.md` mục f, g.*", ""]
    return "\n".join(L)


def main():
    tot = totals()
    (HW / "ai-forms").mkdir(exist_ok=True)
    (HW / "ai-forms" / "AI-02_Audit_Report_23120255.md").write_text(ai02(tot), encoding="utf-8")
    (HW / "ai-forms" / "AI-03_Disclosure_Form_23120255.md").write_text(ai03(tot), encoding="utf-8")
    rp = HW / "23120255_HW03_Report.md"
    t = rp.read_text(encoding="utf-8")
    pat = re.compile(r"(<!-- REPORT:HW03:disclosure:START -->\n).*?(<!-- REPORT:HW03:disclosure:END -->)", re.S)
    ok = bool(pat.search(t))
    if ok:
        rp.write_text(pat.sub(lambda m: m.group(1) + disclosure() + m.group(2), t, count=1), encoding="utf-8")
    print(f"AI-02, AI-03 đã ghi; tổng {tot[0]} lượt ({tot[2]}); §11: {'đã ghi' if ok else 'CHƯA CÓ MARKER'}")


if __name__ == "__main__":
    main()
