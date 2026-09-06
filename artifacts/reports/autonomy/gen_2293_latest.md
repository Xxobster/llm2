# Autonomy public-indicator hunt gen 2293

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T235139Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret371_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2623 | 0.6036 | 1.3584 | 0.0076 | 0.1834 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret371_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1838 | 0.5870 | 1.0537 | 0.0054 | 0.1793 | ok | RAN |
| SOLUSDT | 8 | `ret371_pos_at_h` | one_head_filter_pi_star | 153 | 12.4757 | 1.1509 | 0.5490 | 0.7353 | 0.0030 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `ret371_pos_at_h` | one_head_filter_pi_star | 149 | 12.1495 | 1.0217 | 0.5369 | 0.1101 | 0.0004 | 0.1208 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret371_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9563 | 0.5753 | -0.2652 | -0.0009 | 0.1505 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret371_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9100 | 0.5491 | -0.5530 | -0.0020 | 0.1445 | ok | RAN |
| ETHUSDT | 4 | `ret371_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.7873 | 0.5135 | -1.3626 | -0.0096 | 0.1027 | ok | RAN |
| ETHUSDT | 8 | `ret371_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7789 | 0.5309 | -1.3865 | -0.0099 | 0.0979 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret371_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0601 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret371_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret371_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret371_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret371_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret371_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
