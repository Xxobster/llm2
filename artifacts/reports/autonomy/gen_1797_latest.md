# Autonomy public-indicator hunt gen 1797

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T140823Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret300_neg_at_h` | one_head_filter_pi_star | 151 | 12.3353 | 1.2146 | 0.6093 | 1.0778 | 0.0064 | 0.2185 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret300_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1879 | 0.6056 | 1.1049 | 0.0055 | 0.1889 | ok | RAN |
| SOLUSDT | 8 | `ret300_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.1573 | 0.5706 | 0.7950 | 0.0029 | 0.1043 | ok | RAN |
| SOLUSDT | 8 | `ret300_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.0535 | 0.5800 | 0.3145 | 0.0011 | 0.1450 | ok | RAN |
| SOLUSDT | 4 | `ret300_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.0557 | 0.5345 | 0.3061 | 0.0010 | 0.1034 | ok | RAN |
| SOLUSDT | 4 | `ret300_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.0305 | 0.5636 | 0.1682 | 0.0006 | 0.1515 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret300_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.8515 | 0.5309 | -0.9225 | -0.0058 | 0.0928 | ok | RAN |
| ETHUSDT | 4 | `ret300_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 0.7361 | 0.5172 | -1.7174 | -0.0114 | 0.1034 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret300_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret300_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0705 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret300_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret300_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret300_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret300_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
