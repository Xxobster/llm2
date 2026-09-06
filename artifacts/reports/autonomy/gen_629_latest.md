# Autonomy public-indicator hunt gen 629

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T022234Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret105_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.7919 | 0.6722 | 3.7508 | 0.0199 | 0.3611 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret105_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7228 | 0.6548 | 3.5591 | 0.0192 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret105_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.3860 | 0.6895 | 4.8122 | 0.0178 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret105_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2349 | 0.6889 | 4.2953 | 0.0165 | 0.3444 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret105_pos_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.4429 | 0.6457 | 2.0224 | 0.0138 | 0.2457 | ok | RAN |
| ETHUSDT | 4 | `ret105_pos_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.3813 | 0.6359 | 1.8036 | 0.0121 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret105_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3817 | 0.6041 | 1.9212 | 0.0059 | 0.2640 | ok | RAN |
| SOLUSDT | 4 | `ret105_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.3681 | 0.5989 | 1.8428 | 0.0059 | 0.2599 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret105_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret105_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret105_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret105_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret105_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret105_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
