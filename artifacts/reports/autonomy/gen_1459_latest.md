# Autonomy public-indicator hunt gen 1459

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T224613Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma668_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0591 | 0.6825 | 4.4429 | 0.0240 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma668_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9405 | 0.6800 | 4.1295 | 0.0226 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma668_below_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 1.7882 | 0.6589 | 3.5338 | 0.0119 | 0.3084 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma668_below_at_h` | one_head_filter_pi_star | 217 | 17.6534 | 1.6786 | 0.6498 | 3.1957 | 0.0108 | 0.3041 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma668_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.4625 | 0.5985 | 1.8877 | 0.0074 | 0.3066 | ok | RAN |
| ETHUSDT | 8 | `sma668_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.2025 | 0.6115 | 0.9582 | 0.0074 | 0.2374 | ok | RAN |
| ETHUSDT | 4 | `sma668_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2049 | 0.5951 | 1.0383 | 0.0074 | 0.2025 | ok | RAN |
| SOLUSDT | 8 | `sma668_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.4243 | 0.6031 | 1.7770 | 0.0070 | 0.3206 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma668_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma668_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma668_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma668_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma668_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma668_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
