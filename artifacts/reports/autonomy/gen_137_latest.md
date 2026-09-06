# Autonomy public-indicator hunt gen 137

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T182835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret48_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7165 | 0.6684 | 3.4983 | 0.0195 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret48_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.6453 | 0.6667 | 3.3410 | 0.0177 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret48_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1515 | 0.6982 | 4.0975 | 0.0175 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret48_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.9305 | 0.6726 | 3.5677 | 0.0149 | 0.3869 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret48_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.3050 | 0.6064 | 1.4594 | 0.0092 | 0.2287 | ok | RAN |
| ETHUSDT | 4 | `ret48_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3012 | 0.5989 | 1.4759 | 0.0092 | 0.2203 | ok | RAN |
| SOLUSDT | 8 | `ret48_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.5629 | 0.6215 | 2.7771 | 0.0078 | 0.2664 | ok | RAN |
| SOLUSDT | 4 | `ret48_pos_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.5252 | 0.6195 | 2.5799 | 0.0072 | 0.2683 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret48_cross_down_0` | one_head_filter_pi_star | 19 | 1.7766 | 1.0350 | 0.4737 | 0.0653 | 0.0007 | 0.1579 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret48_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret48_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret48_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret48_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret48_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret48_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret48_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret48_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret48_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret48_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
