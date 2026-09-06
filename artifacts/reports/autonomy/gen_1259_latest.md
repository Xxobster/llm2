# Autonomy public-indicator hunt gen 1259

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T161344Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma637_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0589 | 0.6862 | 4.4505 | 0.0245 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma637_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0347 | 0.6859 | 4.4230 | 0.0232 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma637_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8066 | 0.6718 | 3.5726 | 0.0126 | 0.3282 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma637_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 1.7653 | 0.6650 | 3.3660 | 0.0118 | 0.3200 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma637_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.3245 | 0.6273 | 1.5482 | 0.0111 | 0.2112 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma637_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.6209 | 0.6258 | 2.5287 | 0.0097 | 0.3097 | ok | RAN |
| SOLUSDT | 4 | `sma637_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.4465 | 0.6000 | 1.8685 | 0.0074 | 0.3143 | ok | RAN |
| ETHUSDT | 4 | `sma637_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1565 | 0.5875 | 0.7858 | 0.0058 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma637_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma637_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma637_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma637_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma637_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma637_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
