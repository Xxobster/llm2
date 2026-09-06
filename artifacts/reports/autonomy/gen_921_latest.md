# Autonomy public-indicator hunt gen 921

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T034443Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1860_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1860_above_at_h` | one_head_filter_pi_star | 54 | 4.7488 | 1.5519 | 0.6296 | 1.3339 | 0.0187 | 0.2778 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1860_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5797 | 0.6409 | 3.5659 | 0.0156 | 0.3116 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1860_below_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.5725 | 0.6386 | 3.4740 | 0.0155 | 0.3133 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1860_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.8521 | 0.6545 | 4.3188 | 0.0131 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1860_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.8002 | 0.6502 | 4.2035 | 0.0127 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1860_above_at_h` | one_head_filter_pi_star | 109 | 8.8894 | 1.5865 | 0.6330 | 1.9854 | 0.0083 | 0.2661 | ok | RAN |
| SOLUSDT | 8 | `ema1860_above_at_h` | one_head_filter_pi_star | 101 | 8.2360 | 1.5294 | 0.6337 | 1.7810 | 0.0076 | 0.2475 | ok | RAN |
| ETHUSDT | 4 | `ema1860_above_at_h` | one_head_filter_pi_star | 56 | 4.9247 | 1.1065 | 0.5714 | 0.3230 | 0.0040 | 0.2321 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1860_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1860_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
