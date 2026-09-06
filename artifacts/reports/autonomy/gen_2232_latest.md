# Autonomy public-indicator hunt gen 2232

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T163205Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5180_above_at_h` | one_head_filter_pi_star | 47 | 4.3466 | 2.3042 | 0.6170 | 2.1320 | 0.0152 | 0.0851 | ok | RAN |
| SOLUSDT | 4 | `sma5180_above_at_h` | one_head_filter_pi_star | 52 | 4.4279 | 1.8330 | 0.5962 | 1.6447 | 0.0111 | 0.0962 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5180_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9965 | 0.5588 | -0.0279 | -0.0001 | 0.1324 | ok | RAN |
| SOLUSDT | 8 | `sma5180_below_at_h` | one_head_filter_pi_star | 296 | 24.0802 | 0.9619 | 0.5338 | -0.2833 | -0.0008 | 0.1284 | ok | RAN |
| SOLUSDT | 4 | `sma5180_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9575 | 0.5378 | -0.3397 | -0.0009 | 0.1299 | ok | RAN |
| ETHUSDT | 8 | `sma5180_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9727 | 0.5556 | -0.2217 | -0.0009 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5180_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.8308 | 0.5143 | -0.9728 | -0.0085 | 0.1143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5180_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.6671 | 0.4737 | -2.0929 | -0.0195 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5180_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5180_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
