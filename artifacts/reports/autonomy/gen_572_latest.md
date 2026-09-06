# Autonomy public-indicator hunt gen 572

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T224105Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema475_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.1210 | 0.6995 | 4.7223 | 0.0247 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema475_below_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.9416 | 0.6682 | 4.3590 | 0.0217 | 0.3555 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema475_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8993 | 0.6650 | 3.8108 | 0.0133 | 0.3498 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema475_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8776 | 0.6618 | 3.7159 | 0.0127 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema475_above_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.6097 | 0.6199 | 2.6511 | 0.0095 | 0.2924 | ok | RAN |
| SOLUSDT | 8 | `ema475_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.5550 | 0.6129 | 2.5490 | 0.0084 | 0.2581 | ok | RAN |
| ETHUSDT | 8 | `ema475_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.2262 | 0.6053 | 1.0785 | 0.0079 | 0.2105 | ok | RAN |
| ETHUSDT | 4 | `ema475_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.1075 | 0.5920 | 0.5598 | 0.0041 | 0.2011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema475_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema475_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema475_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema475_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
