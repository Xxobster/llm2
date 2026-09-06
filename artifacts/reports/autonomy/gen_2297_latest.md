# Autonomy public-indicator hunt gen 2297

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T002032Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5300_above_at_h` | one_head_filter_pi_star | 37 | 3.4740 | 2.1473 | 0.6757 | 1.8002 | 0.0144 | 0.1351 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5300_above_at_h` | one_head_filter_pi_star | 52 | 4.4675 | 1.8445 | 0.6538 | 1.7513 | 0.0125 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5300_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9645 | 0.5329 | -0.2765 | -0.0007 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `ema5300_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9267 | 0.5240 | -0.5731 | -0.0016 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5300_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9425 | 0.5526 | -0.4867 | -0.0019 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema5300_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9300 | 0.5503 | -0.5799 | -0.0023 | 0.1391 | ok | RAN |
| ETHUSDT | 4 | `ema5300_above_at_h` | one_head_filter_pi_star | 45 | 13.2778 | 0.7359 | 0.4889 | -1.6750 | -0.0136 | 0.1333 | ok | RAN |
| ETHUSDT | 8 | `ema5300_above_at_h` | one_head_filter_pi_star | 49 | 5.7580 | 0.7396 | 0.4898 | -1.1392 | -0.0146 | 0.1633 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5300_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5300_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
