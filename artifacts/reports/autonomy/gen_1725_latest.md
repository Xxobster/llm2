# Autonomy public-indicator hunt gen 1725

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T072825Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret290_neg_at_h` | one_head_filter_pi_star | 142 | 11.6001 | 1.2454 | 0.6197 | 1.2831 | 0.0074 | 0.2254 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret290_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2127 | 0.6136 | 1.1804 | 0.0066 | 0.1761 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret290_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0688 | 0.5464 | 0.3701 | 0.0012 | 0.1148 | ok | RAN |
| SOLUSDT | 4 | `ret290_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.0530 | 0.5491 | 0.2860 | 0.0010 | 0.1098 | ok | RAN |
| SOLUSDT | 4 | `ret290_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 1.0084 | 0.5658 | 0.0461 | 0.0002 | 0.1579 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret290_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9777 | 0.5491 | -0.1279 | -0.0005 | 0.1561 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret290_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.9027 | 0.5576 | -0.5583 | -0.0037 | 0.1030 | ok | RAN |
| ETHUSDT | 8 | `ret290_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8379 | 0.5376 | -0.9945 | -0.0066 | 0.1129 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret290_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret290_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0732 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret290_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret290_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret290_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret290_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
