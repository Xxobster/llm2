# Autonomy public-indicator hunt gen 2372

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T101326Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1091_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.1966 | 0.5841 | 0.8370 | 0.0034 | 0.1504 | ok | RAN |
| SOLUSDT | 8 | `ema1091_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.1564 | 0.5804 | 0.6567 | 0.0028 | 0.1339 | ok | RAN |
| ETHUSDT | 4 | `ema1091_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.0131 | 0.5502 | 0.0884 | 0.0004 | 0.1572 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1091_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 0.9373 | 0.5368 | -0.4560 | -0.0014 | 0.1324 | ok | RAN |
| SOLUSDT | 8 | `ema1091_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 0.9315 | 0.5333 | -0.4941 | -0.0015 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1091_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9357 | 0.5575 | -0.4514 | -0.0020 | 0.1549 | ok | RAN |
| ETHUSDT | 4 | `ema1091_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 0.9206 | 0.5522 | -0.3882 | -0.0035 | 0.1119 | ok | RAN |
| ETHUSDT | 8 | `ema1091_above_at_h` | one_head_filter_pi_star | 107 | 8.8305 | 0.8744 | 0.5234 | -0.5743 | -0.0055 | 0.1121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1091_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1091_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1091_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1091_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1091_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1091_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
