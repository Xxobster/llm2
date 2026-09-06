# Autonomy public-indicator hunt gen 2196

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T115902Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1068_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.2670 | 0.5965 | 1.0370 | 0.0044 | 0.1316 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1068_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.1529 | 0.5847 | 0.6462 | 0.0027 | 0.1271 | ok | RAN |
| ETHUSDT | 4 | `ema1068_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.0059 | 0.5570 | 0.0413 | 0.0002 | 0.1477 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1068_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 0.9932 | 0.5635 | -0.0304 | -0.0003 | 0.1190 | ok | RAN |
| ETHUSDT | 8 | `ema1068_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9794 | 0.5583 | -0.1451 | -0.0007 | 0.1583 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1068_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9214 | 0.5287 | -0.5673 | -0.0017 | 0.1264 | ok | RAN |
| SOLUSDT | 4 | `ema1068_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9044 | 0.5310 | -0.6810 | -0.0021 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema1068_above_at_h` | one_head_filter_pi_star | 107 | 8.8305 | 0.8257 | 0.5234 | -0.8002 | -0.0080 | 0.1215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1068_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1068_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0568 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1068_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1068_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1068_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1068_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
