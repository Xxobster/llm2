# Autonomy public-indicator hunt gen 2059

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T163217Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma748_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2063 | 0.5838 | 1.1394 | 0.0059 | 0.1850 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma748_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.0789 | 0.5765 | 0.4520 | 0.0024 | 0.2059 | ok | RAN |
| SOLUSDT | 8 | `sma748_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.0772 | 0.5448 | 0.3847 | 0.0015 | 0.1241 | ok | RAN |
| SOLUSDT | 4 | `sma748_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.0326 | 0.5379 | 0.1688 | 0.0006 | 0.1241 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma748_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9526 | 0.5672 | -0.2935 | -0.0010 | 0.1294 | ok | RAN |
| SOLUSDT | 8 | `sma748_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 0.9429 | 0.5556 | -0.3598 | -0.0012 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma748_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8864 | 0.5533 | -0.6130 | -0.0046 | 0.1133 | ok | RAN |
| ETHUSDT | 4 | `sma748_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 0.8617 | 0.5594 | -0.7141 | -0.0056 | 0.1049 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma748_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma748_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma748_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma748_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma748_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma748_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
