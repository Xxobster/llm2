# Autonomy public-indicator hunt gen 1541

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T063848Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret263_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.4285 | 0.7321 | 4.9402 | 0.0294 | 0.3988 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret263_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.1597 | 0.7118 | 4.5322 | 0.0264 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret263_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0039 | 0.6703 | 4.0151 | 0.0148 | 0.3514 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret263_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.9082 | 0.6685 | 3.7588 | 0.0135 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret263_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5770 | 0.6271 | 2.4888 | 0.0087 | 0.2825 | ok | RAN |
| SOLUSDT | 8 | `ret263_pos_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.4954 | 0.6111 | 2.2906 | 0.0079 | 0.2778 | ok | RAN |
| ETHUSDT | 4 | `ret263_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2010 | 0.5963 | 1.0078 | 0.0073 | 0.2174 | ok | RAN |
| ETHUSDT | 8 | `ret263_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1516 | 0.5978 | 0.7784 | 0.0055 | 0.2123 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret263_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret263_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret263_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret263_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret263_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret263_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
