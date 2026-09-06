# Autonomy public-indicator hunt gen 857

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T210727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1700_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1700_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1700_below_at_h` | one_head_filter_pi_star | 297 | 24.2622 | 1.6969 | 0.6498 | 3.7557 | 0.0171 | 0.3232 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1700_below_at_h` | one_head_filter_pi_star | 324 | 26.4678 | 1.5996 | 0.6420 | 3.6564 | 0.0161 | 0.3117 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1700_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 1.8242 | 0.6506 | 4.1821 | 0.0134 | 0.3234 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1700_below_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 1.7790 | 0.6454 | 4.0344 | 0.0126 | 0.3262 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1700_above_at_h` | one_head_filter_pi_star | 60 | 5.2764 | 1.3047 | 0.6167 | 0.8899 | 0.0118 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1700_above_at_h` | one_head_filter_pi_star | 106 | 8.6447 | 1.5484 | 0.6321 | 1.8229 | 0.0078 | 0.2642 | ok | RAN |
| SOLUSDT | 8 | `ema1700_above_at_h` | one_head_filter_pi_star | 104 | 8.4816 | 1.4161 | 0.5962 | 1.4658 | 0.0064 | 0.2404 | ok | RAN |
| ETHUSDT | 8 | `ema1700_above_at_h` | one_head_filter_pi_star | 48 | 4.2211 | 1.1046 | 0.5833 | 0.2999 | 0.0044 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1700_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1700_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0653 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
