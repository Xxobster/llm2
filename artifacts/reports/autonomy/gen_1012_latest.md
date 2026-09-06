# Autonomy public-indicator hunt gen 1012

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T115723Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema901_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema901_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.8837 | 0.6609 | 4.0424 | 0.0205 | 0.3391 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema901_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.7502 | 0.6609 | 3.6395 | 0.0186 | 0.3519 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema901_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.7762 | 0.6481 | 3.6453 | 0.0121 | 0.3090 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema901_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.7762 | 0.6569 | 3.7390 | 0.0120 | 0.3054 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema901_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.6015 | 0.6378 | 2.1797 | 0.0088 | 0.3228 | ok | RAN |
| SOLUSDT | 8 | `ema901_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.5367 | 0.6047 | 1.9894 | 0.0082 | 0.3256 | ok | RAN |
| ETHUSDT | 4 | `ema901_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.1670 | 0.5734 | 0.8175 | 0.0065 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `ema901_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.0976 | 0.5828 | 0.4847 | 0.0038 | 0.2185 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema901_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema901_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema901_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema901_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema901_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
