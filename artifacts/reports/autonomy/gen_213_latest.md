# Autonomy public-indicator hunt gen 213

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T232610Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret12_cross_up_0` | one_head_filter_pi_star | 15 | 1.2835 | 4.1057 | 0.8000 | 2.1968 | 0.0729 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret12_cross_up_0` | one_head_filter_pi_star | 30 | 2.4768 | 2.9046 | 0.7667 | 2.4918 | 0.0487 | 0.3667 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret12_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8433 | 0.6820 | 3.9366 | 0.0212 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret12_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2426 | 0.6951 | 4.1776 | 0.0184 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret12_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.6814 | 0.6667 | 3.3425 | 0.0181 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret12_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1295 | 0.6928 | 3.9318 | 0.0173 | 0.4096 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret12_cross_down_0` | one_head_filter_pi_star | 34 | 2.9670 | 1.3747 | 0.5882 | 0.8148 | 0.0150 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret12_cross_up_0` | one_head_filter_pi_star | 17 | 1.6761 | 1.6218 | 0.5882 | 0.9374 | 0.0134 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret12_cross_down_0` | one_head_filter_pi_star | 27 | 2.4983 | 1.5137 | 0.6667 | 0.8920 | 0.0070 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret12_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2200 | 0.5901 | 1.0153 | 0.0068 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `ret12_cross_down_0` | one_head_filter_pi_star | 17 | 1.5730 | 1.2967 | 0.6471 | 0.4762 | 0.0064 | 0.0588 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret12_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3751 | 0.5945 | 2.0440 | 0.0056 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `ret12_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3830 | 0.5896 | 2.0487 | 0.0056 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `ret12_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1709 | 0.5886 | 0.7905 | 0.0055 | 0.1962 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret12_cross_down_0` | one_head_filter_pi_star | 20 | 2.4326 | 0.8887 | 0.5500 | -0.2711 | -0.0059 | 0.1500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret12_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret12_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret12_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret12_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret12_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret12_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret12_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret12_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret12_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
