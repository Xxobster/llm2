# Autonomy public-indicator hunt gen 1050

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T163852Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret904_neg_at_h` | one_head_filter_pi_star | 261 | 21.3213 | 1.7787 | 0.6667 | 4.0692 | 0.0189 | 0.3487 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret904_neg_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 1.7318 | 0.6570 | 3.8649 | 0.0178 | 0.3471 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret904_neg_at_h` | one_head_filter_pi_star | 220 | 18.0153 | 1.9964 | 0.6591 | 4.0920 | 0.0149 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret904_neg_at_h` | one_head_filter_pi_star | 235 | 19.4480 | 1.9225 | 0.6468 | 4.0664 | 0.0138 | 0.3234 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret904_pos_at_h` | one_head_filter_pi_star | 50 | 4.2199 | 2.0353 | 0.7000 | 2.1772 | 0.0133 | 0.2000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret904_pos_at_h` | one_head_filter_pi_star | 47 | 3.9759 | 1.8779 | 0.7021 | 1.9607 | 0.0131 | 0.2128 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret904_pos_at_h` | one_head_filter_pi_star | 55 | 4.5391 | 1.1316 | 0.5636 | 0.4102 | 0.0063 | 0.2545 | ok | RAN |
| ETHUSDT | 8 | `ret904_pos_at_h` | one_head_filter_pi_star | 113 | 9.2885 | 1.0579 | 0.5752 | 0.2567 | 0.0026 | 0.2035 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret904_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4406 | 0.2857 | -1.1310 | -0.0500 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret904_pos_at_h` | one_head_filter_pi_star | 11 | 0.9361 | 0.1907 | 0.2727 | -1.7343 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret904_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret904_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret904_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret904_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
