# Autonomy public-indicator hunt gen 1179

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T081515Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma625_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1603 | 0.6952 | 4.7094 | 0.0254 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma625_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9939 | 0.6806 | 4.2546 | 0.0230 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma625_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.8332 | 0.6587 | 3.6803 | 0.0126 | 0.3173 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma625_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.7829 | 0.6667 | 3.4880 | 0.0122 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma625_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.5572 | 0.6196 | 2.4129 | 0.0087 | 0.3129 | ok | RAN |
| SOLUSDT | 8 | `sma625_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.5089 | 0.6127 | 2.0800 | 0.0081 | 0.3380 | ok | RAN |
| ETHUSDT | 8 | `sma625_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1445 | 0.5964 | 0.7417 | 0.0055 | 0.2289 | ok | RAN |
| ETHUSDT | 4 | `sma625_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.0982 | 0.5818 | 0.5174 | 0.0038 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
