# Autonomy public-indicator hunt gen 1636

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T212916Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema992_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema992_above_at_h` | one_head_filter_pi_star | 123 | 10.1096 | 1.1933 | 0.6016 | 0.8215 | 0.0035 | 0.1382 | ok | RAN |
| SOLUSDT | 8 | `ema992_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.0984 | 0.5484 | 0.4477 | 0.0018 | 0.1290 | ok | RAN |
| SOLUSDT | 8 | `ema992_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.0144 | 0.5451 | 0.0985 | 0.0003 | 0.1255 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema992_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9974 | 0.5511 | -0.0174 | -0.0001 | 0.1556 | ok | RAN |
| ETHUSDT | 8 | `ema992_above_at_h` | one_head_filter_pi_star | 121 | 9.9851 | 0.9938 | 0.5702 | -0.0283 | -0.0002 | 0.1240 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema992_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 0.9214 | 0.5344 | -0.5396 | -0.0017 | 0.1255 | ok | RAN |
| ETHUSDT | 8 | `ema992_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9379 | 0.5439 | -0.4423 | -0.0020 | 0.1535 | ok | RAN |
| ETHUSDT | 4 | `ema992_above_at_h` | one_head_filter_pi_star | 119 | 9.8209 | 0.8963 | 0.5546 | -0.4982 | -0.0046 | 0.1261 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema992_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema992_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema992_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema992_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema992_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
