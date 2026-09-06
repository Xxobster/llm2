# Autonomy public-indicator hunt gen 039

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T120500Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `fish_cross_down_0` | one_head_filter_pi_star | 22 | 1.8809 | 2.2715 | 0.5909 | 1.5775 | 0.0276 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 8 | `fish_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8664 | 0.6892 | 4.0679 | 0.0220 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `fish_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `fish_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.2512 | 0.6894 | 4.1774 | 0.0188 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 8 | `fish_cross_up_0` | one_head_filter_pi_star | 27 | 2.2880 | 1.5532 | 0.6667 | 0.9373 | 0.0185 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 4 | `fish_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1837 | 0.6909 | 4.0500 | 0.0179 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `fish_cross_down_0` | one_head_filter_pi_star | 24 | 2.0518 | 1.8397 | 0.5833 | 1.2422 | 0.0163 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `fish_cross_down_0` | one_head_filter_pi_star | 34 | 2.9092 | 1.3380 | 0.6471 | 0.7817 | 0.0153 | 0.3529 | EBR>35% | RAN |
| ETHUSDT | 4 | `fish_cross_up_0` | one_head_filter_pi_star | 23 | 2.4043 | 1.3273 | 0.6522 | 0.6226 | 0.0133 | 0.2174 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `fish_cross_down_0` | one_head_filter_pi_star | 37 | 3.1659 | 1.1830 | 0.6216 | 0.4650 | 0.0090 | 0.3243 | TPM<MIN | RAN |
| ETHUSDT | 8 | `fish_pos_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.2106 | 0.5933 | 0.9196 | 0.0074 | 0.1933 | ok | RAN |
| ETHUSDT | 4 | `fish_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `fish_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3843 | 0.5991 | 2.0777 | 0.0056 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `fish_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3611 | 0.5953 | 1.9506 | 0.0054 | 0.2419 | ok | RAN |
| SOLUSDT | 4 | `fish_cross_up_0` | one_head_filter_pi_star | 26 | 2.2661 | 1.2940 | 0.6154 | 0.5688 | 0.0046 | 0.2308 | TPM<MIN | RAN |
| SOLUSDT | 8 | `fish_cross_up_0` | one_head_filter_pi_star | 28 | 2.4404 | 1.1295 | 0.6071 | 0.2773 | 0.0022 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `fish_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `fish_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `fish_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `fish_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `fish_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `fish_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `fish_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `fish_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
