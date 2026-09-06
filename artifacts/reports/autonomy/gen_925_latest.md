# Autonomy public-indicator hunt gen 925

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T041406Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret179_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1094 | 0.7017 | 4.6615 | 0.0262 | 0.4033 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret179_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.0664 | 0.6988 | 4.3866 | 0.0246 | 0.3855 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret179_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1027 | 0.6707 | 3.9405 | 0.0162 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret179_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 1.9852 | 0.6603 | 3.5756 | 0.0148 | 0.3782 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret179_pos_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.5116 | 0.6154 | 2.4969 | 0.0076 | 0.2596 | ok | RAN |
| ETHUSDT | 8 | `ret179_pos_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.2246 | 0.5968 | 1.1710 | 0.0076 | 0.2151 | ok | RAN |
| ETHUSDT | 4 | `ret179_pos_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.1914 | 0.5864 | 1.0104 | 0.0065 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `ret179_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4113 | 0.6091 | 2.0304 | 0.0064 | 0.2589 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret179_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret179_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret179_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret179_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret179_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret179_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
