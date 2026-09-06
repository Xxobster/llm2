# Autonomy public-indicator hunt gen 1530

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T053823Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1384_pos_at_h` | one_head_filter_pi_star | 30 | 2.5254 | 2.2746 | 0.7000 | 1.9509 | 0.0157 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1384_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5630 | 0.6420 | 3.4655 | 0.0154 | 0.3047 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1384_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5599 | 0.6377 | 3.4403 | 0.0152 | 0.3054 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1384_pos_at_h` | one_head_filter_pi_star | 33 | 2.7774 | 1.8079 | 0.6970 | 1.5857 | 0.0135 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1384_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.7839 | 0.6437 | 4.3963 | 0.0114 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1384_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.7489 | 0.6429 | 4.2490 | 0.0111 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1384_pos_at_h` | one_head_filter_pi_star | 36 | 3.5344 | 1.2128 | 0.5833 | 0.5322 | 0.0089 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1384_pos_at_h` | one_head_filter_pi_star | 22 | 2.5852 | 0.9382 | 0.5000 | -0.1537 | -0.0027 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1384_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4121 | 0.2000 | -1.2008 | -0.0518 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1384_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4715 | 0.2353 | -1.1334 | -0.0605 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1384_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1384_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1384_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1384_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
