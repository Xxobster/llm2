# Autonomy public-indicator hunt gen 682

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T055423Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret536_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.5432 | 0.7216 | 5.2796 | 0.0302 | 0.4034 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret536_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.2143 | 0.7088 | 4.6742 | 0.0261 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret536_neg_at_h` | one_head_filter_pi_star | 190 | 15.9137 | 1.6275 | 0.6368 | 2.8210 | 0.0108 | 0.3368 | ok | RAN |
| SOLUSDT | 8 | `ret536_neg_at_h` | one_head_filter_pi_star | 189 | 15.7231 | 1.6191 | 0.6455 | 2.7641 | 0.0104 | 0.3386 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret536_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2052 | 0.5932 | 1.0328 | 0.0077 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `ret536_pos_at_h` | one_head_filter_pi_star | 161 | 13.3812 | 1.3776 | 0.5652 | 1.7711 | 0.0062 | 0.2733 | ok | RAN |
| SOLUSDT | 8 | `ret536_pos_at_h` | one_head_filter_pi_star | 138 | 11.2526 | 1.2705 | 0.5435 | 1.2250 | 0.0048 | 0.2609 | ok | RAN |
| ETHUSDT | 8 | `ret536_pos_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.0936 | 0.5706 | 0.4912 | 0.0036 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret536_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0360 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret536_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret536_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret536_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret536_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret536_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
