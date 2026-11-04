/**
 * Reporter: gom kết quả theo mã item (đầu tiêu đề test) → HW03/checklist/runs/<P>_auto_<YYYYMMDD-HHMM>.json
 * (định dạng đầu vào merge_platform.py, kind = "auto" → ghi auto_status, không ghi ket_qua).
 * passed → Passed · failed/timedOut → Failed · skipped + annotation blocked → Blocked · skipped + manual → danh sách manual.
 * notes = các annotation obs + dòng đầu của từng lỗi soft-assert; partial = item mixed (phần còn lại chạy tay).
 */
import fs from 'fs';
import path from 'path';
import type { Reporter, TestCase, TestResult, FullConfig, Suite } from '@playwright/test/reporter';
import { ORACLE } from './oracle';

type Row = { status: string; notes: string; evidence: string[]; partial?: boolean };

export default class ChecklistReporter implements Reporter {
  private byProject: Record<string, { results: Record<string, Row>; manual: string[]; browser: string }> = {};
  private started = new Date();

  onBegin(_c: FullConfig, _s: Suite) { this.started = new Date(); }

  onTestEnd(test: TestCase, r: TestResult) {
    const project = test.parent.project()?.name ?? '?';
    const P = (this.byProject[project] ??= { results: {}, manual: [], browser: '' });
    const id = test.title.split(' ')[0];
    const ann = [...test.annotations, ...r.annotations];
    if (r.status === 'skipped' && ann.some(a => a.type === 'manual')) { P.manual.push(id); return; }
    const blocked = ann.find(a => a.type === 'blocked');
    const status = r.status === 'passed' ? 'Passed' : r.status === 'skipped' ? (blocked ? 'Blocked' : 'Skipped') : 'Failed';
    const errs = r.errors.map(e => (e.message ?? '').split('\n')[0].replace(/\u001b\[[0-9;]*m/g, '').trim()).filter(Boolean);
    const notes = [
      ...(blocked ? [blocked.description] : []),
      ...errs.map(e => `Lỗi: ${e}`),
      ...ann.filter(a => a.type === 'obs').map(a => a.description),
    ].join(' · ');
    P.results[id] = { status, notes, evidence: ann.filter(a => a.type === 'evidence').map(a => a.description!), ...(ORACLE[id]?.mixed ? { partial: true } : {}) };
  }

  onEnd() {
    const ts = this.started;
    const stamp = `${ts.getFullYear()}${String(ts.getMonth() + 1).padStart(2, '0')}${String(ts.getDate()).padStart(2, '0')}-${String(ts.getHours()).padStart(2, '0')}${String(ts.getMinutes()).padStart(2, '0')}`;
    const dir = path.resolve(__dirname, '../checklist/runs');
    fs.mkdirSync(dir, { recursive: true });
    for (const [project, P] of Object.entries(this.byProject)) {
      const env = project === 'P1' ? 'Google Chrome đã cài (Playwright channel "chrome")' : 'Firefox bản build của Playwright (không phải Firefox đã cài)';
      const out = { platform: project, kind: 'auto', run_at: ts.toISOString(), env, manual: P.manual, results: P.results };
      const file = path.join(dir, `${project}_auto_${stamp}.json`);
      fs.writeFileSync(file, JSON.stringify(out, null, 2) + '\n', 'utf-8');
      console.log(`[checklist] ${Object.keys(P.results).length} item → ${path.relative(process.cwd(), file)}`);
    }
  }
}
