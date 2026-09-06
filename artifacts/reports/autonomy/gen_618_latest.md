# Autonomy public-indicator hunt gen 618

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T014036Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret472_neg_at_h` | one_head_filter_pi_star | 143 | 11.6818 | 2.6088 | 0.7413 | 4.9546 | 0.0318 | 0.4476 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret472_neg_at_h` | one_head_filter_pi_star | 146 | 11.9269 | 2.1832 | 0.6918 | 4.1505 | 0.0263 | 0.4178 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret472_neg_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 1.7718 | 0.6567 | 3.4202 | 0.0117 | 0.3383 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret472_neg_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 1.7656 | 0.6542 | 3.4281 | 0.0115 | 0.3318 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret472_pos_at_h` | one_head_filter_pi_star | 146 | 12.0563 | 1.5898 | 0.6096 | 2.3223 | 0.0096 | 0.3082 | ok | RAN |
| SOLUSDT | 8 | `ret472_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.5532 | 0.5848 | 2.3939 | 0.0087 | 0.2865 | ok | RAN |
| ETHUSDT | 8 | `ret472_pos_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.1863 | 0.5894 | 0.9046 | 0.0070 | 0.2252 | ok | RAN |
| ETHUSDT | 4 | `ret472_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.1521 | 0.5944 | 0.8034 | 0.0057 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret472_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0377 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret472_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret472_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret472_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret472_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret472_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
