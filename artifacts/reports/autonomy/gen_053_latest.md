# Autonomy public-indicator hunt gen 053

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T130228Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `tp_cross_down_0` | one_head_filter_pi_star | 13 | 1.0695 | 3.7507 | 0.7692 | 1.6160 | 0.0279 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tp_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `tp_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `tp_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `tp_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1837 | 0.6909 | 4.0500 | 0.0179 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `tp_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2178 | 0.5926 | 1.0049 | 0.0071 | 0.2037 | ok | RAN |
| ETHUSDT | 4 | `tp_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1890 | 0.5901 | 0.8787 | 0.0061 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `tp_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3788 | 0.5915 | 2.0475 | 0.0057 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `tp_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3841 | 0.5991 | 2.0751 | 0.0056 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tp_cross_down_0` | one_head_filter_pi_star | 13 | 1.6508 | 0.9671 | 0.6923 | -0.0563 | -0.0013 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 4 | `tp_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `tp_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `tp_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `tp_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `tp_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `tp_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `tp_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `tp_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `tp_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
