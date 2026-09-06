# Autonomy public-indicator hunt gen 2317

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T024351Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret374_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.3190 | 0.6111 | 1.6120 | 0.0087 | 0.1914 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret374_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1215 | 0.5780 | 0.6963 | 0.0037 | 0.1734 | ok | RAN |
| SOLUSDT | 8 | `ret374_pos_at_h` | one_head_filter_pi_star | 156 | 12.7203 | 1.1177 | 0.5513 | 0.5936 | 0.0023 | 0.1090 | ok | RAN |
| SOLUSDT | 4 | `ret374_pos_at_h` | one_head_filter_pi_star | 156 | 12.7203 | 1.0518 | 0.5449 | 0.2718 | 0.0010 | 0.0962 | ok | RAN |
| SOLUSDT | 4 | `ret374_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.0237 | 0.5600 | 0.1425 | 0.0005 | 0.1500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret374_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9509 | 0.5746 | -0.3000 | -0.0010 | 0.1547 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret374_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8444 | 0.5532 | -0.9671 | -0.0065 | 0.1064 | ok | RAN |
| ETHUSDT | 4 | `ret374_pos_at_h` | one_head_filter_pi_star | 204 | 16.7685 | 0.8324 | 0.5441 | -1.0848 | -0.0070 | 0.1127 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret374_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4796 | 0.2222 | -1.1817 | -0.0510 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret374_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret374_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret374_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret374_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret374_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
