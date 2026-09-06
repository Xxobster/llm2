# Autonomy public-indicator hunt gen 1506

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T032103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1360_pos_at_h` | one_head_filter_pi_star | 22 | 1.9161 | 2.7842 | 0.7273 | 1.9252 | 0.0209 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1360_pos_at_h` | one_head_filter_pi_star | 28 | 2.4710 | 2.4350 | 0.7143 | 2.0319 | 0.0181 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1360_pos_at_h` | one_head_filter_pi_star | 33 | 3.3133 | 1.4025 | 0.6061 | 0.9457 | 0.0151 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1360_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.5437 | 0.6369 | 3.2587 | 0.0147 | 0.3046 | ok | RAN |
| ETHUSDT | 8 | `ret1360_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.5220 | 0.6380 | 3.2405 | 0.0141 | 0.3067 | ok | RAN |
| SOLUSDT | 8 | `ret1360_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.7409 | 0.6388 | 4.2201 | 0.0111 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1360_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.7150 | 0.6366 | 4.1392 | 0.0107 | 0.3093 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1360_pos_at_h` | one_head_filter_pi_star | 32 | 3.1417 | 1.2358 | 0.5625 | 0.5620 | 0.0098 | 0.2812 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1360_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.4158 | 0.2308 | -1.1827 | -0.0600 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1360_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3361 | 0.2353 | -1.5077 | -0.0715 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
