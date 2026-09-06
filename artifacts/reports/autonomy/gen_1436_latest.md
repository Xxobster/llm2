# Autonomy public-indicator hunt gen 1436

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T171943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema963_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema963_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8680 | 0.6699 | 3.8197 | 0.0199 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema963_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.8362 | 0.6596 | 3.9443 | 0.0196 | 0.3447 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema963_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.8290 | 0.6524 | 3.8841 | 0.0126 | 0.3219 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema963_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 1.3251 | 0.6103 | 1.4595 | 0.0116 | 0.2426 | ok | RAN |
| SOLUSDT | 4 | `ema963_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.6698 | 0.6375 | 3.4036 | 0.0109 | 0.3028 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema963_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.7289 | 0.6457 | 2.4801 | 0.0107 | 0.3228 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema963_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.6114 | 0.6311 | 2.1865 | 0.0092 | 0.3115 | ok | RAN |
| ETHUSDT | 4 | `ema963_above_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.1421 | 0.5806 | 0.6199 | 0.0057 | 0.2097 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema963_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema963_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema963_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema963_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema963_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
