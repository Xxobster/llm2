# Autonomy public-indicator hunt gen 2292

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T234435Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1081_above_at_h` | one_head_filter_pi_star | 104 | 8.5479 | 1.2473 | 0.6058 | 0.9432 | 0.0042 | 0.1442 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1081_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.1478 | 0.5926 | 0.6062 | 0.0027 | 0.1389 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1081_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9797 | 0.5542 | -0.1455 | -0.0006 | 0.1542 | ok | RAN |
| SOLUSDT | 4 | `ema1081_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 0.9639 | 0.5394 | -0.2462 | -0.0008 | 0.1299 | ok | RAN |
| SOLUSDT | 8 | `ema1081_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9537 | 0.5361 | -0.3284 | -0.0010 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema1081_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9596 | 0.5402 | -0.2731 | -0.0012 | 0.1607 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1081_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8951 | 0.5507 | -0.5300 | -0.0046 | 0.1232 | ok | RAN |
| ETHUSDT | 8 | `ema1081_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 0.8740 | 0.5321 | -0.5896 | -0.0054 | 0.1376 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1081_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1081_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1081_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1081_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1081_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1081_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
