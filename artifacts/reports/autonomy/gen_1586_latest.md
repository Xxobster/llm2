# Autonomy public-indicator hunt gen 1586

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T163149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1440_pos_at_h` | one_head_filter_pi_star | 20 | 1.7005 | 2.0901 | 0.7000 | 1.3935 | 0.0128 | 0.1500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1440_pos_at_h` | one_head_filter_pi_star | 24 | 2.0203 | 1.7467 | 0.6667 | 1.1880 | 0.0105 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1440_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.0043 | 0.5455 | 0.0330 | 0.0001 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1440_neg_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9997 | 0.5529 | -0.0025 | -0.0000 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1440_neg_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 0.9219 | 0.5437 | -0.6320 | -0.0026 | 0.1406 | ok | RAN |
| ETHUSDT | 8 | `ret1440_neg_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 0.9203 | 0.5457 | -0.6604 | -0.0027 | 0.1372 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1440_pos_at_h` | one_head_filter_pi_star | 21 | 2.0618 | 0.7202 | 0.4762 | -0.7021 | -0.0173 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1440_pos_at_h` | one_head_filter_pi_star | 23 | 2.2581 | 0.6037 | 0.4783 | -1.0562 | -0.0222 | 0.1739 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1440_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5402 | 0.3000 | -1.0429 | -0.0522 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1440_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.2968 | 0.2353 | -1.7297 | -0.0858 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1440_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1440_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1440_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1440_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
