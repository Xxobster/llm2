# Autonomy public-indicator hunt gen 078

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T143956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `atrf_high_at_h` | one_head_filter_pi_star | 15 | 1.5515 | 10.2522 | 0.9333 | 3.2873 | 0.0648 | 0.8667 | EBR>35% | RAN |
| ETHUSDT | 4 | `atrf_high_at_h` | one_head_filter_pi_star | 16 | 1.6549 | 10.6554 | 0.9375 | 3.5536 | 0.0638 | 0.9375 | EBR>35% | RAN |
| SOLUSDT | 8 | `atrf_cross_up_p01` | one_head_filter_pi_star | 14 | 1.5043 | 53.2053 | 0.9286 | 3.7294 | 0.0558 | 0.8571 | EBR>35% | RAN |
| SOLUSDT | 8 | `atrf_high_at_h` | one_head_filter_pi_star | 17 | 1.9574 | 3.7487 | 0.8235 | 2.6094 | 0.0290 | 0.8235 | EBR>35% | RAN |
| SOLUSDT | 4 | `atrf_high_at_h` | one_head_filter_pi_star | 21 | 2.2438 | 4.4785 | 0.8571 | 2.9173 | 0.0247 | 0.8571 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `atrf_low_at_h` | one_head_filter_pi_star | 136 | 11.3311 | 1.1652 | 0.5588 | 0.7508 | 0.0021 | 0.0809 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `atrf_low_at_h` | one_head_filter_pi_star | 144 | 11.9171 | 1.0408 | 0.5486 | 0.2028 | 0.0006 | 0.0833 | ok | RAN |
| ETHUSDT | 8 | `atrf_low_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 0.8816 | 0.5497 | -0.7035 | -0.0034 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `atrf_low_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8452 | 0.5410 | -0.9795 | -0.0047 | 0.1093 | ok | RAN |
| BTCUSDT | 4 | `atrf_low_at_h` | one_head_filter_pi_star | 22 | 1.8721 | 0.8123 | 0.3636 | -0.3838 | -0.0159 | 0.0455 | TPM<MIN | RAN |
| BTCUSDT | 8 | `atrf_low_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.6703 | 0.3333 | -0.7048 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `atrf_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `atrf_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `atrf_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atrf_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atrf_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atrf_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atrf_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atrf_cross_down_p005` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
