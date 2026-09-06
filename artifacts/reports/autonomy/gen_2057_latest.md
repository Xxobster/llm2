# Autonomy public-indicator hunt gen 2057

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T161819Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4700_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 1.9093 | 0.6774 | 1.8616 | 0.0122 | 0.1129 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4700_above_at_h` | one_head_filter_pi_star | 67 | 5.5081 | 1.6302 | 0.6567 | 1.4605 | 0.0100 | 0.1045 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema4700_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 1.0303 | 0.5588 | 0.1392 | 0.0013 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4700_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9969 | 0.5614 | -0.0240 | -0.0001 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `ema4700_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 0.9770 | 0.5318 | -0.1729 | -0.0005 | 0.1371 | ok | RAN |
| SOLUSDT | 8 | `ema4700_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9723 | 0.5327 | -0.2153 | -0.0006 | 0.1340 | ok | RAN |
| ETHUSDT | 4 | `ema4700_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9545 | 0.5556 | -0.3742 | -0.0015 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4700_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8796 | 0.5000 | -0.5542 | -0.0060 | 0.1875 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4700_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
