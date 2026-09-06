# Autonomy public-indicator hunt gen 1851

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T185954Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma721_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2554 | 0.5952 | 1.3933 | 0.0070 | 0.1964 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma721_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1886 | 0.5873 | 1.1216 | 0.0055 | 0.1746 | ok | RAN |
| SOLUSDT | 4 | `sma721_above_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.1284 | 0.5667 | 0.5707 | 0.0023 | 0.1083 | ok | RAN |
| SOLUSDT | 8 | `sma721_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.1017 | 0.5476 | 0.4597 | 0.0018 | 0.1190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma721_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9607 | 0.5594 | -0.2426 | -0.0008 | 0.1386 | ok | RAN |
| SOLUSDT | 4 | `sma721_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9380 | 0.5561 | -0.3916 | -0.0014 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma721_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.9483 | 0.5694 | -0.2665 | -0.0021 | 0.1111 | ok | RAN |
| ETHUSDT | 8 | `sma721_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.9017 | 0.5774 | -0.5392 | -0.0039 | 0.1012 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma721_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma721_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma721_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma721_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma721_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma721_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
