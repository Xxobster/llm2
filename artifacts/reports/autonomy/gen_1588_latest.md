# Autonomy public-indicator hunt gen 1588

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T164511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema986_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.1040 | 0.5785 | 0.4743 | 0.0019 | 0.1405 | ok | RAN |
| SOLUSDT | 8 | `ema986_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.0549 | 0.5517 | 0.2464 | 0.0010 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema986_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9978 | 0.5444 | -0.0148 | -0.0000 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema986_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9619 | 0.5451 | -0.2681 | -0.0012 | 0.1545 | ok | RAN |
| SOLUSDT | 4 | `ema986_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9310 | 0.5331 | -0.4885 | -0.0015 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema986_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 0.9281 | 0.5419 | -0.5009 | -0.0023 | 0.1498 | ok | RAN |
| ETHUSDT | 4 | `ema986_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 0.9438 | 0.5672 | -0.2718 | -0.0025 | 0.1194 | ok | RAN |
| ETHUSDT | 8 | `ema986_above_at_h` | one_head_filter_pi_star | 113 | 9.3257 | 0.8894 | 0.5398 | -0.5314 | -0.0047 | 0.1239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema986_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema986_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema986_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema986_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema986_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema986_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
