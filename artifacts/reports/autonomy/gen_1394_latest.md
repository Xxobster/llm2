# Autonomy public-indicator hunt gen 1394

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T050823Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1248_pos_at_h` | one_head_filter_pi_star | 14 | 1.2708 | 2.4606 | 0.7143 | 1.4675 | 0.0209 | 0.4286 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1248_pos_at_h` | one_head_filter_pi_star | 18 | 1.9208 | 2.8025 | 0.7778 | 1.8833 | 0.0189 | 0.4444 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1248_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.6526 | 0.6492 | 3.9262 | 0.0167 | 0.3200 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1248_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.6448 | 0.6506 | 3.9661 | 0.0167 | 0.3133 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1248_neg_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 1.7833 | 0.6422 | 4.3363 | 0.0118 | 0.3355 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1248_neg_at_h` | one_head_filter_pi_star | 341 | 27.8839 | 1.7393 | 0.6422 | 4.3471 | 0.0114 | 0.3167 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1248_pos_at_h` | one_head_filter_pi_star | 13 | 1.2763 | 1.2680 | 0.5385 | 0.4163 | 0.0085 | 0.3846 | EBR>35% | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1248_pos_at_h` | one_head_filter_pi_star | 45 | 4.1389 | 1.0118 | 0.5556 | 0.0360 | 0.0006 | 0.2222 | ok | RAN |
| BTCUSDT | 8 | `ret1248_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3423 | 0.2778 | -1.4934 | -0.0644 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1248_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0679 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1248_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1248_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1248_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1248_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
