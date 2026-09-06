# Autonomy public-indicator hunt gen 2100

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T221612Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1055_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1055_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.2360 | 0.6132 | 0.9103 | 0.0039 | 0.1415 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1055_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.1008 | 0.5691 | 0.4429 | 0.0018 | 0.1382 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1055_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9576 | 0.5408 | -0.3012 | -0.0014 | 0.1459 | ok | RAN |
| SOLUSDT | 4 | `ema1055_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9328 | 0.5339 | -0.4714 | -0.0014 | 0.1235 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1055_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 0.9150 | 0.5277 | -0.6276 | -0.0019 | 0.1255 | ok | RAN |
| ETHUSDT | 8 | `ema1055_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9335 | 0.5432 | -0.4920 | -0.0022 | 0.1481 | ok | RAN |
| ETHUSDT | 4 | `ema1055_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.8632 | 0.5289 | -0.6556 | -0.0061 | 0.1074 | ok | RAN |
| ETHUSDT | 8 | `ema1055_above_at_h` | one_head_filter_pi_star | 113 | 9.3249 | 0.8421 | 0.5221 | -0.7285 | -0.0067 | 0.1239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1055_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1055_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1055_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1055_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1055_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
