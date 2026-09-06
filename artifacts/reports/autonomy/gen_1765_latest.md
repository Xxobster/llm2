# Autonomy public-indicator hunt gen 1765

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T110926Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret295_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.3193 | 0.6188 | 1.6476 | 0.0092 | 0.1875 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret295_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.2461 | 0.6149 | 1.2800 | 0.0072 | 0.1988 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret295_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.0720 | 0.5476 | 0.3825 | 0.0014 | 0.1131 | ok | RAN |
| SOLUSDT | 4 | `ret295_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 1.0555 | 0.5767 | 0.3008 | 0.0012 | 0.1472 | ok | RAN |
| SOLUSDT | 4 | `ret295_pos_at_h` | one_head_filter_pi_star | 183 | 15.0069 | 1.0325 | 0.5464 | 0.1855 | 0.0006 | 0.1093 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret295_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 1.0037 | 0.5500 | 0.0204 | 0.0001 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret295_pos_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 0.8907 | 0.5427 | -0.6322 | -0.0042 | 0.1037 | ok | RAN |
| ETHUSDT | 4 | `ret295_pos_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 0.8827 | 0.5503 | -0.6480 | -0.0048 | 0.1007 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret295_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret295_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret295_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret295_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret295_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret295_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
