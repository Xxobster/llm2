# Autonomy public-indicator hunt gen 1170

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T071933Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1024_neg_at_h` | one_head_filter_pi_star | 250 | 20.4227 | 1.7235 | 0.6560 | 3.7470 | 0.0179 | 0.3400 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1024_neg_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.7078 | 0.6500 | 4.0674 | 0.0177 | 0.3300 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1024_neg_at_h` | one_head_filter_pi_star | 287 | 23.4682 | 1.7458 | 0.6411 | 3.7984 | 0.0117 | 0.3310 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1024_neg_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 1.7734 | 0.6447 | 4.1164 | 0.0117 | 0.3224 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1024_pos_at_h` | one_head_filter_pi_star | 68 | 5.5457 | 1.7265 | 0.6471 | 1.9070 | 0.0102 | 0.2794 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1024_pos_at_h` | one_head_filter_pi_star | 71 | 5.9010 | 1.4320 | 0.6338 | 1.3594 | 0.0075 | 0.2817 | ok | RAN |
| ETHUSDT | 4 | `ret1024_pos_at_h` | one_head_filter_pi_star | 79 | 6.7629 | 1.0276 | 0.5696 | 0.1085 | 0.0014 | 0.2152 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1024_pos_at_h` | one_head_filter_pi_star | 63 | 5.3679 | 0.8885 | 0.5556 | -0.4218 | -0.0061 | 0.2222 | ok | RAN |
| BTCUSDT | 8 | `ret1024_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3827 | 0.2353 | -1.3686 | -0.0551 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1024_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3273 | 0.2778 | -1.5882 | -0.0715 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1024_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1024_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1024_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1024_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
