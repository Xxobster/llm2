# Research peek log

Append-only contamination ledger. Policy: **D-036**.

| Constant | Value |
|---|---|
| Forward lockbox start | `2026-05-01` |
| Post-multitrade freeze (clean param claims) | `2026-08-05` UTC |
| Contaminated diagnostic multitrade window | `[2026-05-01, 2026-08-05)` |

## Commands

```bash
python scripts/log_research_peek.py seed
python scripts/log_research_peek.py list
python scripts/log_research_peek.py append --experiment-id my_exp --window-end 2026-08-04 --purpose chart
python scripts/log_research_peek.py check-promote --claim promote_K8
```

Copying SQLite files does **not** clear peeks. Quotable historical edge = outer-fold settle only.
