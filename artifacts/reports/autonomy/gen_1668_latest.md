# Autonomy public-indicator hunt gen 1668

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T004711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema997_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema997_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.1040 | 0.5656 | 0.4680 | 0.0019 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `ema997_above_at_h` | one_head_filter_pi_star | 118 | 9.6992 | 1.0642 | 0.5678 | 0.2936 | 0.0012 | 0.1356 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema997_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 0.9920 | 0.5485 | -0.0529 | -0.0002 | 0.1266 | ok | RAN |
| SOLUSDT | 8 | `ema997_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9757 | 0.5441 | -0.1702 | -0.0005 | 0.1264 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema997_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9353 | 0.5394 | -0.4779 | -0.0021 | 0.1494 | ok | RAN |
| ETHUSDT | 4 | `ema997_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.9325 | 0.5620 | -0.3366 | -0.0029 | 0.1314 | ok | RAN |
| ETHUSDT | 8 | `ema997_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 0.9096 | 0.5374 | -0.6339 | -0.0029 | 0.1498 | ok | RAN |
| ETHUSDT | 8 | `ema997_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9272 | 0.5610 | -0.3415 | -0.0030 | 0.1220 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema997_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema997_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema997_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema997_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema997_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
