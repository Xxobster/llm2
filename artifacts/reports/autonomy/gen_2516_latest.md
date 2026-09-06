# Autonomy public-indicator hunt gen 2516

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T024938Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1110_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1110_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.2111 | 0.5932 | 0.8687 | 0.0037 | 0.1356 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1110_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.0633 | 0.5603 | 0.2744 | 0.0012 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1110_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9791 | 0.5417 | -0.1444 | -0.0004 | 0.1326 | ok | RAN |
| ETHUSDT | 4 | `ema1110_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9590 | 0.5459 | -0.2812 | -0.0013 | 0.1441 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1110_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.9575 | 0.5463 | -0.1881 | -0.0018 | 0.1019 | ok | RAN |
| SOLUSDT | 8 | `ema1110_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9196 | 0.5310 | -0.5739 | -0.0018 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema1110_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9418 | 0.5413 | -0.4305 | -0.0019 | 0.1529 | ok | RAN |
| ETHUSDT | 8 | `ema1110_above_at_h` | one_head_filter_pi_star | 125 | 10.3152 | 0.9278 | 0.5440 | -0.3312 | -0.0031 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1110_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0313 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1110_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
