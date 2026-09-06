# Autonomy public-indicator hunt gen 1924

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T013519Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1032_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1032_above_at_h` | one_head_filter_pi_star | 111 | 9.1238 | 1.4165 | 0.6306 | 1.5264 | 0.0067 | 0.1441 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1032_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.1465 | 0.5849 | 0.6130 | 0.0027 | 0.1226 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1032_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9854 | 0.5495 | -0.0988 | -0.0004 | 0.1532 | ok | RAN |
| SOLUSDT | 8 | `ema1032_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9630 | 0.5409 | -0.2562 | -0.0008 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ema1032_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 0.9805 | 0.5674 | -0.0977 | -0.0008 | 0.1277 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1032_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 0.9095 | 0.5315 | -0.6392 | -0.0020 | 0.1260 | ok | RAN |
| ETHUSDT | 8 | `ema1032_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9032 | 0.5339 | -0.6973 | -0.0032 | 0.1525 | ok | RAN |
| ETHUSDT | 8 | `ema1032_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.8574 | 0.5214 | -0.6790 | -0.0062 | 0.1197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1032_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1032_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1032_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1032_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1032_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
