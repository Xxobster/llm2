# Autonomy public-indicator hunt gen 1554

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T075123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1408_pos_at_h` | one_head_filter_pi_star | 25 | 2.3298 | 2.9352 | 0.7600 | 2.4825 | 0.0225 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret1408_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5649 | 0.6380 | 3.4987 | 0.0152 | 0.3027 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1408_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5541 | 0.6388 | 3.3736 | 0.0148 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1408_pos_at_h` | one_head_filter_pi_star | 29 | 2.4658 | 1.9648 | 0.6897 | 1.5369 | 0.0134 | 0.3793 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1408_pos_at_h` | one_head_filter_pi_star | 54 | 4.7488 | 1.2765 | 0.5926 | 0.8592 | 0.0119 | 0.2593 | ok | RAN |
| SOLUSDT | 4 | `ret1408_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.7360 | 0.6352 | 4.1491 | 0.0109 | 0.3113 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1408_neg_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.7217 | 0.6361 | 4.0722 | 0.0107 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1408_pos_at_h` | one_head_filter_pi_star | 24 | 2.3563 | 1.0110 | 0.5417 | 0.0257 | 0.0006 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1408_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6092 | 0.3158 | -0.8112 | -0.0390 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1408_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4715 | 0.2353 | -1.1334 | -0.0569 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1408_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1408_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
