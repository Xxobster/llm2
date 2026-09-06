# Autonomy public-indicator hunt gen 1388

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T043527Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema956_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 2.0271 | 0.6774 | 4.4204 | 0.0225 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema956_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.7661 | 0.6509 | 3.6041 | 0.0182 | 0.3448 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema956_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 1.4072 | 0.6183 | 1.6165 | 0.0141 | 0.2366 | ok | RAN |
| SOLUSDT | 4 | `ema956_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7684 | 0.6457 | 3.7818 | 0.0120 | 0.3071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema956_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.8127 | 0.6612 | 2.7712 | 0.0115 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema956_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.6909 | 0.6371 | 3.6082 | 0.0111 | 0.3050 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema956_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.7259 | 0.6610 | 2.4802 | 0.0104 | 0.3390 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema956_above_at_h` | one_head_filter_pi_star | 136 | 11.2239 | 1.1914 | 0.5882 | 0.8603 | 0.0074 | 0.2206 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema956_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema956_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema956_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema956_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema956_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema956_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
