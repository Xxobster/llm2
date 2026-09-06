# Autonomy public-indicator hunt gen 1245

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T145438Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret221_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.1798 | 0.7110 | 4.5815 | 0.0268 | 0.3873 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret221_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1575 | 0.7081 | 4.8040 | 0.0265 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret221_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0194 | 0.6774 | 4.0146 | 0.0148 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret221_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8817 | 0.6597 | 3.6836 | 0.0135 | 0.3665 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret221_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.3087 | 0.6000 | 1.4994 | 0.0103 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret221_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.5506 | 0.6196 | 2.3855 | 0.0082 | 0.2761 | ok | RAN |
| SOLUSDT | 4 | `ret221_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.4993 | 0.6199 | 2.2270 | 0.0078 | 0.2749 | ok | RAN |
| ETHUSDT | 8 | `ret221_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.0770 | 0.5707 | 0.4149 | 0.0028 | 0.2323 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret221_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6964 | 0.3684 | -0.6260 | -0.0315 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret221_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret221_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret221_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret221_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret221_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
