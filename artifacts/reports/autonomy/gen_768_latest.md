# Autonomy public-indicator hunt gen 768

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T123155Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1520_below_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.7885 | 0.6557 | 4.1474 | 0.0190 | 0.3260 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1520_below_at_h` | one_head_filter_pi_star | 271 | 22.1382 | 1.6802 | 0.6494 | 3.7033 | 0.0169 | 0.3247 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1520_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 2.0240 | 0.7031 | 2.2998 | 0.0141 | 0.2656 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1520_above_at_h` | one_head_filter_pi_star | 91 | 7.5101 | 1.2851 | 0.6044 | 0.9838 | 0.0115 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `sma1520_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.7678 | 0.6361 | 4.1195 | 0.0113 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1520_above_at_h` | one_head_filter_pi_star | 73 | 6.0672 | 1.6933 | 0.6849 | 1.9483 | 0.0109 | 0.3151 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1520_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 1.7130 | 0.6287 | 3.8684 | 0.0108 | 0.3192 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1520_above_at_h` | one_head_filter_pi_star | 89 | 7.3450 | 1.1513 | 0.5843 | 0.5713 | 0.0061 | 0.2360 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1520_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1520_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
