# Autonomy public-indicator hunt gen 1756

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T102037Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1010_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 1.2275 | 0.5965 | 0.9244 | 0.0038 | 0.1491 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1010_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.1368 | 0.5913 | 0.5800 | 0.0024 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1010_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9963 | 0.5455 | -0.0255 | -0.0001 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema1010_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 0.9859 | 0.5600 | -0.0661 | -0.0006 | 0.1360 | ok | RAN |
| SOLUSDT | 4 | `ema1010_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9702 | 0.5451 | -0.2056 | -0.0006 | 0.1255 | ok | RAN |
| ETHUSDT | 4 | `ema1010_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9544 | 0.5381 | -0.3127 | -0.0014 | 0.1570 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1010_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9295 | 0.5398 | -0.4942 | -0.0023 | 0.1593 | ok | RAN |
| ETHUSDT | 8 | `ema1010_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.8584 | 0.5478 | -0.6833 | -0.0062 | 0.1217 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1010_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1010_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1010_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1010_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1010_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1010_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
