# Autonomy public-indicator hunt gen 1572

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T145906Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema983_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.1292 | 0.5690 | 0.5550 | 0.0023 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `ema983_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.0787 | 0.5469 | 0.3600 | 0.0014 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema983_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.0416 | 0.5648 | 0.2676 | 0.0012 | 0.1574 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema983_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 0.9755 | 0.5422 | -0.1572 | -0.0005 | 0.1244 | ok | RAN |
| SOLUSDT | 4 | `ema983_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9441 | 0.5437 | -0.3913 | -0.0012 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema983_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9263 | 0.5309 | -0.5407 | -0.0024 | 0.1440 | ok | RAN |
| ETHUSDT | 8 | `ema983_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 0.9383 | 0.5515 | -0.3112 | -0.0027 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema983_above_at_h` | one_head_filter_pi_star | 122 | 10.0676 | 0.8690 | 0.5410 | -0.6222 | -0.0057 | 0.1230 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema983_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema983_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema983_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema983_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema983_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema983_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
