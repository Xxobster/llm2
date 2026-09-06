# Autonomy public-indicator hunt gen 784

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T141327Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1560_below_at_h` | one_head_filter_pi_star | 265 | 21.6481 | 1.7514 | 0.6566 | 3.8700 | 0.0184 | 0.3358 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1560_below_at_h` | one_head_filter_pi_star | 269 | 21.9748 | 1.7012 | 0.6506 | 3.7510 | 0.0175 | 0.3271 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1560_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 2.1950 | 0.7115 | 2.5483 | 0.0163 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1560_below_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.8348 | 0.6421 | 4.3066 | 0.0121 | 0.3177 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1560_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7406 | 0.6340 | 3.9444 | 0.0112 | 0.3170 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1560_above_at_h` | one_head_filter_pi_star | 69 | 5.7358 | 1.7250 | 0.6957 | 1.9201 | 0.0101 | 0.3478 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1560_above_at_h` | one_head_filter_pi_star | 81 | 6.8925 | 1.1601 | 0.5926 | 0.5733 | 0.0068 | 0.2346 | ok | RAN |
| ETHUSDT | 8 | `sma1560_above_at_h` | one_head_filter_pi_star | 76 | 6.2722 | 1.1110 | 0.5658 | 0.3937 | 0.0047 | 0.2237 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1560_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1560_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0563 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
