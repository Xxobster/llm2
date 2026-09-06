# Autonomy public-indicator hunt gen 1101

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T231412Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret201_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0820 | 0.6977 | 4.4544 | 0.0252 | 0.4012 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret201_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0812 | 0.7011 | 4.5017 | 0.0250 | 0.3908 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret201_neg_at_h` | one_head_filter_pi_star | 149 | 12.1839 | 2.0454 | 0.6913 | 3.6338 | 0.0156 | 0.3960 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret201_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.9181 | 0.6648 | 3.6725 | 0.0138 | 0.3693 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret201_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5985 | 0.6250 | 2.6189 | 0.0091 | 0.2670 | ok | RAN |
| SOLUSDT | 4 | `ret201_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5620 | 0.6250 | 2.5363 | 0.0086 | 0.2826 | ok | RAN |
| ETHUSDT | 4 | `ret201_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1269 | 0.5957 | 0.6773 | 0.0046 | 0.2181 | ok | RAN |
| ETHUSDT | 8 | `ret201_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.0993 | 0.5819 | 0.5382 | 0.0037 | 0.2260 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret201_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret201_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret201_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret201_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret201_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret201_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
