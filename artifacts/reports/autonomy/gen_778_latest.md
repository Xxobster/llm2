# Autonomy public-indicator hunt gen 778

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T133021Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret632_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1802 | 0.7053 | 4.6982 | 0.0252 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret632_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9968 | 0.6943 | 4.2181 | 0.0219 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret632_neg_at_h` | one_head_filter_pi_star | 223 | 18.2349 | 1.8806 | 0.6682 | 3.8984 | 0.0143 | 0.3274 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret632_neg_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 1.7358 | 0.6425 | 3.4391 | 0.0125 | 0.3258 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret632_pos_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.6879 | 0.6457 | 2.3545 | 0.0091 | 0.2756 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret632_pos_at_h` | one_head_filter_pi_star | 146 | 12.0491 | 1.2110 | 0.5753 | 0.9930 | 0.0083 | 0.2329 | ok | RAN |
| SOLUSDT | 8 | `ret632_pos_at_h` | one_head_filter_pi_star | 104 | 8.5484 | 1.5383 | 0.6442 | 1.8909 | 0.0070 | 0.2596 | ok | RAN |
| ETHUSDT | 4 | `ret632_pos_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.0954 | 0.5478 | 0.4922 | 0.0038 | 0.2229 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret632_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.5297 | 0.3333 | -0.9414 | -0.0558 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret632_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4677 | 0.2353 | -1.1523 | -0.0590 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret632_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret632_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret632_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret632_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
