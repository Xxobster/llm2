# Autonomy public-indicator hunt gen 1789

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T132502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret299_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.3870 | 0.6319 | 1.9285 | 0.0108 | 0.1902 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret299_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.1231 | 0.5849 | 0.7057 | 0.0038 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `ret299_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.1139 | 0.5787 | 0.6084 | 0.0023 | 0.1404 | ok | RAN |
| SOLUSDT | 4 | `ret299_pos_at_h` | one_head_filter_pi_star | 174 | 14.2689 | 1.0949 | 0.5575 | 0.5108 | 0.0017 | 0.1034 | ok | RAN |
| SOLUSDT | 8 | `ret299_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.0220 | 0.5380 | 0.1178 | 0.0004 | 0.1139 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret299_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 0.9931 | 0.5497 | -0.0374 | -0.0001 | 0.1589 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret299_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 0.7990 | 0.5281 | -1.2463 | -0.0080 | 0.1011 | ok | RAN |
| ETHUSDT | 8 | `ret299_pos_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 0.7894 | 0.5200 | -1.3063 | -0.0085 | 0.1150 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret299_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0664 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret299_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0727 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret299_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret299_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret299_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret299_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
