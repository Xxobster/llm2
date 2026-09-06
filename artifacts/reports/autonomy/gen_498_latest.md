# Autonomy public-indicator hunt gen 498

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T174712Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret352_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.2862 | 0.7135 | 4.8108 | 0.0288 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret352_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0138 | 0.6995 | 4.2918 | 0.0241 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret352_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.7473 | 0.6569 | 3.4379 | 0.0116 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret352_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.7154 | 0.6452 | 2.8414 | 0.0111 | 0.2903 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret352_pos_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.7312 | 0.6387 | 2.8140 | 0.0108 | 0.3097 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret352_neg_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.6299 | 0.6402 | 3.0274 | 0.0104 | 0.3131 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret352_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.1866 | 0.5977 | 0.9269 | 0.0071 | 0.2241 | ok | RAN |
| ETHUSDT | 4 | `ret352_pos_at_h` | one_head_filter_pi_star | 180 | 14.7472 | 1.1722 | 0.6000 | 0.8798 | 0.0062 | 0.2056 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret352_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0467 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret352_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0512 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret352_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret352_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret352_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret352_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
