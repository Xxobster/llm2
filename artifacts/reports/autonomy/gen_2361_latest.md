# Autonomy public-indicator hunt gen 2361

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T083152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5460_above_at_h` | one_head_filter_pi_star | 43 | 3.9869 | 1.7394 | 0.6047 | 1.4276 | 0.0105 | 0.1163 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5460_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.6160 | 0.6042 | 1.2606 | 0.0079 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema5460_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 0.9872 | 0.5597 | -0.1054 | -0.0004 | 0.1392 | ok | RAN |
| SOLUSDT | 8 | `ema5460_below_at_h` | one_head_filter_pi_star | 314 | 25.6761 | 0.9723 | 0.5350 | -0.2133 | -0.0006 | 0.1338 | ok | RAN |
| SOLUSDT | 4 | `ema5460_below_at_h` | one_head_filter_pi_star | 327 | 26.7391 | 0.9516 | 0.5321 | -0.3839 | -0.0010 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5460_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9430 | 0.5539 | -0.4771 | -0.0019 | 0.1341 | ok | RAN |
| ETHUSDT | 8 | `ema5460_above_at_h` | one_head_filter_pi_star | 48 | 5.6405 | 0.9055 | 0.5208 | -0.3586 | -0.0051 | 0.1875 | ok | RAN |
| ETHUSDT | 4 | `ema5460_above_at_h` | one_head_filter_pi_star | 42 | 7.1538 | 0.8184 | 0.5000 | -0.7440 | -0.0087 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5460_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5460_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
