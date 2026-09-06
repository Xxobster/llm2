# Autonomy public-indicator hunt gen 2147

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T043038Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma759_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2469 | 0.6023 | 1.3797 | 0.0065 | 0.1871 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma759_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.0911 | 0.5714 | 0.5535 | 0.0027 | 0.1813 | ok | RAN |
| SOLUSDT | 4 | `sma759_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.0653 | 0.5484 | 0.3046 | 0.0012 | 0.1129 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma759_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0033 | 0.5349 | 0.0164 | 0.0001 | 0.1318 | ok | RAN |
| SOLUSDT | 4 | `sma759_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9537 | 0.5588 | -0.2875 | -0.0010 | 0.1373 | ok | RAN |
| SOLUSDT | 8 | `sma759_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 0.9311 | 0.5493 | -0.4399 | -0.0015 | 0.1268 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma759_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.8656 | 0.5500 | -0.7204 | -0.0055 | 0.1125 | ok | RAN |
| ETHUSDT | 4 | `sma759_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.7945 | 0.5411 | -1.0853 | -0.0088 | 0.1096 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma759_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma759_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0658 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma759_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma759_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma759_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma759_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
