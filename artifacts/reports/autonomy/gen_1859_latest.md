# Autonomy public-indicator hunt gen 1859

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T194210Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma722_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1317 | 0.5665 | 0.7491 | 0.0039 | 0.1965 | ok | RAN |
| SOLUSDT | 4 | `sma722_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.2044 | 0.5652 | 0.8514 | 0.0036 | 0.1130 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma722_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.0942 | 0.5621 | 0.5474 | 0.0028 | 0.1775 | ok | RAN |
| SOLUSDT | 8 | `sma722_above_at_h` | one_head_filter_pi_star | 117 | 9.7242 | 1.0823 | 0.5470 | 0.3622 | 0.0015 | 0.1197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma722_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9434 | 0.5622 | -0.3510 | -0.0012 | 0.1343 | ok | RAN |
| SOLUSDT | 8 | `sma722_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9309 | 0.5505 | -0.4282 | -0.0015 | 0.1414 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma722_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.9531 | 0.5704 | -0.2367 | -0.0018 | 0.1056 | ok | RAN |
| ETHUSDT | 8 | `sma722_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.9111 | 0.5695 | -0.4768 | -0.0035 | 0.1060 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma722_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0607 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma722_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma722_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma722_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma722_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma722_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
