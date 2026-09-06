# Autonomy public-indicator hunt gen 1261

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T162517Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret223_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.9893 | 0.6910 | 4.2515 | 0.0247 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret223_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0137 | 0.6971 | 4.1741 | 0.0241 | 0.4057 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret223_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0190 | 0.6648 | 3.9747 | 0.0150 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret223_neg_at_h` | one_head_filter_pi_star | 189 | 15.4703 | 1.9945 | 0.6772 | 4.1238 | 0.0149 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret223_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.4987 | 0.6127 | 2.2344 | 0.0076 | 0.2717 | ok | RAN |
| ETHUSDT | 4 | `ret223_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2058 | 0.5909 | 1.0605 | 0.0073 | 0.2121 | ok | RAN |
| SOLUSDT | 4 | `ret223_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.4297 | 0.6145 | 1.9502 | 0.0067 | 0.2771 | ok | RAN |
| ETHUSDT | 8 | `ret223_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1678 | 0.5892 | 0.8413 | 0.0061 | 0.2324 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret223_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret223_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret223_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret223_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret223_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret223_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
