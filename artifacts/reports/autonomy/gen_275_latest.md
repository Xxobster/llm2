# Autonomy public-indicator hunt gen 275

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T034235Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma82_cross_up` | one_head_filter_pi_star | 14 | 1.3378 | 6.0255 | 0.7143 | 2.3661 | 0.0329 | 0.0714 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma82_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9366 | 0.6959 | 4.2795 | 0.0228 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma82_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.7839 | 0.6749 | 3.7840 | 0.0203 | 0.3596 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma82_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2907 | 0.6941 | 4.4006 | 0.0187 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma82_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2387 | 0.6923 | 4.2761 | 0.0184 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma82_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3594 | 0.6145 | 1.6621 | 0.0108 | 0.2291 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma82_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.3274 | 0.6080 | 1.5077 | 0.0099 | 0.2330 | ok | RAN |
| SOLUSDT | 8 | `sma82_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3317 | 0.5962 | 1.7645 | 0.0050 | 0.2582 | ok | RAN |
| SOLUSDT | 4 | `sma82_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.2874 | 0.5905 | 1.5523 | 0.0044 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma82_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma82_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma82_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma82_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma82_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma82_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma82_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma82_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma82_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma82_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
