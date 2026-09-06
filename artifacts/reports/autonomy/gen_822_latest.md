# Autonomy public-indicator hunt gen 822

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T174443Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma420_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9704 | 0.6995 | 4.2960 | 0.0227 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma420_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8679 | 0.6859 | 4.0095 | 0.0213 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma420_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2383 | 0.6961 | 4.4413 | 0.0169 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma420_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2145 | 0.6933 | 4.0859 | 0.0168 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma420_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2517 | 0.6011 | 1.3024 | 0.0086 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `wma420_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2273 | 0.6011 | 1.1992 | 0.0079 | 0.2234 | ok | RAN |
| SOLUSDT | 8 | `wma420_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4545 | 0.6094 | 2.2177 | 0.0069 | 0.2604 | ok | RAN |
| SOLUSDT | 4 | `wma420_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2768 | 0.5829 | 1.4800 | 0.0046 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma420_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
