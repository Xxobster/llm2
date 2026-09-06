# Autonomy public-indicator hunt gen 1301

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T202643Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret229_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.3968 | 0.7257 | 5.1513 | 0.0298 | 0.4057 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret229_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 2.2332 | 0.7027 | 4.3072 | 0.0275 | 0.4257 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret229_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8642 | 0.6538 | 3.5610 | 0.0126 | 0.3626 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret229_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8364 | 0.6497 | 3.6616 | 0.0125 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret229_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2331 | 0.6108 | 1.1558 | 0.0080 | 0.2270 | ok | RAN |
| SOLUSDT | 8 | `ret229_pos_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.4858 | 0.6235 | 2.1962 | 0.0075 | 0.2706 | ok | RAN |
| SOLUSDT | 4 | `ret229_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4840 | 0.6175 | 2.2111 | 0.0075 | 0.2842 | ok | RAN |
| ETHUSDT | 8 | `ret229_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1302 | 0.5798 | 0.6974 | 0.0049 | 0.2340 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret229_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret229_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret229_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret229_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret229_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret229_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
