# Autonomy public-indicator hunt gen 331

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T115521Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma118_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0119 | 0.6943 | 4.4960 | 0.0240 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma118_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9406 | 0.6853 | 4.3867 | 0.0225 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma118_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.3195 | 0.6959 | 4.4684 | 0.0183 | 0.3860 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma118_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2685 | 0.6928 | 4.2770 | 0.0182 | 0.3916 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma118_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2098 | 0.6043 | 1.0803 | 0.0071 | 0.2193 | ok | RAN |
| ETHUSDT | 8 | `sma118_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1352 | 0.5936 | 0.7101 | 0.0048 | 0.2193 | ok | RAN |
| SOLUSDT | 4 | `sma118_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2773 | 0.5960 | 1.4828 | 0.0044 | 0.2677 | ok | RAN |
| SOLUSDT | 8 | `sma118_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2520 | 0.5859 | 1.3639 | 0.0040 | 0.2677 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma118_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma118_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma118_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma118_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma118_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma118_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
