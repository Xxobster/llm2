# Autonomy public-indicator hunt gen 1860

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T194727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1024_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.3228 | 0.6218 | 1.2429 | 0.0053 | 0.1345 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1024_above_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.0413 | 0.5887 | 0.1870 | 0.0017 | 0.1210 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1024_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9936 | 0.5430 | -0.0438 | -0.0001 | 0.1250 | ok | RAN |
| SOLUSDT | 8 | `ema1024_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 0.9571 | 0.5417 | -0.2050 | -0.0008 | 0.1167 | ok | RAN |
| ETHUSDT | 4 | `ema1024_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9527 | 0.5439 | -0.3214 | -0.0015 | 0.1535 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1024_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9209 | 0.5331 | -0.5636 | -0.0017 | 0.1323 | ok | RAN |
| ETHUSDT | 8 | `ema1024_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9416 | 0.5395 | -0.4077 | -0.0018 | 0.1535 | ok | RAN |
| ETHUSDT | 8 | `ema1024_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 0.8976 | 0.5463 | -0.4597 | -0.0044 | 0.1204 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1024_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1024_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1024_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1024_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1024_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1024_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
