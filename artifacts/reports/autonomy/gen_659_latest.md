# Autonomy public-indicator hunt gen 659

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T042019Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma388_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0921 | 0.7072 | 4.6607 | 0.0253 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma388_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0594 | 0.6968 | 4.5676 | 0.0237 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma388_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9725 | 0.6737 | 3.8938 | 0.0138 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma388_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.8986 | 0.6630 | 3.7479 | 0.0135 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma388_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2710 | 0.5926 | 1.3916 | 0.0091 | 0.2275 | ok | RAN |
| SOLUSDT | 8 | `sma388_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5789 | 0.6216 | 2.6605 | 0.0088 | 0.2757 | ok | RAN |
| SOLUSDT | 4 | `sma388_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4900 | 0.6096 | 2.3071 | 0.0078 | 0.2620 | ok | RAN |
| ETHUSDT | 8 | `sma388_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2147 | 0.5957 | 1.1413 | 0.0077 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma388_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma388_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma388_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma388_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma388_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma388_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
