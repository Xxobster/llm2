# Autonomy public-indicator hunt gen 1157

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T055011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret209_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1679 | 0.7066 | 4.5890 | 0.0269 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret209_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.1084 | 0.6988 | 4.4709 | 0.0250 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret209_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0085 | 0.6649 | 3.9649 | 0.0152 | 0.3564 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret209_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 2.0513 | 0.6784 | 4.2244 | 0.0147 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret209_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5832 | 0.6286 | 2.6121 | 0.0086 | 0.2686 | ok | RAN |
| ETHUSDT | 8 | `ret209_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.2397 | 0.5941 | 1.2773 | 0.0083 | 0.2376 | ok | RAN |
| SOLUSDT | 4 | `ret209_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.5042 | 0.6127 | 2.2955 | 0.0075 | 0.2890 | ok | RAN |
| ETHUSDT | 4 | `ret209_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.2117 | 0.5891 | 1.0935 | 0.0074 | 0.2327 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret209_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret209_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret209_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret209_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret209_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret209_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
