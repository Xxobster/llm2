# Autonomy public-indicator hunt gen 968

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T194001Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2020_above_at_h` | one_head_filter_pi_star | 38 | 3.3275 | 1.5113 | 0.6316 | 1.1538 | 0.0194 | 0.3158 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma2020_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.6287 | 0.6456 | 3.7507 | 0.0165 | 0.3123 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2020_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5920 | 0.6441 | 3.6413 | 0.0161 | 0.3088 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2020_above_at_h` | one_head_filter_pi_star | 53 | 4.4057 | 1.8765 | 0.6792 | 1.8947 | 0.0125 | 0.3019 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2020_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.8696 | 0.6467 | 4.4057 | 0.0124 | 0.3100 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2020_above_at_h` | one_head_filter_pi_star | 69 | 5.7358 | 1.8328 | 0.6812 | 2.0272 | 0.0120 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2020_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.7698 | 0.6441 | 4.0905 | 0.0114 | 0.3051 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma2020_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.1659 | 0.5769 | 0.4653 | 0.0062 | 0.1923 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2020_above_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.4436 | 0.2500 | -1.0639 | -0.0579 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2020_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0867 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
