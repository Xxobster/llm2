# Autonomy public-indicator hunt gen 973

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T213819Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret191_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1255 | 0.6946 | 4.6425 | 0.0265 | 0.3952 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret191_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.9802 | 0.6860 | 4.0598 | 0.0230 | 0.3837 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret191_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0013 | 0.6647 | 3.7328 | 0.0149 | 0.3713 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret191_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.9558 | 0.6647 | 3.6802 | 0.0143 | 0.3584 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret191_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4762 | 0.6209 | 2.2229 | 0.0076 | 0.2747 | ok | RAN |
| SOLUSDT | 8 | `ret191_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4134 | 0.6042 | 2.0259 | 0.0066 | 0.2708 | ok | RAN |
| ETHUSDT | 4 | `ret191_pos_at_h` | one_head_filter_pi_star | 199 | 16.4218 | 1.1735 | 0.5879 | 0.9163 | 0.0062 | 0.2462 | ok | RAN |
| ETHUSDT | 8 | `ret191_pos_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.1593 | 0.5926 | 0.8365 | 0.0056 | 0.2169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret191_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret191_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret191_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret191_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret191_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret191_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
