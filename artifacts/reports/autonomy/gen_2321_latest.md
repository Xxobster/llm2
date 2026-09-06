# Autonomy public-indicator hunt gen 2321

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T031223Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5360_above_at_h` | one_head_filter_pi_star | 74 | 6.2152 | 1.6504 | 0.6351 | 1.7189 | 0.0090 | 0.1081 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5360_above_at_h` | one_head_filter_pi_star | 41 | 3.8014 | 1.6164 | 0.6098 | 1.1716 | 0.0088 | 0.1463 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5360_below_at_h` | one_head_filter_pi_star | 320 | 26.1667 | 0.9701 | 0.5344 | -0.2349 | -0.0006 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `ema5360_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9579 | 0.5543 | -0.3437 | -0.0014 | 0.1378 | ok | RAN |
| SOLUSDT | 8 | `ema5360_below_at_h` | one_head_filter_pi_star | 314 | 25.6761 | 0.9260 | 0.5223 | -0.5821 | -0.0016 | 0.1338 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5360_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9306 | 0.5503 | -0.5757 | -0.0023 | 0.1361 | ok | RAN |
| ETHUSDT | 8 | `ema5360_above_at_h` | one_head_filter_pi_star | 42 | 12.2589 | 0.8219 | 0.5000 | -1.0205 | -0.0091 | 0.1667 | ok | RAN |
| ETHUSDT | 4 | `ema5360_above_at_h` | one_head_filter_pi_star | 41 | 6.9835 | 0.7227 | 0.4878 | -1.3141 | -0.0132 | 0.1220 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5360_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4556 | 0.2632 | -1.3433 | -0.0723 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
