# Autonomy public-indicator hunt gen 1620

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T200006Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema990_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema990_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.1289 | 0.5714 | 0.5808 | 0.0023 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `ema990_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.1193 | 0.5913 | 0.5105 | 0.0021 | 0.1478 | ok | RAN |
| ETHUSDT | 4 | `ema990_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.0115 | 0.5574 | 0.0790 | 0.0004 | 0.1489 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema990_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 0.9847 | 0.5481 | -0.1000 | -0.0003 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `ema990_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.9678 | 0.5422 | -0.2180 | -0.0007 | 0.1285 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema990_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 0.9539 | 0.5635 | -0.2191 | -0.0019 | 0.1190 | ok | RAN |
| ETHUSDT | 8 | `ema990_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9060 | 0.5342 | -0.6960 | -0.0031 | 0.1496 | ok | RAN |
| ETHUSDT | 8 | `ema990_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.8613 | 0.5492 | -0.6803 | -0.0058 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema990_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema990_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema990_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema990_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema990_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
