# Autonomy public-indicator hunt gen 946

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T063249Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret800_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8827 | 0.6823 | 3.5540 | 0.0195 | 0.3542 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret800_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8486 | 0.6769 | 3.5543 | 0.0191 | 0.3590 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret800_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9641 | 0.6684 | 3.7803 | 0.0158 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret800_neg_at_h` | one_head_filter_pi_star | 224 | 18.3167 | 1.7381 | 0.6429 | 3.3143 | 0.0127 | 0.3482 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret800_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.2481 | 0.5649 | 1.1064 | 0.0098 | 0.2338 | ok | RAN |
| SOLUSDT | 8 | `ret800_pos_at_h` | one_head_filter_pi_star | 48 | 3.9452 | 1.5477 | 0.6250 | 1.2245 | 0.0073 | 0.2292 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret800_pos_at_h` | one_head_filter_pi_star | 47 | 3.8630 | 1.5060 | 0.6383 | 1.2241 | 0.0070 | 0.2128 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret800_pos_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.0393 | 0.5600 | 0.1868 | 0.0019 | 0.2320 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret800_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.6403 | 0.3571 | -0.6409 | -0.0294 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret800_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6477 | 0.3750 | -0.6836 | -0.0339 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret800_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret800_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret800_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret800_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
