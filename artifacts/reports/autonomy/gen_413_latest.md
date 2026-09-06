# Autonomy public-indicator hunt gen 413

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T051622Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret51_cross_down_0` | one_head_filter_pi_star | 24 | 2.2014 | 1.5172 | 0.6667 | 0.9294 | 0.0239 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret51_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.7793 | 0.6735 | 3.8365 | 0.0207 | 0.3622 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret51_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.6556 | 0.6683 | 3.3577 | 0.0184 | 0.3564 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret51_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0818 | 0.6886 | 3.9345 | 0.0167 | 0.3952 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret51_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.0643 | 0.6894 | 3.7849 | 0.0165 | 0.3975 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret51_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.4290 | 0.6162 | 1.9970 | 0.0128 | 0.2432 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret51_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2569 | 0.5955 | 1.2618 | 0.0085 | 0.2303 | ok | RAN |
| SOLUSDT | 8 | `ret51_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4426 | 0.6000 | 2.2950 | 0.0064 | 0.2619 | ok | RAN |
| SOLUSDT | 4 | `ret51_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.4150 | 0.5980 | 2.1523 | 0.0061 | 0.2549 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret51_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret51_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret51_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret51_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret51_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret51_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret51_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret51_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret51_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret51_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
