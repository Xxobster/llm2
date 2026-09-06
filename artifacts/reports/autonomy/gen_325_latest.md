# Autonomy public-indicator hunt gen 325

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T110633Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret33_cross_up_0` | one_head_filter_pi_star | 21 | 1.7574 | 2.0844 | 0.6190 | 1.4496 | 0.0329 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret33_cross_down_0` | one_head_filter_pi_star | 33 | 2.8236 | 1.8781 | 0.5758 | 1.5623 | 0.0259 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret33_neg_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8336 | 0.6729 | 4.0195 | 0.0219 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret33_cross_down_0` | one_head_filter_pi_star | 27 | 2.2234 | 2.5640 | 0.6667 | 1.7984 | 0.0208 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret33_neg_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.7538 | 0.6667 | 3.7639 | 0.0202 | 0.3524 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret33_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0886 | 0.6786 | 3.9363 | 0.0168 | 0.3929 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret33_cross_up_0` | one_head_filter_pi_star | 17 | 1.4509 | 1.9422 | 0.5882 | 1.0831 | 0.0167 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret33_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 1.9737 | 0.6707 | 3.6086 | 0.0156 | 0.3963 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret33_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2795 | 0.6140 | 1.3237 | 0.0084 | 0.2398 | ok | RAN |
| SOLUSDT | 4 | `ret33_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.5320 | 0.6193 | 2.6260 | 0.0074 | 0.2615 | ok | RAN |
| SOLUSDT | 8 | `ret33_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.4759 | 0.6075 | 2.3789 | 0.0067 | 0.2523 | ok | RAN |
| ETHUSDT | 8 | `ret33_pos_at_h` | one_head_filter_pi_star | 169 | 13.9461 | 1.1770 | 0.5976 | 0.8700 | 0.0056 | 0.2130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret33_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret33_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret33_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret33_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret33_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret33_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret33_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret33_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret33_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret33_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret33_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret33_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
