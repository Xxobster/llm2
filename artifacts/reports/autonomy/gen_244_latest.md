# Autonomy public-indicator hunt gen 244

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T013309Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema75_cross_up` | one_head_filter_pi_star | 12 | 1.0195 | 22.1956 | 0.9167 | 2.8678 | 0.0476 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema75_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8383 | 0.6798 | 4.0532 | 0.0215 | 0.3695 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema75_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7852 | 0.6766 | 3.8715 | 0.0202 | 0.3582 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema75_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1454 | 0.6852 | 3.9970 | 0.0172 | 0.4074 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema75_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1304 | 0.6852 | 3.8898 | 0.0171 | 0.4074 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema75_cross_down` | one_head_filter_pi_star | 20 | 1.9353 | 2.2353 | 0.7500 | 1.5060 | 0.0161 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema75_cross_down` | one_head_filter_pi_star | 19 | 1.5744 | 1.3149 | 0.5263 | 0.5456 | 0.0134 | 0.3158 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema75_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3172 | 0.6158 | 1.4679 | 0.0099 | 0.2203 | ok | RAN |
| ETHUSDT | 8 | `ema75_above_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.2879 | 0.6092 | 1.3184 | 0.0091 | 0.2126 | ok | RAN |
| SOLUSDT | 8 | `ema75_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3809 | 0.6009 | 1.9865 | 0.0056 | 0.2582 | ok | RAN |
| SOLUSDT | 4 | `ema75_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3183 | 0.5905 | 1.6912 | 0.0048 | 0.2571 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema75_cross_up` | one_head_filter_pi_star | 16 | 1.3885 | 0.7607 | 0.3750 | -0.4772 | -0.0104 | 0.3750 | EBR>35% | RAN |
| BTCUSDT | 4 | `ema75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema75_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema75_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema75_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema75_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
