# Autonomy public-indicator hunt gen 2252

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T185353Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1075_above_at_h` | one_head_filter_pi_star | 107 | 8.7248 | 1.2574 | 0.5888 | 1.0151 | 0.0042 | 0.1308 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1075_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.1531 | 0.5656 | 0.6656 | 0.0027 | 0.1230 | ok | RAN |
| ETHUSDT | 8 | `ema1075_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.0043 | 0.5642 | 0.0285 | 0.0001 | 0.1560 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1075_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 0.9648 | 0.5481 | -0.2353 | -0.0007 | 0.1255 | ok | RAN |
| ETHUSDT | 4 | `ema1075_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9488 | 0.5467 | -0.3539 | -0.0016 | 0.1556 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1075_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.9578 | 0.5463 | -0.1916 | -0.0018 | 0.1296 | ok | RAN |
| SOLUSDT | 4 | `ema1075_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 0.9006 | 0.5316 | -0.7324 | -0.0022 | 0.1338 | ok | RAN |
| ETHUSDT | 4 | `ema1075_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.8796 | 0.5366 | -0.5883 | -0.0054 | 0.1301 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1075_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1075_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1075_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1075_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1075_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1075_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
