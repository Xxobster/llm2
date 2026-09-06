# Autonomy public-indicator hunt gen 2228

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T160317Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1072_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1072_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.2404 | 0.5983 | 0.9750 | 0.0041 | 0.1282 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1072_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.1493 | 0.5950 | 0.6499 | 0.0027 | 0.1157 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1072_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9688 | 0.5436 | -0.2204 | -0.0010 | 0.1494 | ok | RAN |
| SOLUSDT | 4 | `ema1072_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9446 | 0.5382 | -0.3903 | -0.0012 | 0.1374 | ok | RAN |
| SOLUSDT | 8 | `ema1072_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9334 | 0.5364 | -0.4774 | -0.0015 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1072_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.8975 | 0.5420 | -0.7609 | -0.0034 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `ema1072_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.9038 | 0.5455 | -0.4620 | -0.0043 | 0.1074 | ok | RAN |
| ETHUSDT | 8 | `ema1072_above_at_h` | one_head_filter_pi_star | 117 | 9.6172 | 0.8932 | 0.5299 | -0.4857 | -0.0046 | 0.1197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1072_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1072_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0592 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1072_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1072_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1072_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
