# Autonomy public-indicator hunt gen 1837

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T174624Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret306_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2571 | 0.6048 | 1.3493 | 0.0073 | 0.1916 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret306_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2108 | 0.6000 | 1.1701 | 0.0061 | 0.1778 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret306_pos_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.2048 | 0.5600 | 0.9703 | 0.0038 | 0.1067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret306_pos_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1487 | 0.5636 | 0.7632 | 0.0028 | 0.1212 | ok | RAN |
| SOLUSDT | 8 | `ret306_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0492 | 0.5739 | 0.2780 | 0.0010 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `ret306_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 1.0339 | 0.5769 | 0.1860 | 0.0007 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret306_pos_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.8938 | 0.5490 | -0.5924 | -0.0042 | 0.0980 | ok | RAN |
| ETHUSDT | 4 | `ret306_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8866 | 0.5500 | -0.6799 | -0.0045 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret306_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret306_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret306_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret306_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret306_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret306_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
