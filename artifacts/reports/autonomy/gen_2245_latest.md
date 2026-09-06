# Autonomy public-indicator hunt gen 2245

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T180512Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret364_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2568 | 0.6045 | 1.3959 | 0.0077 | 0.2034 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret364_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2524 | 0.5854 | 1.3270 | 0.0072 | 0.1829 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret364_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.1852 | 0.5750 | 0.9169 | 0.0034 | 0.1062 | ok | RAN |
| SOLUSDT | 4 | `ret364_pos_at_h` | one_head_filter_pi_star | 151 | 12.3126 | 1.1028 | 0.5563 | 0.5079 | 0.0020 | 0.1192 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret364_neg_at_h` | one_head_filter_pi_star | 192 | 15.9727 | 0.8893 | 0.5469 | -0.7100 | -0.0024 | 0.1458 | ok | RAN |
| SOLUSDT | 4 | `ret364_neg_at_h` | one_head_filter_pi_star | 178 | 14.6516 | 0.8789 | 0.5506 | -0.7470 | -0.0026 | 0.1461 | ok | RAN |
| ETHUSDT | 8 | `ret364_pos_at_h` | one_head_filter_pi_star | 182 | 14.9111 | 0.8253 | 0.5549 | -1.0264 | -0.0075 | 0.0989 | ok | RAN |
| ETHUSDT | 4 | `ret364_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 0.7766 | 0.5333 | -1.4101 | -0.0096 | 0.1026 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret364_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5580 | 0.2353 | -0.9085 | -0.0380 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret364_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret364_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret364_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret364_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret364_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
