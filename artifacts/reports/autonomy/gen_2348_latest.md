# Autonomy public-indicator hunt gen 2348

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T065215Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1088_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0822 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1088_above_at_h` | one_head_filter_pi_star | 112 | 9.1846 | 1.1267 | 0.5893 | 0.5443 | 0.0023 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `ema1088_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.0874 | 0.5868 | 0.3943 | 0.0016 | 0.1405 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1088_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9845 | 0.5426 | -0.1069 | -0.0003 | 0.1357 | ok | RAN |
| SOLUSDT | 4 | `ema1088_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9822 | 0.5444 | -0.1234 | -0.0004 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1088_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9389 | 0.5467 | -0.4205 | -0.0019 | 0.1556 | ok | RAN |
| ETHUSDT | 4 | `ema1088_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9233 | 0.5371 | -0.5374 | -0.0024 | 0.1485 | ok | RAN |
| ETHUSDT | 4 | `ema1088_above_at_h` | one_head_filter_pi_star | 107 | 8.8305 | 0.9172 | 0.5514 | -0.3571 | -0.0035 | 0.1121 | ok | RAN |
| ETHUSDT | 8 | `ema1088_above_at_h` | one_head_filter_pi_star | 110 | 9.0781 | 0.8592 | 0.5364 | -0.6572 | -0.0063 | 0.1182 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1088_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1088_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1088_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1088_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1088_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
