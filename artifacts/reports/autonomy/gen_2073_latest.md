# Autonomy public-indicator hunt gen 2073

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T183141Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4740_above_at_h` | one_head_filter_pi_star | 36 | 3.3801 | 3.0273 | 0.7222 | 2.3457 | 0.0194 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4740_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 1.4139 | 0.6129 | 1.0630 | 0.0063 | 0.1290 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4740_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9939 | 0.5408 | -0.0470 | -0.0001 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `ema4740_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9766 | 0.5575 | -0.1854 | -0.0008 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `ema4740_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9670 | 0.5572 | -0.2662 | -0.0011 | 0.1378 | ok | RAN |
| SOLUSDT | 4 | `ema4740_below_at_h` | one_head_filter_pi_star | 312 | 25.5125 | 0.9440 | 0.5321 | -0.4379 | -0.0012 | 0.1282 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4740_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.8698 | 0.5000 | -0.6494 | -0.0068 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `ema4740_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.8239 | 0.5000 | -0.8877 | -0.0093 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4740_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4740_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0590 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
