# Autonomy public-indicator hunt gen 2393

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T130043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5540_above_at_h` | one_head_filter_pi_star | 38 | 3.5233 | 2.2751 | 0.6316 | 1.8553 | 0.0136 | 0.0789 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5540_above_at_h` | one_head_filter_pi_star | 52 | 4.8213 | 1.6861 | 0.6154 | 1.4739 | 0.0093 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5540_below_at_h` | one_head_filter_pi_star | 311 | 25.4307 | 0.9821 | 0.5338 | -0.1376 | -0.0004 | 0.1286 | ok | RAN |
| SOLUSDT | 8 | `ema5540_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9694 | 0.5327 | -0.2401 | -0.0006 | 0.1246 | ok | RAN |
| ETHUSDT | 4 | `ema5540_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9704 | 0.5578 | -0.2460 | -0.0010 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5540_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9363 | 0.5498 | -0.5207 | -0.0021 | 0.1390 | ok | RAN |
| ETHUSDT | 4 | `ema5540_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.8919 | 0.5250 | -0.5363 | -0.0054 | 0.1750 | ok | RAN |
| ETHUSDT | 8 | `ema5540_above_at_h` | one_head_filter_pi_star | 44 | 12.8427 | 0.7237 | 0.4773 | -1.7286 | -0.0158 | 0.1818 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5540_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0590 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5540_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0615 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
