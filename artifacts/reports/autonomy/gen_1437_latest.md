# Autonomy public-indicator hunt gen 1437

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T174414Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret249_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.2276 | 0.7055 | 4.4798 | 0.0274 | 0.3865 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret249_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.9776 | 0.6964 | 4.0176 | 0.0238 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret249_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.9902 | 0.6575 | 3.8691 | 0.0142 | 0.3536 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret249_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.6648 | 0.6344 | 3.0217 | 0.0106 | 0.3441 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret249_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.6231 | 0.6304 | 2.7642 | 0.0092 | 0.2935 | ok | RAN |
| SOLUSDT | 4 | `ret249_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5310 | 0.6209 | 2.3882 | 0.0082 | 0.2802 | ok | RAN |
| ETHUSDT | 4 | `ret249_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2198 | 0.5930 | 1.0671 | 0.0076 | 0.2384 | ok | RAN |
| ETHUSDT | 8 | `ret249_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1051 | 0.5789 | 0.5707 | 0.0039 | 0.2211 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret249_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret249_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret249_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret249_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret249_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret249_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
