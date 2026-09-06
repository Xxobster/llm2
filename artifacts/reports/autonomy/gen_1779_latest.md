# Autonomy public-indicator hunt gen 1779

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T122902Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma711_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1875 | 0.5833 | 1.0706 | 0.0056 | 0.1889 | ok | RAN |
| ETHUSDT | 4 | `sma711_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1958 | 0.5814 | 1.0861 | 0.0056 | 0.1919 | ok | RAN |
| SOLUSDT | 4 | `sma711_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.1023 | 0.5588 | 0.4889 | 0.0019 | 0.1176 | ok | RAN |
| SOLUSDT | 8 | `sma711_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0673 | 0.5469 | 0.3137 | 0.0012 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma711_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 0.9096 | 0.5437 | -0.5702 | -0.0019 | 0.1359 | ok | RAN |
| SOLUSDT | 8 | `sma711_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.8807 | 0.5544 | -0.7515 | -0.0027 | 0.1399 | ok | RAN |
| ETHUSDT | 8 | `sma711_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8720 | 0.5556 | -0.6687 | -0.0052 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma711_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.7907 | 0.5333 | -1.1890 | -0.0092 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma711_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma711_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma711_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma711_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma711_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma711_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
