# Autonomy public-indicator hunt gen 2177

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T091940Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5000_above_at_h` | one_head_filter_pi_star | 56 | 4.8675 | 1.9714 | 0.6786 | 1.8766 | 0.0123 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5000_above_at_h` | one_head_filter_pi_star | 62 | 5.3266 | 1.4640 | 0.6290 | 1.1455 | 0.0074 | 0.1452 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema5000_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 1.1631 | 0.5806 | 0.6602 | 0.0063 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5000_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9802 | 0.5335 | -0.1512 | -0.0004 | 0.1342 | ok | RAN |
| SOLUSDT | 4 | `ema5000_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9591 | 0.5348 | -0.3175 | -0.0009 | 0.1392 | ok | RAN |
| ETHUSDT | 4 | `ema5000_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9623 | 0.5569 | -0.3080 | -0.0012 | 0.1370 | ok | RAN |
| ETHUSDT | 8 | `ema5000_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9514 | 0.5526 | -0.3991 | -0.0016 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5000_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.8718 | 0.5263 | -0.6529 | -0.0063 | 0.1316 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5000_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5000_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
