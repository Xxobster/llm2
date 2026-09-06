# Autonomy public-indicator hunt gen 2324

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T033353Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1085_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1085_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.2400 | 0.6083 | 0.9892 | 0.0040 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1085_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.1615 | 0.6018 | 0.6934 | 0.0028 | 0.1416 | ok | RAN |
| SOLUSDT | 8 | `ema1085_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.0162 | 0.5484 | 0.1081 | 0.0003 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1085_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 0.9451 | 0.5415 | -0.3815 | -0.0012 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `ema1085_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9595 | 0.5432 | -0.2963 | -0.0013 | 0.1523 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1085_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 0.9453 | 0.5388 | -0.4070 | -0.0018 | 0.1510 | ok | RAN |
| ETHUSDT | 4 | `ema1085_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 0.8681 | 0.5391 | -0.6406 | -0.0060 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema1085_above_at_h` | one_head_filter_pi_star | 100 | 8.2528 | 0.8320 | 0.5300 | -0.7725 | -0.0079 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1085_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1085_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1085_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1085_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1085_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
