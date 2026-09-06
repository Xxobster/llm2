# Autonomy public-indicator hunt gen 361

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T170014Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema460_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9514 | 0.6716 | 4.3041 | 0.0227 | 0.3725 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema460_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9913 | 0.6859 | 4.2801 | 0.0226 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema460_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.9388 | 0.6635 | 4.0099 | 0.0144 | 0.3510 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema460_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8066 | 0.6517 | 3.5070 | 0.0122 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema460_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.6056 | 0.6185 | 2.6182 | 0.0091 | 0.2832 | ok | RAN |
| SOLUSDT | 8 | `ema460_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5398 | 0.6080 | 2.4035 | 0.0084 | 0.2784 | ok | RAN |
| ETHUSDT | 8 | `ema460_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2240 | 0.5975 | 1.0849 | 0.0079 | 0.2013 | ok | RAN |
| ETHUSDT | 4 | `ema460_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.1942 | 0.6089 | 1.0034 | 0.0069 | 0.2067 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema460_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema460_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
