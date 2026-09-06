# Autonomy public-indicator hunt gen 284

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T041951Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema125_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0389 | 0.6963 | 4.6329 | 0.0241 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema125_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9871 | 0.6927 | 4.4869 | 0.0233 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema125_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1943 | 0.6872 | 4.3023 | 0.0174 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema125_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1427 | 0.6810 | 3.9807 | 0.0170 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema125_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.1841 | 0.5979 | 0.9505 | 0.0065 | 0.2275 | ok | RAN |
| ETHUSDT | 8 | `ema125_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1713 | 0.5926 | 0.8672 | 0.0059 | 0.2275 | ok | RAN |
| SOLUSDT | 8 | `ema125_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3684 | 0.5972 | 1.9218 | 0.0056 | 0.2654 | ok | RAN |
| SOLUSDT | 4 | `ema125_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3365 | 0.5971 | 1.7593 | 0.0051 | 0.2670 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema125_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema125_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema125_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema125_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema125_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema125_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
