# Autonomy public-indicator hunt gen 970

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T203905Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret824_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 2.3373 | 0.7197 | 4.3388 | 0.0250 | 0.4076 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret824_neg_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0265 | 0.6893 | 4.2262 | 0.0219 | 0.3544 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret824_neg_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.9003 | 0.6531 | 4.0098 | 0.0144 | 0.3388 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret824_neg_at_h` | one_head_filter_pi_star | 220 | 18.2521 | 1.7684 | 0.6364 | 3.4644 | 0.0128 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret824_pos_at_h` | one_head_filter_pi_star | 69 | 5.6712 | 1.6464 | 0.6522 | 1.7639 | 0.0085 | 0.2319 | ok | RAN |
| SOLUSDT | 8 | `ret824_pos_at_h` | one_head_filter_pi_star | 73 | 5.9907 | 1.5109 | 0.6575 | 1.4094 | 0.0076 | 0.2603 | ok | RAN |
| ETHUSDT | 8 | `ret824_pos_at_h` | one_head_filter_pi_star | 98 | 8.0878 | 1.1591 | 0.5918 | 0.6402 | 0.0073 | 0.2449 | ok | RAN |
| ETHUSDT | 4 | `ret824_pos_at_h` | one_head_filter_pi_star | 108 | 8.8775 | 1.0922 | 0.5741 | 0.3828 | 0.0046 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret824_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.8820 | 0.3750 | -0.1919 | -0.0099 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret824_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.7840 | 0.3529 | -0.3893 | -0.0175 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret824_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret824_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret824_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret824_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
