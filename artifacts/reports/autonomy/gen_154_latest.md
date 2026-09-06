# Autonomy public-indicator hunt gen 154

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T193413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret96_neg_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.8390 | 0.6714 | 4.0846 | 0.0214 | 0.3619 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret96_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7919 | 0.6598 | 3.7754 | 0.0203 | 0.3711 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret96_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2275 | 0.6740 | 4.3415 | 0.0170 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret96_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0965 | 0.6591 | 4.0079 | 0.0163 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret96_pos_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3314 | 0.6257 | 1.5828 | 0.0108 | 0.2235 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret96_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2977 | 0.6188 | 1.4831 | 0.0096 | 0.2320 | ok | RAN |
| SOLUSDT | 4 | `ret96_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3364 | 0.5990 | 1.7458 | 0.0053 | 0.2552 | ok | RAN |
| SOLUSDT | 8 | `ret96_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3194 | 0.5936 | 1.6521 | 0.0051 | 0.2567 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret96_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret96_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret96_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret96_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret96_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret96_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
