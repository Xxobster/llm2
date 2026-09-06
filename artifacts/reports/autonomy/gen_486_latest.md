# Autonomy public-indicator hunt gen 486

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T165952Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma210_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0447 | 0.6931 | 4.6105 | 0.0237 | 0.3651 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma210_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9906 | 0.6895 | 4.4880 | 0.0232 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma210_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2433 | 0.6983 | 4.3963 | 0.0176 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma210_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1733 | 0.6971 | 4.2206 | 0.0170 | 0.3771 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma210_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2337 | 0.6021 | 1.1791 | 0.0079 | 0.2304 | ok | RAN |
| ETHUSDT | 4 | `wma210_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2075 | 0.5978 | 1.0588 | 0.0070 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `wma210_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3038 | 0.5813 | 1.6281 | 0.0048 | 0.2660 | ok | RAN |
| SOLUSDT | 4 | `wma210_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3073 | 0.5902 | 1.6222 | 0.0048 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma210_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma210_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma210_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma210_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma210_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma210_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
