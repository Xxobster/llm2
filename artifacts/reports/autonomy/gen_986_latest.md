# Autonomy public-indicator hunt gen 986

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T121705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret840_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.1148 | 0.6950 | 4.5245 | 0.0237 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret840_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 2.1041 | 0.6976 | 4.5165 | 0.0232 | 0.3707 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret840_neg_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.9921 | 0.6707 | 4.3405 | 0.0151 | 0.3455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret840_neg_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8700 | 0.6537 | 3.8721 | 0.0142 | 0.3420 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret840_pos_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.1968 | 0.5726 | 0.8728 | 0.0078 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ret840_pos_at_h` | one_head_filter_pi_star | 78 | 6.4410 | 1.5059 | 0.6410 | 1.6245 | 0.0075 | 0.2436 | ok | RAN |
| SOLUSDT | 8 | `ret840_pos_at_h` | one_head_filter_pi_star | 89 | 7.3151 | 1.4675 | 0.6404 | 1.5147 | 0.0075 | 0.2921 | ok | RAN |
| ETHUSDT | 4 | `ret840_pos_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 1.0769 | 0.5583 | 0.3353 | 0.0033 | 0.2417 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret840_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.7754 | 0.3529 | -0.4102 | -0.0184 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret840_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5980 | 0.3333 | -0.8392 | -0.0436 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret840_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret840_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret840_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret840_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
