# Autonomy public-indicator hunt gen 1458

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T224038Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1312_pos_at_h` | one_head_filter_pi_star | 19 | 1.8499 | 2.7212 | 0.7368 | 1.8653 | 0.0197 | 0.4211 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1312_neg_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 1.6374 | 0.6467 | 3.9091 | 0.0170 | 0.2991 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1312_neg_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 1.6076 | 0.6484 | 3.8005 | 0.0163 | 0.2997 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1312_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.7490 | 0.6414 | 4.3307 | 0.0111 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1312_neg_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 1.7136 | 0.6379 | 4.2610 | 0.0108 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1312_pos_at_h` | one_head_filter_pi_star | 21 | 4.2089 | 0.4804 | 0.3810 | -1.9658 | -0.0218 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `ret1312_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0512 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1312_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.4158 | 0.2308 | -1.1827 | -0.0533 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1312_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1312_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1312_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1312_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1312_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1312_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
