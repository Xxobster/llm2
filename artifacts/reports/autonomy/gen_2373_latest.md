# Autonomy public-indicator hunt gen 2373

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T102144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret382_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1516 | 0.5906 | 0.8475 | 0.0044 | 0.1754 | ok | RAN |
| ETHUSDT | 4 | `ret382_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.1237 | 0.5948 | 0.6584 | 0.0038 | 0.2026 | ok | RAN |
| SOLUSDT | 8 | `ret382_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.1265 | 0.5497 | 0.6373 | 0.0024 | 0.0795 | ok | RAN |
| SOLUSDT | 4 | `ret382_pos_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.0987 | 0.5580 | 0.4746 | 0.0018 | 0.0942 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret382_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9696 | 0.5642 | -0.1827 | -0.0006 | 0.1453 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret382_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 0.8827 | 0.5351 | -0.7500 | -0.0026 | 0.1568 | ok | RAN |
| ETHUSDT | 4 | `ret382_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.9265 | 0.5657 | -0.4154 | -0.0030 | 0.1029 | ok | RAN |
| ETHUSDT | 8 | `ret382_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 0.8767 | 0.5446 | -0.7851 | -0.0052 | 0.1139 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret382_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0713 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret382_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0720 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret382_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret382_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret382_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret382_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
