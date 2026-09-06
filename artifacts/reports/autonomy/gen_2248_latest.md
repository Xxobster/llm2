# Autonomy public-indicator hunt gen 2248

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T182547Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5220_above_at_h` | one_head_filter_pi_star | 38 | 3.5679 | 2.1676 | 0.6053 | 1.8181 | 0.0155 | 0.0789 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5220_above_at_h` | one_head_filter_pi_star | 57 | 5.3518 | 1.7886 | 0.6316 | 1.6868 | 0.0108 | 0.1053 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5220_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.0182 | 0.5621 | 0.1451 | 0.0006 | 0.1331 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5220_above_at_h` | one_head_filter_pi_star | 29 | 8.5568 | 0.9926 | 0.5517 | -0.0297 | -0.0003 | 0.1724 | ok | RAN |
| SOLUSDT | 4 | `sma5220_below_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9795 | 0.5392 | -0.1617 | -0.0004 | 0.1295 | ok | RAN |
| ETHUSDT | 4 | `sma5220_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9852 | 0.5588 | -0.1192 | -0.0005 | 0.1353 | ok | RAN |
| SOLUSDT | 8 | `sma5220_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 0.9723 | 0.5372 | -0.2093 | -0.0006 | 0.1294 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5220_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.8476 | 0.5135 | -0.7679 | -0.0078 | 0.1622 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
