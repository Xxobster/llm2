# Autonomy public-indicator hunt gen 1828

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T165616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1019_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.3361 | 0.6239 | 1.3616 | 0.0057 | 0.1197 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1019_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.0058 | 0.5434 | 0.0400 | 0.0001 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1019_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0042 | 0.5462 | 0.0195 | 0.0001 | 0.1008 | ok | RAN |
| ETHUSDT | 4 | `ema1019_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 0.9902 | 0.5478 | -0.0662 | -0.0003 | 0.1478 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1019_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9194 | 0.5328 | -0.5787 | -0.0018 | 0.1236 | ok | RAN |
| ETHUSDT | 8 | `ema1019_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9410 | 0.5422 | -0.4022 | -0.0018 | 0.1467 | ok | RAN |
| ETHUSDT | 8 | `ema1019_above_at_h` | one_head_filter_pi_star | 120 | 9.9034 | 0.9461 | 0.5417 | -0.2436 | -0.0023 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema1019_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.9435 | 0.5571 | -0.2792 | -0.0024 | 0.1286 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1019_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1019_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1019_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1019_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1019_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1019_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
