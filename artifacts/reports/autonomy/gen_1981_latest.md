# Autonomy public-indicator hunt gen 1981

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T065808Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret326_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 1.2447 | 0.5839 | 1.2072 | 0.0073 | 0.2148 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret326_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.1996 | 0.6025 | 1.1109 | 0.0062 | 0.2050 | ok | RAN |
| SOLUSDT | 4 | `ret326_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.1657 | 0.5464 | 0.8698 | 0.0029 | 0.1093 | ok | RAN |
| SOLUSDT | 8 | `ret326_pos_at_h` | one_head_filter_pi_star | 189 | 15.4989 | 1.1423 | 0.5661 | 0.7873 | 0.0026 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `ret326_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.0766 | 0.5801 | 0.4392 | 0.0015 | 0.1547 | ok | RAN |
| SOLUSDT | 8 | `ret326_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0115 | 0.5581 | 0.0673 | 0.0002 | 0.1512 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret326_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7891 | 0.5376 | -1.3297 | -0.0085 | 0.0914 | ok | RAN |
| ETHUSDT | 8 | `ret326_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.7814 | 0.5291 | -1.3291 | -0.0095 | 0.0988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret326_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret326_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret326_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret326_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret326_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret326_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
