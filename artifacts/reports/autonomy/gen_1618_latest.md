# Autonomy public-indicator hunt gen 1618

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T194931Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1472_pos_at_h` | one_head_filter_pi_star | 15 | 1.4775 | 2.1114 | 0.7333 | 1.3346 | 0.0126 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1472_pos_at_h` | one_head_filter_pi_star | 22 | 1.9161 | 1.6942 | 0.6818 | 1.0451 | 0.0111 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1472_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.0136 | 0.5503 | 0.1064 | 0.0003 | 0.1272 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1472_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.0017 | 0.5471 | 0.0133 | 0.0000 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `ret1472_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 0.9553 | 0.5552 | -0.3606 | -0.0015 | 0.1411 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1472_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9388 | 0.5471 | -0.4902 | -0.0020 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `ret1472_pos_at_h` | one_head_filter_pi_star | 23 | 2.3092 | 0.8620 | 0.4783 | -0.3281 | -0.0065 | 0.2174 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1472_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4124 | 0.2353 | -1.3306 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1472_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3787 | 0.2222 | -1.5167 | -0.0867 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1472_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1472_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1472_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
