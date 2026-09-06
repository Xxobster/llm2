# Autonomy public-indicator hunt gen 1788

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T131931Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1014_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.2076 | 0.5968 | 0.8864 | 0.0036 | 0.1210 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1014_above_at_h` | one_head_filter_pi_star | 120 | 9.8636 | 1.1851 | 0.5833 | 0.7926 | 0.0034 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema1014_above_at_h` | one_head_filter_pi_star | 132 | 10.8928 | 1.0471 | 0.5758 | 0.2221 | 0.0019 | 0.1288 | ok | RAN |
| SOLUSDT | 8 | `ema1014_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.0119 | 0.5494 | 0.0766 | 0.0002 | 0.1202 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1014_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 0.9886 | 0.5551 | -0.0786 | -0.0004 | 0.1542 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1014_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9231 | 0.5397 | -0.5425 | -0.0017 | 0.1310 | ok | RAN |
| ETHUSDT | 8 | `ema1014_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9153 | 0.5372 | -0.6231 | -0.0028 | 0.1446 | ok | RAN |
| ETHUSDT | 8 | `ema1014_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.9319 | 0.5492 | -0.3181 | -0.0029 | 0.1393 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1014_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1014_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1014_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1014_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1014_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1014_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
