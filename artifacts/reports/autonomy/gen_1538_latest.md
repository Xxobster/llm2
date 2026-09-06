# Autonomy public-indicator hunt gen 1538

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T062158Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1392_pos_at_h` | one_head_filter_pi_star | 28 | 2.4212 | 2.8031 | 0.7500 | 2.2597 | 0.0205 | 0.4286 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1392_pos_at_h` | one_head_filter_pi_star | 42 | 3.5711 | 2.4325 | 0.7143 | 2.4429 | 0.0182 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1392_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5705 | 0.6396 | 3.5345 | 0.0156 | 0.3063 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1392_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.5828 | 0.6440 | 3.5060 | 0.0156 | 0.3127 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1392_pos_at_h` | one_head_filter_pi_star | 40 | 3.8586 | 1.3888 | 0.5750 | 0.9751 | 0.0152 | 0.2250 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1392_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.7535 | 0.6442 | 4.2031 | 0.0112 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1392_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.7541 | 0.6420 | 4.2987 | 0.0112 | 0.3107 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1392_pos_at_h` | one_head_filter_pi_star | 22 | 2.1599 | 1.1729 | 0.5455 | 0.3829 | 0.0062 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1392_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0430 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1392_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4715 | 0.2353 | -1.1334 | -0.0632 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1392_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1392_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1392_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1392_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
