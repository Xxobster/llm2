# Autonomy public-indicator hunt gen 1985

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T072353Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4520_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 1.6407 | 0.6324 | 1.5750 | 0.0093 | 0.1176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4520_above_at_h` | one_head_filter_pi_star | 73 | 6.0010 | 1.3069 | 0.6164 | 0.9184 | 0.0055 | 0.1370 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4520_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 1.0107 | 0.5431 | 0.0802 | 0.0002 | 0.1310 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4520_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 0.9879 | 0.5331 | -0.0905 | -0.0003 | 0.1325 | ok | RAN |
| ETHUSDT | 8 | `ema4520_above_at_h` | one_head_filter_pi_star | 37 | 10.7995 | 0.9787 | 0.5405 | -0.1046 | -0.0010 | 0.1622 | ok | RAN |
| ETHUSDT | 4 | `ema4520_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9619 | 0.5569 | -0.3090 | -0.0013 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4520_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9412 | 0.5549 | -0.4946 | -0.0020 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `ema4520_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.7100 | 0.4667 | -1.4741 | -0.0162 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
