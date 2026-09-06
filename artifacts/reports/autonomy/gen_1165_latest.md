# Autonomy public-indicator hunt gen 1165

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T065016Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret210_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.1212 | 0.6975 | 4.4188 | 0.0266 | 0.4136 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret210_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0518 | 0.7011 | 4.3625 | 0.0235 | 0.3851 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret210_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0000 | 0.6667 | 3.8741 | 0.0149 | 0.3661 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret210_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9835 | 0.6743 | 3.7894 | 0.0146 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret210_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.5189 | 0.6265 | 2.2497 | 0.0078 | 0.2771 | ok | RAN |
| SOLUSDT | 4 | `ret210_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5117 | 0.6198 | 2.4025 | 0.0077 | 0.2656 | ok | RAN |
| ETHUSDT | 8 | `ret210_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.1731 | 0.5859 | 0.9025 | 0.0062 | 0.2172 | ok | RAN |
| ETHUSDT | 4 | `ret210_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1666 | 0.5936 | 0.8979 | 0.0060 | 0.2299 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret210_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret210_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret210_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret210_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret210_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret210_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
