# Autonomy public-indicator hunt gen 553

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T212628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema940_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema940_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.9555 | 0.6770 | 4.2746 | 0.0214 | 0.3584 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema940_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.6869 | 0.6483 | 3.4853 | 0.0171 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema940_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.8381 | 0.6589 | 2.8183 | 0.0116 | 0.2946 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema940_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.7016 | 0.6400 | 3.5432 | 0.0113 | 0.3040 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema940_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.7128 | 0.6414 | 3.4604 | 0.0110 | 0.3122 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema940_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6212 | 0.6341 | 2.2653 | 0.0091 | 0.2927 | ok | RAN |
| ETHUSDT | 8 | `ema940_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.2022 | 0.5920 | 0.9053 | 0.0076 | 0.2320 | ok | RAN |
| ETHUSDT | 4 | `ema940_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 1.1669 | 0.5902 | 0.7231 | 0.0063 | 0.2213 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema940_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema940_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
