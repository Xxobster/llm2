# Autonomy public-indicator hunt gen 035

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T114954Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `rvi_cross_down_0` | one_head_filter_pi_star | 16 | 1.4095 | 6.0779 | 0.8750 | 2.4876 | 0.0294 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rvi_cross_up_0` | one_head_filter_pi_star | 18 | 1.5254 | 2.2610 | 0.7222 | 1.4473 | 0.0266 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rvi_cross_down_0` | one_head_filter_pi_star | 28 | 2.3958 | 1.5967 | 0.6429 | 1.0474 | 0.0214 | 0.3214 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rvi_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7870 | 0.6757 | 3.7948 | 0.0203 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `rvi_cross_down_0` | one_head_filter_pi_star | 34 | 2.8799 | 3.4398 | 0.7647 | 2.5723 | 0.0201 | 0.0882 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rvi_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7248 | 0.6727 | 3.5557 | 0.0194 | 0.3773 | EBR>35% | RAN |
| SOLUSDT | 8 | `rvi_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2459 | 0.6951 | 4.1658 | 0.0183 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `rvi_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1535 | 0.6871 | 3.9629 | 0.0176 | 0.4172 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `rvi_cross_up_0` | one_head_filter_pi_star | 13 | 1.1419 | 1.4179 | 0.6154 | 0.5627 | 0.0122 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `rvi_pos_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2242 | 0.5915 | 1.0306 | 0.0072 | 0.2012 | ok | RAN |
| ETHUSDT | 4 | `rvi_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2223 | 0.5875 | 1.0222 | 0.0069 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `rvi_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.4013 | 0.6000 | 2.1495 | 0.0060 | 0.2465 | ok | RAN |
| SOLUSDT | 4 | `rvi_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3931 | 0.5953 | 2.1189 | 0.0058 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `rvi_cross_up_0` | one_head_filter_pi_star | 23 | 1.8921 | 1.2131 | 0.6087 | 0.3779 | 0.0049 | 0.1304 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `rvi_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `rvi_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rvi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `rvi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `rvi_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `rvi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rvi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rvi_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `rvi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rvi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
