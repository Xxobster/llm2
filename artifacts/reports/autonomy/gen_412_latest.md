# Autonomy public-indicator hunt gen 412

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T050055Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema275_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.9749 | 0.6897 | 4.4621 | 0.0228 | 0.3695 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema275_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9319 | 0.6888 | 4.2400 | 0.0224 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema275_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1534 | 0.6927 | 4.2636 | 0.0163 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema275_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1295 | 0.6862 | 4.3108 | 0.0161 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema275_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2493 | 0.6022 | 1.3058 | 0.0086 | 0.2258 | ok | RAN |
| ETHUSDT | 8 | `ema275_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2316 | 0.6085 | 1.2037 | 0.0080 | 0.2275 | ok | RAN |
| SOLUSDT | 4 | `ema275_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4475 | 0.5959 | 2.2158 | 0.0070 | 0.2591 | ok | RAN |
| SOLUSDT | 8 | `ema275_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3047 | 0.5825 | 1.6140 | 0.0049 | 0.2577 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema275_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema275_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema275_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema275_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema275_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema275_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
