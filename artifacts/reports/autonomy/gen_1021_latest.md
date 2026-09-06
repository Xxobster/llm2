# Autonomy public-indicator hunt gen 1021

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T131606Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret398_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.3070 | 0.7202 | 4.7006 | 0.0289 | 0.4048 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret398_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1448 | 0.6979 | 4.6863 | 0.0259 | 0.3594 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret398_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9545 | 0.6842 | 3.8380 | 0.0137 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret398_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.7560 | 0.6686 | 3.1753 | 0.0115 | 0.3432 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret398_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.6147 | 0.6118 | 2.4592 | 0.0102 | 0.3224 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret398_pos_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5994 | 0.6301 | 2.4159 | 0.0090 | 0.2397 | ok | RAN |
| ETHUSDT | 8 | `ret398_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2465 | 0.6062 | 1.1832 | 0.0089 | 0.2375 | ok | RAN |
| ETHUSDT | 4 | `ret398_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1768 | 0.5930 | 0.9181 | 0.0067 | 0.2209 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret398_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5824 | 0.3158 | -0.9020 | -0.0420 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret398_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0452 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret398_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret398_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret398_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret398_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
