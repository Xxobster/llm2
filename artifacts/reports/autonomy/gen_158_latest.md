# Autonomy public-indicator hunt gen 158

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T195033Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma80_cross_up` | one_head_filter_pi_star | 20 | 1.6626 | 6.3551 | 0.7000 | 2.6291 | 0.0374 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma80_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8022 | 0.6779 | 3.8216 | 0.0209 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma80_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7376 | 0.6697 | 3.6662 | 0.0199 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma80_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1241 | 0.6855 | 3.9028 | 0.0174 | 0.4214 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma80_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1021 | 0.6855 | 3.9140 | 0.0169 | 0.4088 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma80_cross_down` | one_head_filter_pi_star | 38 | 3.2433 | 1.9613 | 0.6842 | 1.6701 | 0.0168 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma80_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2753 | 0.6051 | 1.2343 | 0.0082 | 0.2102 | ok | RAN |
| ETHUSDT | 4 | `wma80_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2322 | 0.6012 | 1.0677 | 0.0071 | 0.2147 | ok | RAN |
| ETHUSDT | 8 | `wma80_cross_up` | one_head_filter_pi_star | 24 | 2.0889 | 1.1532 | 0.5417 | 0.2935 | 0.0058 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma80_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3533 | 0.5935 | 1.9160 | 0.0052 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `wma80_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3380 | 0.5962 | 1.7958 | 0.0050 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma80_cross_down` | one_head_filter_pi_star | 25 | 2.0716 | 0.8768 | 0.5200 | -0.2790 | -0.0058 | 0.2400 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma80_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma80_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma80_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma80_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
