# Autonomy public-indicator hunt gen 1180

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T082046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema926_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 1.7689 | 0.6583 | 3.7427 | 0.0187 | 0.3458 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema926_below_at_h` | one_head_filter_pi_star | 247 | 20.1776 | 1.7195 | 0.6518 | 3.6059 | 0.0181 | 0.3360 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema926_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.3682 | 0.6154 | 1.6265 | 0.0133 | 0.2168 | ok | RAN |
| SOLUSDT | 4 | `ema926_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.7139 | 0.6484 | 3.6469 | 0.0114 | 0.3086 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema926_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.6870 | 0.6395 | 3.5624 | 0.0111 | 0.3062 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema926_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.7765 | 0.6489 | 2.6496 | 0.0109 | 0.3053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema926_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.7058 | 0.6341 | 2.4705 | 0.0099 | 0.3171 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema926_above_at_h` | one_head_filter_pi_star | 138 | 11.3889 | 1.1850 | 0.5870 | 0.8348 | 0.0070 | 0.2101 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema926_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema926_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema926_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema926_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema926_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema926_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
