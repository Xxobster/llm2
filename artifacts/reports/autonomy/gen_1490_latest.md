# Autonomy public-indicator hunt gen 1490

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T015157Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1344_pos_at_h` | one_head_filter_pi_star | 23 | 2.0032 | 2.4924 | 0.7391 | 1.9166 | 0.0215 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1344_pos_at_h` | one_head_filter_pi_star | 27 | 2.3515 | 2.3100 | 0.7037 | 1.8756 | 0.0172 | 0.4074 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1344_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.5928 | 0.6453 | 3.5515 | 0.0158 | 0.3119 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1344_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5792 | 0.6429 | 3.5384 | 0.0155 | 0.3095 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1344_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.7851 | 0.6437 | 4.4693 | 0.0114 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1344_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.7482 | 0.6407 | 4.3019 | 0.0112 | 0.3114 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1344_pos_at_h` | one_head_filter_pi_star | 34 | 3.2375 | 1.2208 | 0.5588 | 0.5114 | 0.0083 | 0.2941 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1344_pos_at_h` | one_head_filter_pi_star | 23 | 2.2581 | 0.7742 | 0.4783 | -0.5704 | -0.0125 | 0.3478 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1344_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0289 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1344_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0295 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1344_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1344_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1344_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1344_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
