# Autonomy public-indicator hunt gen 1562

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T164022Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1416_pos_at_h` | one_head_filter_pi_star | 28 | 2.3807 | 3.1454 | 0.7500 | 2.5340 | 0.0250 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1416_pos_at_h` | one_head_filter_pi_star | 33 | 2.8059 | 2.9538 | 0.7273 | 2.4147 | 0.0246 | 0.3939 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1416_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5517 | 0.6439 | 3.4287 | 0.0151 | 0.3056 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1416_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.5488 | 0.6369 | 3.2843 | 0.0149 | 0.3108 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1416_pos_at_h` | one_head_filter_pi_star | 30 | 2.9454 | 1.2977 | 0.6000 | 0.6504 | 0.0125 | 0.3000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1416_neg_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 1.7031 | 0.6375 | 4.0013 | 0.0107 | 0.3094 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1416_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.7320 | 0.6440 | 4.1287 | 0.0105 | 0.3127 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1416_pos_at_h` | one_head_filter_pi_star | 36 | 3.5344 | 1.1921 | 0.5556 | 0.4866 | 0.0084 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1416_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4715 | 0.2353 | -1.1334 | -0.0605 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1416_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3172 | 0.1875 | -1.5524 | -0.0782 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1416_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1416_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1416_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1416_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
