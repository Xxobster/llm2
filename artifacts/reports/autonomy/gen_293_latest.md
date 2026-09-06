# Autonomy public-indicator hunt gen 293

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T045947Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret26_cross_down_0` | one_head_filter_pi_star | 46 | 3.7977 | 2.9138 | 0.6522 | 2.9266 | 0.0368 | 0.3043 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret26_cross_up_0` | one_head_filter_pi_star | 37 | 3.0963 | 1.9370 | 0.6216 | 1.6353 | 0.0324 | 0.1622 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret26_neg_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.8438 | 0.6792 | 4.0384 | 0.0215 | 0.3821 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret26_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8446 | 0.6794 | 3.9712 | 0.0212 | 0.3876 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret26_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2446 | 0.6951 | 4.1700 | 0.0182 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret26_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0749 | 0.6807 | 3.8504 | 0.0164 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret26_cross_up_0` | one_head_filter_pi_star | 26 | 2.2410 | 2.0476 | 0.6154 | 1.4204 | 0.0149 | 0.2308 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret26_pos_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.4248 | 0.6077 | 2.2213 | 0.0062 | 0.2536 | ok | RAN |
| ETHUSDT | 4 | `ret26_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1886 | 0.5964 | 0.9114 | 0.0061 | 0.2048 | ok | RAN |
| SOLUSDT | 8 | `ret26_cross_down_0` | one_head_filter_pi_star | 38 | 3.1246 | 1.2998 | 0.5526 | 0.6529 | 0.0060 | 0.1579 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret26_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3873 | 0.5953 | 2.0374 | 0.0058 | 0.2512 | ok | RAN |
| ETHUSDT | 8 | `ret26_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1709 | 0.5987 | 0.8079 | 0.0054 | 0.1783 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret26_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret26_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret26_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret26_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret26_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret26_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret26_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret26_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret26_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret26_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret26_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret26_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
