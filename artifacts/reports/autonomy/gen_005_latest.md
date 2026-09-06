# Autonomy public-indicator hunt gen 005

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260821T052857Z`. Arms: 33.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `bb_break_down` | one_head_filter_pi_star | 156 | 12.7438 | 1.8142 | 0.6859 | 3.3109 | 0.0230 | 0.4038 | EBR>35% | RAN |
| ETHUSDT | 8 | `bb_break_down` | one_head_filter_pi_star | 168 | 13.7241 | 1.7801 | 0.6845 | 3.2829 | 0.0215 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `bb_break_down` | one_head_filter_pi_star | 119 | 9.7307 | 2.0754 | 0.6807 | 3.2374 | 0.0178 | 0.3950 | EBR>35% | RAN |
| SOLUSDT | 8 | `bb_break_down` | one_head_filter_pi_star | 121 | 9.8943 | 2.0414 | 0.6777 | 3.2861 | 0.0174 | 0.4132 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `bb_break_up` | one_head_filter_pi_star | 99 | 8.1696 | 1.4146 | 0.6263 | 1.4616 | 0.0141 | 0.2323 | ok | RAN |
| ETHUSDT | 4 | `bb_break_up` | one_head_filter_pi_star | 117 | 9.6550 | 1.3861 | 0.6239 | 1.4703 | 0.0128 | 0.2393 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `bb_break_up` | one_head_filter_pi_star | 133 | 10.9067 | 1.5564 | 0.6165 | 2.2608 | 0.0095 | 0.3083 | ok | RAN |
| SOLUSDT | 8 | `bb_break_up` | one_head_filter_pi_star | 138 | 11.2526 | 1.3715 | 0.5870 | 1.5837 | 0.0065 | 0.2754 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `bb_break_up` | one_head_filter_pi_star | 14 | 1.1914 | 0.7943 | 0.3571 | -0.3366 | -0.0235 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 4 | `bb_break_up` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0470 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bb_break_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `bb_pctb_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bb_pctb_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bb_squeeze_expand` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bb_break_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
