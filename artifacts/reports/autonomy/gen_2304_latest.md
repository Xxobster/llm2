# Autonomy public-indicator hunt gen 2304

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T010857Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5360_above_at_h` | one_head_filter_pi_star | 46 | 4.3190 | 2.2555 | 0.6304 | 2.1424 | 0.0164 | 0.1087 | ok | RAN |
| SOLUSDT | 4 | `sma5360_above_at_h` | one_head_filter_pi_star | 65 | 5.5349 | 2.0275 | 0.6308 | 2.1507 | 0.0144 | 0.1077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5360_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 0.9864 | 0.5380 | -0.1037 | -0.0003 | 0.1297 | ok | RAN |
| ETHUSDT | 4 | `sma5360_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9885 | 0.5599 | -0.0919 | -0.0004 | 0.1287 | ok | RAN |
| SOLUSDT | 4 | `sma5360_below_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 0.9789 | 0.5344 | -0.1636 | -0.0004 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `sma5360_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9854 | 0.5585 | -0.1195 | -0.0005 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5360_above_at_h` | one_head_filter_pi_star | 28 | 8.4494 | 0.8150 | 0.4643 | -0.8742 | -0.0091 | 0.1786 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5360_above_at_h` | one_head_filter_pi_star | 41 | 11.9670 | 0.6491 | 0.4634 | -2.3084 | -0.0214 | 0.1707 | ok | RAN |
| ETHUSDT | 4 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5360_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
