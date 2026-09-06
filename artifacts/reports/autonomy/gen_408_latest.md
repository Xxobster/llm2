# Autonomy public-indicator hunt gen 408

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T040430Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma620_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1954 | 0.7027 | 4.8077 | 0.0260 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma620_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9696 | 0.6774 | 4.1617 | 0.0237 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma620_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7614 | 0.6649 | 3.3507 | 0.0114 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma620_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.7291 | 0.6616 | 3.2460 | 0.0114 | 0.3232 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma620_above_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.5603 | 0.6118 | 2.2824 | 0.0088 | 0.3158 | ok | RAN |
| ETHUSDT | 8 | `sma620_above_at_h` | one_head_filter_pi_star | 142 | 11.7180 | 1.2133 | 0.6056 | 0.9923 | 0.0074 | 0.1972 | ok | RAN |
| SOLUSDT | 8 | `sma620_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.4390 | 0.5942 | 1.8101 | 0.0070 | 0.3116 | ok | RAN |
| ETHUSDT | 4 | `sma620_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1251 | 0.5988 | 0.6484 | 0.0047 | 0.2160 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
