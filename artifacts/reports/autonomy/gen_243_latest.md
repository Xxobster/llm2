# Autonomy public-indicator hunt gen 243

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T012854Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma62_cross_up` | one_head_filter_pi_star | 23 | 1.9120 | 6.3349 | 0.6957 | 2.8127 | 0.0350 | 0.2609 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma62_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7503 | 0.6699 | 3.6099 | 0.0201 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma62_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7447 | 0.6731 | 3.6342 | 0.0200 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma62_cross_down` | one_head_filter_pi_star | 26 | 2.1545 | 1.6379 | 0.5769 | 1.0769 | 0.0187 | 0.2692 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma62_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1986 | 0.6890 | 4.1672 | 0.0181 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma62_below_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.1023 | 0.6859 | 3.8842 | 0.0170 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma62_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.3076 | 0.6069 | 1.4073 | 0.0089 | 0.2197 | ok | RAN |
| ETHUSDT | 4 | `sma62_cross_down` | one_head_filter_pi_star | 14 | 1.3755 | 1.2141 | 0.5714 | 0.3794 | 0.0081 | 0.2143 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma62_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2033 | 0.5976 | 0.9511 | 0.0064 | 0.2134 | ok | RAN |
| SOLUSDT | 4 | `sma62_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3804 | 0.6009 | 1.9873 | 0.0055 | 0.2488 | ok | RAN |
| SOLUSDT | 8 | `sma62_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3237 | 0.5935 | 1.7252 | 0.0048 | 0.2477 | ok | RAN |
| SOLUSDT | 8 | `sma62_cross_down` | one_head_filter_pi_star | 31 | 2.6458 | 1.1965 | 0.6129 | 0.4013 | 0.0040 | 0.1935 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma62_cross_up` | one_head_filter_pi_star | 16 | 1.3926 | 0.7492 | 0.4375 | -0.5089 | -0.0121 | 0.1875 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma62_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma62_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma62_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma62_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma62_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma62_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma62_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma62_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma62_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma62_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma62_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
