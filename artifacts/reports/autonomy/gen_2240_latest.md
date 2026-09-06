# Autonomy public-indicator hunt gen 2240

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T172932Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5200_above_at_h` | one_head_filter_pi_star | 55 | 4.6834 | 2.8939 | 0.6909 | 2.8549 | 0.0198 | 0.1091 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5200_above_at_h` | one_head_filter_pi_star | 46 | 4.3190 | 2.1360 | 0.6304 | 1.9557 | 0.0154 | 0.0870 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5200_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 0.9852 | 0.5405 | -0.1109 | -0.0003 | 0.1262 | ok | RAN |
| SOLUSDT | 4 | `sma5200_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9598 | 0.5369 | -0.3225 | -0.0008 | 0.1268 | ok | RAN |
| ETHUSDT | 8 | `sma5200_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9601 | 0.5539 | -0.3204 | -0.0013 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `sma5200_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9514 | 0.5543 | -0.4046 | -0.0016 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5200_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.9129 | 0.5312 | -0.4028 | -0.0041 | 0.1562 | ok | RAN |
| ETHUSDT | 8 | `sma5200_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.8977 | 0.5161 | -0.4750 | -0.0047 | 0.1290 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5200_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5200_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
