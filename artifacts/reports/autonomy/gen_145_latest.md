# Autonomy public-indicator hunt gen 145

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T185951Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema72_cross_up` | one_head_filter_pi_star | 12 | 1.1700 | 38.3145 | 0.9167 | 3.0550 | 0.0613 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema72_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8703 | 0.6881 | 4.1288 | 0.0217 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema72_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.7984 | 0.6800 | 3.8239 | 0.0205 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema72_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2275 | 0.6928 | 4.1979 | 0.0181 | 0.4036 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema72_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1702 | 0.6894 | 3.9877 | 0.0175 | 0.4161 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema72_cross_down` | one_head_filter_pi_star | 25 | 2.4191 | 2.3364 | 0.6400 | 1.7071 | 0.0153 | 0.0400 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema72_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3614 | 0.6215 | 1.6569 | 0.0108 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema72_cross_down` | one_head_filter_pi_star | 23 | 1.9059 | 1.2438 | 0.5217 | 0.4855 | 0.0096 | 0.3043 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema72_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2639 | 0.6066 | 1.2516 | 0.0084 | 0.2186 | ok | RAN |
| SOLUSDT | 8 | `ema72_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3484 | 0.5943 | 1.8382 | 0.0052 | 0.2547 | ok | RAN |
| SOLUSDT | 4 | `ema72_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.2985 | 0.5885 | 1.5968 | 0.0045 | 0.2536 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema72_cross_up` | one_head_filter_pi_star | 26 | 2.2562 | 0.5976 | 0.3846 | -1.1218 | -0.0211 | 0.3462 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema72_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema72_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema72_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema72_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
