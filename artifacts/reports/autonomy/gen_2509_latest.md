# Autonomy public-indicator hunt gen 2509

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T020600Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret412_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.3478 | 0.6111 | 1.7031 | 0.0094 | 0.1790 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret412_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.1870 | 0.5938 | 0.9966 | 0.0057 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `ret412_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0397 | 0.5282 | 0.2028 | 0.0008 | 0.1197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret412_pos_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 0.9987 | 0.5223 | -0.0066 | -0.0000 | 0.1083 | ok | RAN |
| SOLUSDT | 8 | `ret412_neg_at_h` | one_head_filter_pi_star | 176 | 14.3179 | 0.9796 | 0.5739 | -0.1158 | -0.0004 | 0.1420 | ok | RAN |
| SOLUSDT | 4 | `ret412_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 0.9530 | 0.5682 | -0.2840 | -0.0010 | 0.1477 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret412_pos_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 0.8519 | 0.5329 | -0.8825 | -0.0063 | 0.1138 | ok | RAN |
| ETHUSDT | 8 | `ret412_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8375 | 0.5410 | -1.0010 | -0.0066 | 0.1093 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret412_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6099 | 0.3529 | -0.7735 | -0.0329 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret412_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0655 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret412_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret412_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret412_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret412_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
