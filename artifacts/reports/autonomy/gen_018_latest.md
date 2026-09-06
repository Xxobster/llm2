# Autonomy public-indicator hunt gen 018

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T084732Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `fi_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8008 | 0.6771 | 3.8681 | 0.0205 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `fi_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8008 | 0.6771 | 3.8681 | 0.0205 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `fi_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2134 | 0.6946 | 4.1529 | 0.0182 | 0.4192 | EBR>35% | RAN |
| SOLUSDT | 4 | `fi_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2008 | 0.6909 | 4.0997 | 0.0182 | 0.4242 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `fi_cross_down_0` | one_head_filter_pi_star | 19 | 1.6855 | 2.5844 | 0.6842 | 1.5821 | 0.0134 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `fi_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2179 | 0.5963 | 1.0035 | 0.0070 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `fi_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2179 | 0.5963 | 1.0035 | 0.0069 | 0.2050 | ok | RAN |
| SOLUSDT | 4 | `fi_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.4019 | 0.6000 | 2.1413 | 0.0058 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `fi_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3839 | 0.5952 | 2.0616 | 0.0056 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `fi_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `fi_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `fi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `fi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `fi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `fi_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `fi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `fi_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `fi_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `fi_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
