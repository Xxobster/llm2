# Autonomy public-indicator hunt gen 994

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T201716Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret848_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.3182 | 0.7136 | 5.0238 | 0.0262 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret848_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 2.3334 | 0.7179 | 4.3723 | 0.0256 | 0.3910 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret848_neg_at_h` | one_head_filter_pi_star | 232 | 19.2477 | 2.1430 | 0.6810 | 4.6192 | 0.0172 | 0.3405 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret848_neg_at_h` | one_head_filter_pi_star | 223 | 18.5010 | 2.0541 | 0.6637 | 4.3126 | 0.0162 | 0.3498 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret848_pos_at_h` | one_head_filter_pi_star | 86 | 7.0974 | 1.2283 | 0.5930 | 0.8148 | 0.0097 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `ret848_pos_at_h` | one_head_filter_pi_star | 90 | 7.3386 | 1.5702 | 0.6222 | 1.8193 | 0.0077 | 0.2556 | ok | RAN |
| ETHUSDT | 8 | `ret848_pos_at_h` | one_head_filter_pi_star | 106 | 8.7131 | 1.1623 | 0.5755 | 0.6659 | 0.0070 | 0.2736 | ok | RAN |
| SOLUSDT | 4 | `ret848_pos_at_h` | one_head_filter_pi_star | 101 | 8.3014 | 1.2073 | 0.5941 | 0.8149 | 0.0034 | 0.2475 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret848_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.8521 | 0.3571 | -0.2454 | -0.0127 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret848_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.7754 | 0.3529 | -0.4102 | -0.0200 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret848_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret848_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret848_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret848_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
