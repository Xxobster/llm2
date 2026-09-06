# Autonomy public-indicator hunt gen 1701

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T050004Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret286_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1871 | 0.6140 | 1.0786 | 0.0057 | 0.1988 | ok | RAN |
| ETHUSDT | 8 | `ret286_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.1019 | 0.5875 | 0.6092 | 0.0033 | 0.2125 | ok | RAN |
| SOLUSDT | 4 | `ret286_pos_at_h` | one_head_filter_pi_star | 185 | 15.1709 | 1.1067 | 0.5514 | 0.5706 | 0.0019 | 0.1081 | ok | RAN |
| SOLUSDT | 8 | `ret286_pos_at_h` | one_head_filter_pi_star | 182 | 14.9249 | 1.0863 | 0.5659 | 0.4615 | 0.0015 | 0.1099 | ok | RAN |
| SOLUSDT | 4 | `ret286_neg_at_h` | one_head_filter_pi_star | 132 | 10.7938 | 1.0271 | 0.5682 | 0.1385 | 0.0006 | 0.1591 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret286_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 0.9084 | 0.5370 | -0.5247 | -0.0021 | 0.1543 | ok | RAN |
| ETHUSDT | 4 | `ret286_pos_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8694 | 0.5355 | -0.7529 | -0.0052 | 0.1032 | ok | RAN |
| ETHUSDT | 8 | `ret286_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8101 | 0.5346 | -1.1424 | -0.0077 | 0.0881 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret286_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret286_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0740 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret286_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret286_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret286_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret286_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
