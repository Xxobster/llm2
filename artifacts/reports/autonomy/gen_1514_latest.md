# Autonomy public-indicator hunt gen 1514

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T040443Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1368_pos_at_h` | one_head_filter_pi_star | 40 | 3.3251 | 2.7298 | 0.7250 | 2.6147 | 0.0190 | 0.3500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1368_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.5828 | 0.6391 | 3.4610 | 0.0156 | 0.3089 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1368_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5264 | 0.6382 | 3.2954 | 0.0143 | 0.2971 | ok | RAN |
| ETHUSDT | 8 | `ret1368_pos_at_h` | one_head_filter_pi_star | 31 | 3.0435 | 1.3665 | 0.5806 | 0.8013 | 0.0130 | 0.2258 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1368_pos_at_h` | one_head_filter_pi_star | 35 | 2.9090 | 1.8300 | 0.6571 | 1.6184 | 0.0124 | 0.3714 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1368_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.7551 | 0.6394 | 4.2166 | 0.0113 | 0.3121 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1368_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.7183 | 0.6386 | 4.0711 | 0.0109 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1368_pos_at_h` | one_head_filter_pi_star | 31 | 3.0435 | 1.0845 | 0.5161 | 0.1995 | 0.0034 | 0.2258 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1368_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6137 | 0.2667 | -0.7289 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1368_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.4158 | 0.2308 | -1.1827 | -0.0600 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1368_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1368_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1368_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1368_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
