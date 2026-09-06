# Autonomy public-indicator hunt gen 1389

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T044047Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret242_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1600 | 0.6984 | 4.7416 | 0.0263 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret242_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.1028 | 0.7055 | 4.4427 | 0.0259 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret242_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.9275 | 0.6576 | 3.7077 | 0.0143 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret242_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8077 | 0.6489 | 3.4448 | 0.0118 | 0.3404 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret242_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2865 | 0.6140 | 1.4148 | 0.0095 | 0.2339 | ok | RAN |
| SOLUSDT | 4 | `ret242_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.6439 | 0.6393 | 2.7299 | 0.0094 | 0.2787 | ok | RAN |
| ETHUSDT | 8 | `ret242_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2279 | 0.6000 | 1.1453 | 0.0080 | 0.2324 | ok | RAN |
| SOLUSDT | 8 | `ret242_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.4820 | 0.6193 | 2.1556 | 0.0074 | 0.2898 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret242_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret242_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret242_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret242_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret242_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret242_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
