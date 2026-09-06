# Autonomy public-indicator hunt gen 924

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T040755Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema915_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 2.1872 | 0.6898 | 4.7957 | 0.0242 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema915_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8429 | 0.6681 | 4.0253 | 0.0203 | 0.3445 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema915_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.9156 | 0.6640 | 4.3220 | 0.0134 | 0.3040 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema915_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.8301 | 0.6600 | 3.9762 | 0.0126 | 0.3160 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema915_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.7240 | 0.6412 | 2.5789 | 0.0103 | 0.3130 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema915_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.5381 | 0.6308 | 2.0795 | 0.0084 | 0.3000 | ok | RAN |
| ETHUSDT | 4 | `ema915_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 1.1658 | 0.5923 | 0.7359 | 0.0065 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `ema915_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.1646 | 0.5899 | 0.7760 | 0.0064 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema915_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema915_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema915_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema915_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema915_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema915_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
