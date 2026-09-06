# Autonomy public-indicator hunt gen 765

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T121041Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret139_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.8861 | 0.6738 | 4.0805 | 0.0216 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret139_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8527 | 0.6735 | 4.0177 | 0.0210 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret139_neg_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 2.2413 | 0.6919 | 4.6882 | 0.0170 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret139_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.0841 | 0.6862 | 4.1241 | 0.0157 | 0.3511 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret139_pos_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.3499 | 0.6190 | 1.6786 | 0.0118 | 0.2202 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret139_pos_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.1983 | 0.5978 | 1.0345 | 0.0070 | 0.2283 | ok | RAN |
| SOLUSDT | 4 | `ret139_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3872 | 0.5959 | 1.9115 | 0.0062 | 0.2694 | ok | RAN |
| SOLUSDT | 8 | `ret139_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3651 | 0.5936 | 1.8158 | 0.0058 | 0.2567 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret139_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret139_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret139_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret139_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret139_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret139_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
