# Autonomy public-indicator hunt gen 049

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T124454Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `clv_neg_at_h` | one_head_filter_pi_star | 196 | 16.0141 | 2.1676 | 0.7143 | 4.5101 | 0.0276 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 4 | `clv_neg_at_h` | one_head_filter_pi_star | 191 | 15.6056 | 2.0217 | 0.7016 | 4.1294 | 0.0232 | 0.3508 | EBR>35% | RAN |
| SOLUSDT | 8 | `clv_cross_up_0` | one_head_filter_pi_star | 96 | 7.8098 | 2.8373 | 0.7083 | 4.1120 | 0.0213 | 0.4271 | EBR>35% | RAN |
| SOLUSDT | 4 | `clv_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.5102 | 0.7108 | 4.7225 | 0.0206 | 0.4096 | EBR>35% | RAN |
| SOLUSDT | 8 | `clv_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.2774 | 0.6918 | 4.1314 | 0.0178 | 0.3899 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `clv_cross_up_0` | one_head_filter_pi_star | 41 | 3.3574 | 2.0547 | 0.6585 | 1.9025 | 0.0138 | 0.3902 | EBR>35% | RAN |
| ETHUSDT | 4 | `clv_pos_at_h` | one_head_filter_pi_star | 177 | 14.5014 | 1.3799 | 0.6102 | 1.7114 | 0.0120 | 0.2203 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `clv_cross_down_0` | one_head_filter_pi_star | 105 | 8.5420 | 1.5788 | 0.6000 | 2.0489 | 0.0088 | 0.2476 | ok | RAN |
| SOLUSDT | 4 | `clv_cross_down_0` | one_head_filter_pi_star | 32 | 2.6411 | 1.4642 | 0.5312 | 1.0268 | 0.0084 | 0.2812 | TPM<MIN | RAN |
| ETHUSDT | 8 | `clv_cross_down_0` | one_head_filter_pi_star | 101 | 8.3229 | 1.1759 | 0.5842 | 0.7181 | 0.0064 | 0.2376 | ok | RAN |
| SOLUSDT | 4 | `clv_pos_at_h` | one_head_filter_pi_star | 221 | 18.0204 | 1.3884 | 0.5973 | 2.1802 | 0.0061 | 0.2443 | ok | RAN |
| SOLUSDT | 8 | `clv_pos_at_h` | one_head_filter_pi_star | 213 | 17.4798 | 1.3476 | 0.5962 | 1.9671 | 0.0057 | 0.2535 | ok | RAN |
| ETHUSDT | 4 | `clv_cross_down_0` | one_head_filter_pi_star | 53 | 4.3675 | 1.1380 | 0.5849 | 0.4111 | 0.0049 | 0.2453 | ok | RAN |
| ETHUSDT | 8 | `clv_pos_at_h` | one_head_filter_pi_star | 192 | 15.7304 | 1.0506 | 0.5573 | 0.2656 | 0.0017 | 0.2135 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `clv_cross_up_0` | one_head_filter_pi_star | 98 | 8.0589 | 1.0022 | 0.5408 | 0.0092 | 0.0001 | 0.2857 | ok | RAN |
| BTCUSDT | 4 | `clv_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.8748 | 0.3529 | -0.2078 | -0.0090 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `clv_cross_up_0` | one_head_filter_pi_star | 65 | 5.5073 | 0.6673 | 0.4308 | -1.3694 | -0.0164 | 0.2308 | ok | RAN |
| BTCUSDT | 8 | `clv_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `clv_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `clv_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `clv_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `clv_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `clv_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `clv_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
