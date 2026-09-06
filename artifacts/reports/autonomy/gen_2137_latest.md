# Autonomy public-indicator hunt gen 2137

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T024545Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4900_above_at_h` | one_head_filter_pi_star | 57 | 4.6857 | 1.6565 | 0.6491 | 1.4890 | 0.0097 | 0.1053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4900_above_at_h` | one_head_filter_pi_star | 56 | 4.8111 | 1.5777 | 0.6429 | 1.2601 | 0.0086 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4900_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9834 | 0.5355 | -0.1263 | -0.0003 | 0.1323 | ok | RAN |
| SOLUSDT | 8 | `ema4900_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 0.9540 | 0.5282 | -0.3507 | -0.0010 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4900_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9490 | 0.5549 | -0.4231 | -0.0017 | 0.1358 | ok | RAN |
| ETHUSDT | 8 | `ema4900_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9324 | 0.5529 | -0.5654 | -0.0023 | 0.1353 | ok | RAN |
| ETHUSDT | 8 | `ema4900_above_at_h` | one_head_filter_pi_star | 38 | 11.0914 | 0.9315 | 0.5263 | -0.3905 | -0.0035 | 0.1579 | ok | RAN |
| ETHUSDT | 4 | `ema4900_above_at_h` | one_head_filter_pi_star | 34 | 9.9239 | 0.8868 | 0.5294 | -0.5174 | -0.0054 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4900_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4900_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
