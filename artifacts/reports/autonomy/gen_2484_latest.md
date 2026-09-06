# Autonomy public-indicator hunt gen 2484

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T232726Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1106_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1106_above_at_h` | one_head_filter_pi_star | 101 | 8.3014 | 1.2661 | 0.6040 | 1.0474 | 0.0044 | 0.1386 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1106_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.2193 | 0.5983 | 0.8912 | 0.0038 | 0.1282 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1106_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9759 | 0.5498 | -0.1653 | -0.0007 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1106_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 0.9152 | 0.5311 | -0.6225 | -0.0019 | 0.1355 | ok | RAN |
| SOLUSDT | 8 | `ema1106_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 0.9030 | 0.5263 | -0.7159 | -0.0021 | 0.1278 | ok | RAN |
| ETHUSDT | 8 | `ema1106_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.8689 | 0.5316 | -0.9943 | -0.0043 | 0.1477 | ok | RAN |
| ETHUSDT | 4 | `ema1106_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.8608 | 0.5304 | -0.6310 | -0.0064 | 0.1130 | ok | RAN |
| ETHUSDT | 8 | `ema1106_above_at_h` | one_head_filter_pi_star | 110 | 9.0781 | 0.8316 | 0.5273 | -0.8063 | -0.0075 | 0.1182 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1106_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1106_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1106_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1106_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1106_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
