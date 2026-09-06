# Autonomy public-indicator hunt gen 1276

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T175558Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema939_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8493 | 0.6682 | 3.8743 | 0.0196 | 0.3645 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema939_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.7749 | 0.6568 | 3.7480 | 0.0186 | 0.3390 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema939_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.7781 | 0.6532 | 3.8098 | 0.0120 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema939_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7149 | 0.6434 | 3.5107 | 0.0112 | 0.3033 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema939_above_at_h` | one_head_filter_pi_star | 134 | 10.9264 | 1.6322 | 0.6269 | 2.3674 | 0.0091 | 0.3060 | ok | RAN |
| SOLUSDT | 4 | `ema939_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.5393 | 0.6281 | 2.0514 | 0.0086 | 0.3223 | ok | RAN |
| ETHUSDT | 8 | `ema939_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.1462 | 0.5912 | 0.6723 | 0.0056 | 0.2117 | ok | RAN |
| ETHUSDT | 4 | `ema939_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.1136 | 0.5760 | 0.5159 | 0.0044 | 0.2320 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema939_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema939_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema939_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema939_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema939_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema939_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
