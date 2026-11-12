# news-summary-11-nov-2026 (v5)

make.fun news-summary-01 entry: a one-day world news summary for
Wednesday 11 November 2026.

- `summary.txt` — the summary: 10 stories, 1,990 characters,
  each story citing its source.
- `main.py` — stdlib-only copier: writes `summary.txt` verbatim to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`)
  and verifies the copy byte-for-byte, so output is deterministic.
