# Autonomy public-indicator hunt gen 182

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T212417Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma25_cross_up` | one_head_filter_pi_star | 35 | 2.8800 | 1.6389 | 0.6286 | 1.2456 | 0.0212 | 0.3429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma25_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8331 | 0.6833 | 3.9477 | 0.0210 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma25_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma25_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma25_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0179 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma25_cross_down` | one_head_filter_pi_star | 25 | 2.1168 | 2.8690 | 0.7600 | 1.9529 | 0.0145 | 0.1200 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma25_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `wma25_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1991 | 0.5938 | 0.9235 | 0.0065 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma25_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3736 | 0.5935 | 2.0205 | 0.0055 | 0.2430 | ok | RAN |
| SOLUSDT | 4 | `wma25_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3700 | 0.5953 | 2.0019 | 0.0055 | 0.2465 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma25_cross_down` | one_head_filter_pi_star | 27 | 2.5158 | 0.7911 | 0.4444 | -0.5077 | -0.0067 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma25_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma25_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `wma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma25_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma25_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
