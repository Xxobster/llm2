# Autonomy public-indicator hunt gen 276

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T034659Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema115_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0843 | 0.7016 | 4.7457 | 0.0249 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema115_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9839 | 0.6927 | 4.4800 | 0.0233 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema115_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2685 | 0.6959 | 4.3786 | 0.0183 | 0.3860 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema115_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2740 | 0.6932 | 4.4619 | 0.0181 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema115_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2155 | 0.6000 | 1.0910 | 0.0071 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `ema115_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1820 | 0.5957 | 0.9395 | 0.0063 | 0.2287 | ok | RAN |
| SOLUSDT | 8 | `ema115_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3449 | 0.5943 | 1.8163 | 0.0052 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `ema115_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3185 | 0.5902 | 1.6644 | 0.0049 | 0.2683 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema115_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema115_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema115_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema115_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema115_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema115_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
