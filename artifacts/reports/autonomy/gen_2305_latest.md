# Autonomy public-indicator hunt gen 2305

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T011635Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5320_above_at_h` | one_head_filter_pi_star | 46 | 4.2650 | 1.9782 | 0.6522 | 1.7216 | 0.0112 | 0.1087 | ok | RAN |
| SOLUSDT | 4 | `ema5320_above_at_h` | one_head_filter_pi_star | 60 | 4.9323 | 1.6040 | 0.6333 | 1.4270 | 0.0093 | 0.1500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5320_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9500 | 0.5314 | -0.3900 | -0.0010 | 0.1352 | ok | RAN |
| SOLUSDT | 4 | `ema5320_below_at_h` | one_head_filter_pi_star | 314 | 25.6761 | 0.9480 | 0.5287 | -0.4090 | -0.0011 | 0.1306 | ok | RAN |
| ETHUSDT | 8 | `ema5320_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9584 | 0.5546 | -0.3390 | -0.0014 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5320_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9322 | 0.5523 | -0.5773 | -0.0023 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `ema5320_above_at_h` | one_head_filter_pi_star | 45 | 5.2879 | 0.9120 | 0.5333 | -0.3433 | -0.0038 | 0.1556 | ok | RAN |
| ETHUSDT | 8 | `ema5320_above_at_h` | one_head_filter_pi_star | 53 | 6.0414 | 0.8166 | 0.5094 | -0.7747 | -0.0103 | 0.1698 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5320_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5320_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
