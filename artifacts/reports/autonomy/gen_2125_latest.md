# Autonomy public-indicator hunt gen 2125

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T011942Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret347_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.2881 | 0.6180 | 1.5838 | 0.0084 | 0.1910 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret347_pos_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.3492 | 0.6014 | 1.5011 | 0.0060 | 0.1189 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret347_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1915 | 0.5868 | 1.0372 | 0.0058 | 0.1916 | ok | RAN |
| SOLUSDT | 4 | `ret347_pos_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.1135 | 0.5521 | 0.5839 | 0.0021 | 0.1104 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret347_neg_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 0.9218 | 0.5446 | -0.5042 | -0.0017 | 0.1408 | ok | RAN |
| SOLUSDT | 8 | `ret347_neg_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 0.8874 | 0.5507 | -0.7343 | -0.0024 | 0.1401 | ok | RAN |
| ETHUSDT | 4 | `ret347_pos_at_h` | one_head_filter_pi_star | 189 | 15.4846 | 0.8535 | 0.5503 | -0.8877 | -0.0059 | 0.0847 | ok | RAN |
| ETHUSDT | 8 | `ret347_pos_at_h` | one_head_filter_pi_star | 185 | 15.1569 | 0.8206 | 0.5459 | -1.1229 | -0.0077 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret347_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0744 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret347_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0744 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret347_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret347_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret347_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret347_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
