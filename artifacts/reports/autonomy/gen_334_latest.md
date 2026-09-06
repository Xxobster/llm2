# Autonomy public-indicator hunt gen 334

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T120648Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma115_cross_up` | one_head_filter_pi_star | 23 | 1.9164 | 4.4789 | 0.6957 | 2.6156 | 0.0383 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma115_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9499 | 0.6974 | 4.3333 | 0.0232 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma115_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8885 | 0.6850 | 4.2010 | 0.0224 | 0.3700 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma115_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.3355 | 0.7000 | 4.4934 | 0.0193 | 0.4059 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma115_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2246 | 0.6933 | 4.1814 | 0.0182 | 0.4110 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `wma115_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.3436 | 0.6124 | 1.5907 | 0.0103 | 0.2303 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma115_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.2981 | 0.6102 | 1.3842 | 0.0092 | 0.2260 | ok | RAN |
| SOLUSDT | 8 | `wma115_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3471 | 0.5953 | 1.8422 | 0.0052 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `wma115_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3084 | 0.5935 | 1.6546 | 0.0047 | 0.2523 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma115_cross_down` | one_head_filter_pi_star | 29 | 2.8062 | 1.0476 | 0.5517 | 0.1126 | 0.0010 | 0.1034 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma115_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma115_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `wma115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma115_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma115_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
