# Autonomy public-indicator hunt gen 436

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T105431Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema305_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9742 | 0.6931 | 4.2953 | 0.0227 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema305_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7837 | 0.6733 | 3.8435 | 0.0198 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema305_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9695 | 0.6789 | 3.9300 | 0.0146 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema305_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.9796 | 0.6701 | 3.9536 | 0.0146 | 0.3608 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema305_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.3283 | 0.6141 | 1.6165 | 0.0107 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema305_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5638 | 0.6250 | 2.6021 | 0.0084 | 0.2717 | ok | RAN |
| SOLUSDT | 8 | `ema305_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4583 | 0.6042 | 2.2727 | 0.0071 | 0.2604 | ok | RAN |
| ETHUSDT | 4 | `ema305_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.1924 | 0.6012 | 0.9873 | 0.0068 | 0.2023 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema305_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema305_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema305_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema305_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
