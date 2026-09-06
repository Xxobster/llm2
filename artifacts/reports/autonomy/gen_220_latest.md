# Autonomy public-indicator hunt gen 220

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T235518Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema52_cross_up` | one_head_filter_pi_star | 17 | 1.4409 | 8.8562 | 0.8235 | 2.8138 | 0.0521 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema52_cross_down` | one_head_filter_pi_star | 22 | 1.8777 | 5.0509 | 0.8182 | 2.5863 | 0.0318 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema52_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.8221 | 0.6840 | 3.9260 | 0.0212 | 0.3774 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema52_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.7848 | 0.6847 | 3.7888 | 0.0206 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema52_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1108 | 0.6832 | 3.8414 | 0.0171 | 0.4161 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema52_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.0849 | 0.6813 | 3.7881 | 0.0168 | 0.4250 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema52_cross_up` | one_head_filter_pi_star | 21 | 1.8278 | 1.3123 | 0.5714 | 0.5327 | 0.0100 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema52_above_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.2534 | 0.6000 | 1.1558 | 0.0078 | 0.2121 | ok | RAN |
| ETHUSDT | 4 | `ema52_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2410 | 0.5977 | 1.1317 | 0.0075 | 0.2069 | ok | RAN |
| ETHUSDT | 8 | `ema52_cross_down` | one_head_filter_pi_star | 19 | 1.8933 | 1.1894 | 0.4737 | 0.3771 | 0.0065 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema52_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3837 | 0.6000 | 2.0115 | 0.0056 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `ema52_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3544 | 0.5981 | 1.9182 | 0.0052 | 0.2430 | ok | RAN |
| ETHUSDT | 4 | `ema52_cross_up` | one_head_filter_pi_star | 15 | 1.3056 | 1.0845 | 0.5333 | 0.1353 | 0.0037 | 0.2667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema52_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema52_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema52_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema52_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema52_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema52_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
