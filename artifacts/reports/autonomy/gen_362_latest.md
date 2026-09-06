# Autonomy public-indicator hunt gen 362

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T170658Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret216_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.2888 | 0.7160 | 4.6354 | 0.0277 | 0.4136 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret216_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1805 | 0.7012 | 4.5805 | 0.0266 | 0.3963 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret216_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0558 | 0.6791 | 4.0647 | 0.0155 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret216_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8324 | 0.6633 | 3.6038 | 0.0129 | 0.3668 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret216_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2617 | 0.5938 | 1.3284 | 0.0088 | 0.2135 | ok | RAN |
| SOLUSDT | 4 | `ret216_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5314 | 0.6216 | 2.4550 | 0.0081 | 0.2703 | ok | RAN |
| SOLUSDT | 8 | `ret216_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5221 | 0.6175 | 2.4133 | 0.0080 | 0.2623 | ok | RAN |
| ETHUSDT | 8 | `ret216_pos_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 1.1060 | 0.5714 | 0.5764 | 0.0039 | 0.2266 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret216_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret216_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret216_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret216_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret216_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret216_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
