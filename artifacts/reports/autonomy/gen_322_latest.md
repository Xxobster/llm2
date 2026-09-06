# Autonomy public-indicator hunt gen 322

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T104139Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret176_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1827 | 0.7126 | 4.6887 | 0.0257 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret176_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0096 | 0.6971 | 4.1937 | 0.0242 | 0.3886 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret176_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1296 | 0.6802 | 4.0944 | 0.0157 | 0.3547 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret176_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.9499 | 0.6667 | 3.5085 | 0.0144 | 0.3697 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret176_pos_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2577 | 0.5979 | 1.3375 | 0.0085 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `ret176_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4734 | 0.6143 | 2.3564 | 0.0074 | 0.2762 | ok | RAN |
| SOLUSDT | 4 | `ret176_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4565 | 0.6082 | 2.2035 | 0.0070 | 0.2680 | ok | RAN |
| ETHUSDT | 8 | `ret176_pos_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.1639 | 0.5864 | 0.8696 | 0.0057 | 0.2094 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret176_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret176_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret176_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret176_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret176_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret176_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
