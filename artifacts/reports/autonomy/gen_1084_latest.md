# Autonomy public-indicator hunt gen 1084

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T210645Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema911_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 1.8066 | 0.6583 | 3.8963 | 0.0194 | 0.3458 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema911_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.7295 | 0.6504 | 3.5029 | 0.0177 | 0.3451 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema911_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.7709 | 0.6471 | 3.6538 | 0.0118 | 0.3067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema911_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.7000 | 0.6367 | 3.5604 | 0.0112 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema911_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.7189 | 0.6308 | 2.5200 | 0.0100 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema911_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.6260 | 0.6190 | 2.2952 | 0.0092 | 0.3175 | ok | RAN |
| ETHUSDT | 8 | `ema911_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.2300 | 0.6016 | 0.9937 | 0.0088 | 0.2188 | ok | RAN |
| ETHUSDT | 4 | `ema911_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.1532 | 0.5938 | 0.7091 | 0.0059 | 0.2109 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema911_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema911_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema911_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema911_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema911_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema911_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
