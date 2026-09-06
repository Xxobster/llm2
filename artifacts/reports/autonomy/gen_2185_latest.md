# Autonomy public-indicator hunt gen 2185

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T103416Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5020_above_at_h` | one_head_filter_pi_star | 65 | 5.3434 | 2.3112 | 0.7077 | 2.5071 | 0.0146 | 0.1077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5020_above_at_h` | one_head_filter_pi_star | 72 | 5.9188 | 1.7616 | 0.6389 | 1.8848 | 0.0106 | 0.0972 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema5020_above_at_h` | one_head_filter_pi_star | 25 | 7.5441 | 1.0795 | 0.5200 | 0.3128 | 0.0035 | 0.1200 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5020_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9721 | 0.5304 | -0.2143 | -0.0006 | 0.1342 | ok | RAN |
| SOLUSDT | 8 | `ema5020_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9702 | 0.5363 | -0.2302 | -0.0006 | 0.1325 | ok | RAN |
| ETHUSDT | 8 | `ema5020_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9689 | 0.5565 | -0.2540 | -0.0010 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ema5020_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9617 | 0.5556 | -0.3128 | -0.0013 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5020_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.9384 | 0.5429 | -0.2877 | -0.0027 | 0.1143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5020_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5020_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
