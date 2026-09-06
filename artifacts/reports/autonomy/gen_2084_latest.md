# Autonomy public-indicator hunt gen 2084

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T195748Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1053_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1053_above_at_h` | one_head_filter_pi_star | 104 | 8.4802 | 1.3441 | 0.6346 | 1.3025 | 0.0054 | 0.1442 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1053_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.1597 | 0.5897 | 0.6793 | 0.0029 | 0.1282 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1053_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9402 | 0.5405 | -0.4236 | -0.0013 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `ema1053_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9511 | 0.5459 | -0.3380 | -0.0015 | 0.1485 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1053_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9100 | 0.5299 | -0.6310 | -0.0020 | 0.1275 | ok | RAN |
| ETHUSDT | 8 | `ema1053_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 0.9310 | 0.5447 | -0.5151 | -0.0022 | 0.1423 | ok | RAN |
| ETHUSDT | 8 | `ema1053_above_at_h` | one_head_filter_pi_star | 119 | 9.7816 | 0.8935 | 0.5462 | -0.5158 | -0.0047 | 0.1261 | ok | RAN |
| ETHUSDT | 4 | `ema1053_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 0.8768 | 0.5505 | -0.5654 | -0.0055 | 0.1284 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1053_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1053_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1053_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1053_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1053_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
