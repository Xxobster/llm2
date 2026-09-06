# Autonomy public-indicator hunt gen 1741

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T085942Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret292_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1859 | 0.6082 | 1.0568 | 0.0057 | 0.1871 | ok | RAN |
| ETHUSDT | 8 | `ret292_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1539 | 0.5882 | 0.8956 | 0.0049 | 0.1882 | ok | RAN |
| SOLUSDT | 4 | `ret292_pos_at_h` | one_head_filter_pi_star | 160 | 13.1208 | 1.1142 | 0.5625 | 0.5792 | 0.0021 | 0.1125 | ok | RAN |
| SOLUSDT | 8 | `ret292_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0439 | 0.5484 | 0.2403 | 0.0008 | 0.1129 | ok | RAN |
| SOLUSDT | 4 | `ret292_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 1.0342 | 0.5695 | 0.1812 | 0.0007 | 0.1523 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret292_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9309 | 0.5519 | -0.4196 | -0.0015 | 0.1475 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret292_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8473 | 0.5430 | -0.9182 | -0.0062 | 0.1075 | ok | RAN |
| ETHUSDT | 4 | `ret292_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8302 | 0.5435 | -1.0143 | -0.0067 | 0.1033 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret292_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret292_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret292_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret292_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret292_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret292_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
