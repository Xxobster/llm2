# Autonomy public-indicator hunt gen 357

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T160319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret38_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7161 | 0.6719 | 3.5930 | 0.0195 | 0.3646 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret38_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.6834 | 0.6667 | 3.3966 | 0.0187 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret38_neg_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.0800 | 0.6772 | 3.8376 | 0.0168 | 0.3924 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret38_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0053 | 0.6726 | 3.6963 | 0.0162 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret38_cross_down_0` | one_head_filter_pi_star | 38 | 3.1489 | 1.3174 | 0.5000 | 0.6952 | 0.0118 | 0.1842 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret38_cross_up_0` | one_head_filter_pi_star | 25 | 2.3545 | 1.2272 | 0.5200 | 0.4762 | 0.0100 | 0.2400 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret38_cross_down_0` | one_head_filter_pi_star | 27 | 2.2234 | 1.3932 | 0.5926 | 0.7098 | 0.0089 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret38_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.6044 | 0.6239 | 2.9282 | 0.0081 | 0.2706 | ok | RAN |
| SOLUSDT | 8 | `ret38_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.5192 | 0.6175 | 2.6138 | 0.0073 | 0.2627 | ok | RAN |
| ETHUSDT | 8 | `ret38_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2282 | 0.6047 | 1.1119 | 0.0071 | 0.2326 | ok | RAN |
| ETHUSDT | 4 | `ret38_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1947 | 0.5902 | 0.9725 | 0.0063 | 0.2295 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret38_cross_up_0` | one_head_filter_pi_star | 18 | 1.6674 | 0.7624 | 0.4444 | -0.4996 | -0.0060 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret38_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret38_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret38_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret38_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret38_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret38_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret38_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret38_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret38_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret38_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret38_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret38_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
