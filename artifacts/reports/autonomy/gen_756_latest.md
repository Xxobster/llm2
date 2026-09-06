# Autonomy public-indicator hunt gen 756

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T111506Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema705_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0475 | 0.6881 | 4.3532 | 0.0235 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema705_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0479 | 0.6834 | 4.4460 | 0.0234 | 0.3769 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema705_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8056 | 0.6537 | 3.7278 | 0.0125 | 0.3203 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema705_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.7818 | 0.6604 | 3.5171 | 0.0118 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema705_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2253 | 0.6026 | 1.0642 | 0.0083 | 0.2115 | ok | RAN |
| SOLUSDT | 8 | `ema705_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5096 | 0.6115 | 2.1003 | 0.0081 | 0.3165 | ok | RAN |
| ETHUSDT | 4 | `ema705_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2159 | 0.6013 | 1.0145 | 0.0075 | 0.1962 | ok | RAN |
| SOLUSDT | 4 | `ema705_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.4410 | 0.6172 | 1.7572 | 0.0071 | 0.3359 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema705_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema705_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0467 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
