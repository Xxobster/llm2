# Autonomy public-indicator hunt gen 1418

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T082421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1272_pos_at_h` | one_head_filter_pi_star | 12 | 1.5436 | 2.6824 | 0.7500 | 1.6529 | 0.0207 | 0.5000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret1272_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.6483 | 0.6548 | 3.9973 | 0.0168 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1272_neg_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.6150 | 0.6503 | 3.8473 | 0.0165 | 0.3006 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1272_pos_at_h` | one_head_filter_pi_star | 17 | 1.8710 | 2.4854 | 0.7647 | 1.7119 | 0.0163 | 0.5294 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1272_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.7981 | 0.6420 | 4.4385 | 0.0117 | 0.3166 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1272_neg_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 1.7145 | 0.6404 | 4.2723 | 0.0110 | 0.3174 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1272_pos_at_h` | one_head_filter_pi_star | 24 | 2.3716 | 0.5788 | 0.3750 | -1.2007 | -0.0229 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1272_pos_at_h` | one_head_filter_pi_star | 16 | 1.5709 | 0.5672 | 0.3750 | -1.1084 | -0.0260 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1272_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0289 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1272_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0388 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1272_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1272_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1272_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1272_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
