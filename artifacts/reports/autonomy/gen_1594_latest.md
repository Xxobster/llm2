# Autonomy public-indicator hunt gen 1594

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T172718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1448_pos_at_h` | one_head_filter_pi_star | 13 | 1.4497 | 2.2332 | 0.6923 | 1.3863 | 0.0185 | 0.0769 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1448_pos_at_h` | one_head_filter_pi_star | 12 | 1.0203 | 2.2940 | 0.6667 | 1.2450 | 0.0161 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1448_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.0052 | 0.5474 | 0.0398 | 0.0001 | 0.1346 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1448_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 0.9783 | 0.5424 | -0.1690 | -0.0004 | 0.1394 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1448_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9474 | 0.5509 | -0.4307 | -0.0017 | 0.1377 | ok | RAN |
| ETHUSDT | 8 | `ret1448_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 0.9225 | 0.5446 | -0.6411 | -0.0026 | 0.1385 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1448_pos_at_h` | one_head_filter_pi_star | 18 | 2.1152 | 0.5384 | 0.3889 | -1.3295 | -0.0336 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1448_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6388 | 0.2941 | -0.7038 | -0.0363 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1448_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3880 | 0.2222 | -1.4607 | -0.0735 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1448_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1448_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1448_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
