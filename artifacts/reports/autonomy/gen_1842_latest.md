# Autonomy public-indicator hunt gen 1842

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T181225Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1696_pos_at_h` | one_head_filter_pi_star | 18 | 3.4813 | 1.7500 | 0.6111 | 1.5247 | 0.0252 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1696_pos_at_h` | one_head_filter_pi_star | 34 | 2.8263 | 2.2836 | 0.7059 | 1.9987 | 0.0180 | 0.2059 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1696_pos_at_h` | one_head_filter_pi_star | 29 | 2.4107 | 1.7465 | 0.6897 | 1.1851 | 0.0111 | 0.1724 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1696_pos_at_h` | one_head_filter_pi_star | 19 | 5.8195 | 1.1086 | 0.5263 | 0.3969 | 0.0044 | 0.2105 | ok | RAN |
| SOLUSDT | 8 | `ret1696_neg_at_h` | one_head_filter_pi_star | 289 | 23.5107 | 1.0443 | 0.5536 | 0.3057 | 0.0008 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1696_neg_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 0.9600 | 0.5340 | -0.3018 | -0.0008 | 0.1262 | ok | RAN |
| ETHUSDT | 8 | `ret1696_neg_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 0.9742 | 0.5597 | -0.2163 | -0.0009 | 0.1392 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1696_neg_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 0.9051 | 0.5499 | -0.8283 | -0.0033 | 0.1396 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1696_pos_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.3786 | 0.3000 | -1.7717 | -0.0850 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1696_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1696_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1696_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
