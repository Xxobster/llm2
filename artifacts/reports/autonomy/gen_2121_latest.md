# Autonomy public-indicator hunt gen 2121

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T005107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4860_above_at_h` | one_head_filter_pi_star | 40 | 3.7557 | 1.6767 | 0.6500 | 1.2457 | 0.0093 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4860_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 1.6094 | 0.6346 | 1.2460 | 0.0089 | 0.0962 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4860_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9895 | 0.5380 | -0.0812 | -0.0002 | 0.1361 | ok | RAN |
| SOLUSDT | 4 | `ema4860_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9681 | 0.5294 | -0.2429 | -0.0007 | 0.1340 | ok | RAN |
| ETHUSDT | 4 | `ema4860_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9642 | 0.5562 | -0.2877 | -0.0012 | 0.1391 | ok | RAN |
| ETHUSDT | 8 | `ema4860_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9576 | 0.5559 | -0.3471 | -0.0014 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4860_above_at_h` | one_head_filter_pi_star | 36 | 4.2304 | 0.9343 | 0.5278 | -0.2036 | -0.0031 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `ema4860_above_at_h` | one_head_filter_pi_star | 29 | 8.9414 | 0.8204 | 0.5172 | -0.8208 | -0.0084 | 0.1034 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4860_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4860_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
