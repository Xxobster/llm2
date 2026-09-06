# Autonomy public-indicator hunt gen 474

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T161259Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret328_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.3814 | 0.7267 | 4.9352 | 0.0299 | 0.4224 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret328_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.3922 | 0.7251 | 4.8595 | 0.0281 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret328_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.6673 | 0.6500 | 2.9658 | 0.0109 | 0.3444 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret328_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.7322 | 0.6158 | 3.0018 | 0.0104 | 0.2825 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret328_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6904 | 0.6149 | 2.8111 | 0.0102 | 0.2919 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret328_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.6104 | 0.6583 | 2.9338 | 0.0101 | 0.3317 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret328_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.1432 | 0.5941 | 0.7608 | 0.0052 | 0.2277 | ok | RAN |
| ETHUSDT | 4 | `ret328_pos_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1283 | 0.5988 | 0.6352 | 0.0047 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret328_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret328_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0650 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret328_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret328_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
