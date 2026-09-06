# Autonomy public-indicator hunt gen 2284

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T224541Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1079_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1079_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1079_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.2593 | 0.6053 | 1.0452 | 0.0045 | 0.1491 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1079_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.2037 | 0.6091 | 0.8192 | 0.0034 | 0.1364 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1079_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9963 | 0.5560 | -0.0254 | -0.0001 | 0.1509 | ok | RAN |
| SOLUSDT | 8 | `ema1079_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9684 | 0.5426 | -0.2205 | -0.0007 | 0.1279 | ok | RAN |
| SOLUSDT | 4 | `ema1079_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 0.9508 | 0.5420 | -0.3283 | -0.0010 | 0.1261 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1079_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9244 | 0.5353 | -0.5522 | -0.0024 | 0.1452 | ok | RAN |
| ETHUSDT | 4 | `ema1079_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 0.9228 | 0.5588 | -0.3691 | -0.0034 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema1079_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.8382 | 0.5403 | -0.7997 | -0.0069 | 0.1129 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1079_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1079_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1079_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1079_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
