# Autonomy public-indicator hunt gen 2009

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T101908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4580_above_at_h` | one_head_filter_pi_star | 66 | 5.4256 | 2.1750 | 0.6970 | 2.3974 | 0.0136 | 0.1061 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4580_above_at_h` | one_head_filter_pi_star | 63 | 5.1790 | 1.3316 | 0.6032 | 0.9205 | 0.0058 | 0.1270 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4580_below_at_h` | one_head_filter_pi_star | 298 | 24.3677 | 0.9802 | 0.5336 | -0.1486 | -0.0004 | 0.1409 | ok | RAN |
| ETHUSDT | 8 | `ema4580_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9710 | 0.5581 | -0.2371 | -0.0010 | 0.1366 | ok | RAN |
| SOLUSDT | 4 | `ema4580_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9482 | 0.5316 | -0.4031 | -0.0011 | 0.1297 | ok | RAN |
| ETHUSDT | 4 | `ema4580_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9563 | 0.5556 | -0.3680 | -0.0014 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema4580_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.9661 | 0.5312 | -0.1535 | -0.0015 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4580_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.8899 | 0.5143 | -0.5479 | -0.0055 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4580_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
