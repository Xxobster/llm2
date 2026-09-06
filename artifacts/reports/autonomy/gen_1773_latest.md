# Autonomy public-indicator hunt gen 1773

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T115414Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret297_neg_at_h` | one_head_filter_pi_star | 150 | 12.2536 | 1.2964 | 0.6200 | 1.4786 | 0.0086 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret297_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1711 | 0.6024 | 1.0083 | 0.0053 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `ret297_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.1035 | 0.5575 | 0.5496 | 0.0020 | 0.1034 | ok | RAN |
| SOLUSDT | 8 | `ret297_pos_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.0857 | 0.5535 | 0.4392 | 0.0016 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret297_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 0.9978 | 0.5706 | -0.0126 | -0.0000 | 0.1412 | ok | RAN |
| SOLUSDT | 8 | `ret297_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9588 | 0.5434 | -0.2381 | -0.0009 | 0.1503 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret297_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8743 | 0.5380 | -0.7434 | -0.0047 | 0.1141 | ok | RAN |
| ETHUSDT | 4 | `ret297_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.8516 | 0.5402 | -0.9026 | -0.0058 | 0.1092 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret297_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret297_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0727 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret297_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret297_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret297_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret297_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
