# Autonomy public-indicator hunt gen 2145

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T040812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4920_above_at_h` | one_head_filter_pi_star | 52 | 4.8824 | 1.7906 | 0.6538 | 1.6483 | 0.0115 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4920_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.4767 | 0.6393 | 1.1804 | 0.0076 | 0.1148 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4920_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9887 | 0.5329 | -0.0844 | -0.0002 | 0.1414 | ok | RAN |
| SOLUSDT | 4 | `ema4920_below_at_h` | one_head_filter_pi_star | 322 | 26.3302 | 0.9798 | 0.5311 | -0.1568 | -0.0004 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `ema4920_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9690 | 0.5552 | -0.2442 | -0.0010 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4920_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9300 | 0.5513 | -0.5823 | -0.0023 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `ema4920_above_at_h` | one_head_filter_pi_star | 33 | 9.6320 | 0.8875 | 0.5152 | -0.5374 | -0.0056 | 0.1515 | ok | RAN |
| ETHUSDT | 8 | `ema4920_above_at_h` | one_head_filter_pi_star | 38 | 11.0914 | 0.8916 | 0.5263 | -0.6297 | -0.0057 | 0.1579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4920_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4920_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
