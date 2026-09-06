# Autonomy public-indicator hunt gen 429

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T090945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret55_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.7497 | 0.6774 | 3.6319 | 0.0199 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret55_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7072 | 0.6701 | 3.5534 | 0.0193 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret55_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1703 | 0.7052 | 4.1682 | 0.0175 | 0.3931 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret55_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.0691 | 0.6813 | 4.0819 | 0.0165 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret55_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.4063 | 0.6237 | 1.8785 | 0.0118 | 0.2366 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret55_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2603 | 0.5967 | 1.2862 | 0.0084 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `ret55_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.5339 | 0.6119 | 2.6546 | 0.0075 | 0.2587 | ok | RAN |
| SOLUSDT | 4 | `ret55_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4073 | 0.5970 | 2.1281 | 0.0059 | 0.2587 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret55_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret55_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret55_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret55_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret55_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret55_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
