# Autonomy public-indicator hunt gen 1066

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T185144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret920_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.0267 | 0.7066 | 3.8999 | 0.0235 | 0.4251 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret920_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.8310 | 0.6798 | 3.5552 | 0.0202 | 0.4045 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret920_neg_at_h` | one_head_filter_pi_star | 254 | 20.6634 | 2.0422 | 0.6614 | 4.5862 | 0.0147 | 0.3150 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret920_neg_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.8691 | 0.6484 | 4.1296 | 0.0132 | 0.3187 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret920_pos_at_h` | one_head_filter_pi_star | 31 | 2.7862 | 1.4499 | 0.6452 | 0.9207 | 0.0083 | 0.3226 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret920_pos_at_h` | one_head_filter_pi_star | 44 | 3.8934 | 1.5063 | 0.6591 | 1.1961 | 0.0077 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret920_pos_at_h` | one_head_filter_pi_star | 64 | 5.6282 | 1.1263 | 0.6094 | 0.4397 | 0.0060 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `ret920_pos_at_h` | one_head_filter_pi_star | 51 | 4.4850 | 1.1128 | 0.5686 | 0.3542 | 0.0057 | 0.2745 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret920_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.8593 | 0.3571 | -0.2239 | -0.0118 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret920_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4775 | 0.3529 | -1.1191 | -0.0550 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret920_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret920_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret920_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret920_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
