# Autonomy public-indicator hunt gen 020

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T091751Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `adosc_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.9370 | 0.6944 | 4.2904 | 0.0228 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 8 | `adosc_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9115 | 0.6755 | 3.7182 | 0.0218 | 0.3617 | EBR>35% | RAN |
| SOLUSDT | 4 | `adosc_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.3658 | 0.7048 | 4.4455 | 0.0195 | 0.4217 | EBR>35% | RAN |
| SOLUSDT | 8 | `adosc_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1075 | 0.6760 | 4.1267 | 0.0158 | 0.3799 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `adosc_cross_down_0` | one_head_filter_pi_star | 17 | 1.5060 | 1.4827 | 0.5882 | 0.6831 | 0.0140 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adosc_cross_up_0` | one_head_filter_pi_star | 80 | 6.6392 | 1.4091 | 0.6125 | 1.3717 | 0.0109 | 0.3250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `adosc_cross_down_0` | one_head_filter_pi_star | 68 | 5.8334 | 1.5854 | 0.6176 | 1.6087 | 0.0088 | 0.1912 | ok | RAN |
| SOLUSDT | 8 | `adosc_cross_up_0` | one_head_filter_pi_star | 43 | 3.5546 | 1.5742 | 0.6279 | 1.3155 | 0.0085 | 0.2791 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adosc_pos_at_h` | one_head_filter_pi_star | 159 | 13.0267 | 1.2268 | 0.5849 | 1.0185 | 0.0076 | 0.2013 | ok | RAN |
| ETHUSDT | 8 | `adosc_pos_at_h` | one_head_filter_pi_star | 168 | 13.7641 | 1.1891 | 0.5893 | 0.9073 | 0.0071 | 0.2024 | ok | RAN |
| SOLUSDT | 8 | `adosc_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.3746 | 0.6045 | 1.8546 | 0.0068 | 0.2486 | ok | RAN |
| SOLUSDT | 4 | `adosc_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3464 | 0.5907 | 1.8995 | 0.0053 | 0.2326 | ok | RAN |
| ETHUSDT | 8 | `adosc_cross_down_0` | one_head_filter_pi_star | 67 | 5.5211 | 1.1028 | 0.5522 | 0.3271 | 0.0032 | 0.1642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adosc_cross_up_0` | one_head_filter_pi_star | 16 | 1.4067 | 0.6843 | 0.5000 | -0.6943 | -0.0119 | 0.1250 | TPM<MIN | RAN |
| BTCUSDT | 8 | `adosc_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.8666 | 0.3889 | -0.2464 | -0.0141 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 4 | `adosc_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7040 | 0.3500 | -0.6085 | -0.0297 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `adosc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `adosc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `adosc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `adosc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `adosc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adosc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `adosc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adosc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
