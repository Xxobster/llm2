# Autonomy public-indicator hunt gen 1802

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T143546Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1656_pos_at_h` | one_head_filter_pi_star | 23 | 6.9406 | 1.4054 | 0.5652 | 1.3807 | 0.0155 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `ret1656_pos_at_h` | one_head_filter_pi_star | 22 | 2.1417 | 1.9504 | 0.6818 | 1.3881 | 0.0117 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1656_pos_at_h` | one_head_filter_pi_star | 29 | 2.8232 | 1.5488 | 0.6207 | 0.9500 | 0.0084 | 0.1034 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1656_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9960 | 0.5422 | -0.0307 | -0.0001 | 0.1235 | ok | RAN |
| SOLUSDT | 4 | `ret1656_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9534 | 0.5362 | -0.3739 | -0.0009 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1656_neg_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9366 | 0.5559 | -0.5442 | -0.0021 | 0.1347 | ok | RAN |
| ETHUSDT | 8 | `ret1656_neg_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9308 | 0.5533 | -0.5957 | -0.0023 | 0.1354 | ok | RAN |
| ETHUSDT | 8 | `ret1656_pos_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.8324 | 0.5833 | -0.5715 | -0.0096 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1656_pos_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3761 | 0.2727 | -1.7901 | -0.0859 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1656_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1656_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1656_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
