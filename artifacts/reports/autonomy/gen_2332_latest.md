# Autonomy public-indicator hunt gen 2332

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T043107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1086_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1086_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.3095 | 0.5982 | 1.2110 | 0.0052 | 0.1339 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1086_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.0212 | 0.5546 | 0.1462 | 0.0007 | 0.1555 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1086_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 0.9910 | 0.5526 | -0.0418 | -0.0002 | 0.1316 | ok | RAN |
| SOLUSDT | 4 | `ema1086_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9507 | 0.5378 | -0.3449 | -0.0011 | 0.1275 | ok | RAN |
| SOLUSDT | 8 | `ema1086_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9432 | 0.5364 | -0.4041 | -0.0012 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1086_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9285 | 0.5427 | -0.5090 | -0.0023 | 0.1496 | ok | RAN |
| ETHUSDT | 4 | `ema1086_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 0.9126 | 0.5600 | -0.4186 | -0.0038 | 0.1120 | ok | RAN |
| ETHUSDT | 8 | `ema1086_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.8791 | 0.5259 | -0.5535 | -0.0053 | 0.1207 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1086_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1086_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1086_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1086_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1086_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
