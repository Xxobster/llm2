# Autonomy public-indicator hunt gen 1850

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T185442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1704_pos_at_h` | one_head_filter_pi_star | 15 | 4.5943 | 1.6694 | 0.6667 | 1.7678 | 0.0246 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `ret1704_pos_at_h` | one_head_filter_pi_star | 18 | 5.5132 | 1.4208 | 0.6111 | 1.1884 | 0.0181 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `ret1704_pos_at_h` | one_head_filter_pi_star | 20 | 2.2020 | 1.3196 | 0.6000 | 0.5297 | 0.0054 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1704_neg_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 0.9726 | 0.5350 | -0.2063 | -0.0005 | 0.1242 | ok | RAN |
| SOLUSDT | 8 | `ret1704_neg_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9580 | 0.5370 | -0.3146 | -0.0008 | 0.1286 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1704_neg_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 0.9401 | 0.5565 | -0.5110 | -0.0020 | 0.1384 | ok | RAN |
| ETHUSDT | 8 | `ret1704_neg_at_h` | one_head_filter_pi_star | 360 | 29.2867 | 0.9305 | 0.5556 | -0.6012 | -0.0024 | 0.1361 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1704_pos_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.3786 | 0.3000 | -1.7717 | -0.0905 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1704_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1704_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1704_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1704_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
