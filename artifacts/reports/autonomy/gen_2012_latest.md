# Autonomy public-indicator hunt gen 2012

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T104011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1044_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.3571 | 0.6161 | 1.3692 | 0.0059 | 0.1429 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1044_above_at_h` | one_head_filter_pi_star | 124 | 10.1918 | 1.1773 | 0.5806 | 0.7640 | 0.0032 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `ema1044_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.0123 | 0.5536 | 0.0817 | 0.0004 | 0.1562 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1044_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9642 | 0.5423 | -0.2510 | -0.0008 | 0.1308 | ok | RAN |
| SOLUSDT | 4 | `ema1044_below_at_h` | one_head_filter_pi_star | 259 | 21.0702 | 0.9272 | 0.5367 | -0.5156 | -0.0016 | 0.1274 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1044_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9148 | 0.5401 | -0.6322 | -0.0028 | 0.1561 | ok | RAN |
| ETHUSDT | 4 | `ema1044_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.9329 | 0.5556 | -0.3120 | -0.0029 | 0.1282 | ok | RAN |
| ETHUSDT | 8 | `ema1044_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 0.8411 | 0.5263 | -0.7347 | -0.0070 | 0.1228 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1044_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0313 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1044_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1044_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1044_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1044_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1044_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
