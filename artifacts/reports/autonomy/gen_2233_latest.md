# Autonomy public-indicator hunt gen 2233

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T163903Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5140_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.6404 | 0.6230 | 1.4806 | 0.0096 | 0.0984 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5140_above_at_h` | one_head_filter_pi_star | 68 | 6.3048 | 1.5828 | 0.6324 | 1.5324 | 0.0083 | 0.1029 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5140_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9928 | 0.5390 | -0.0541 | -0.0001 | 0.1396 | ok | RAN |
| ETHUSDT | 8 | `ema5140_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9727 | 0.5581 | -0.2217 | -0.0009 | 0.1366 | ok | RAN |
| SOLUSDT | 4 | `ema5140_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9542 | 0.5316 | -0.3613 | -0.0009 | 0.1297 | ok | RAN |
| ETHUSDT | 4 | `ema5140_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9517 | 0.5552 | -0.3989 | -0.0016 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5140_above_at_h` | one_head_filter_pi_star | 34 | 9.9239 | 0.9589 | 0.5294 | -0.2215 | -0.0019 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `ema5140_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.8381 | 0.5152 | -0.8174 | -0.0080 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5140_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5140_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
