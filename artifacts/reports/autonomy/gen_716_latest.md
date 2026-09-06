# Autonomy public-indicator hunt gen 716

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T082004Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema655_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0461 | 0.6818 | 4.2706 | 0.0230 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema655_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.8764 | 0.6698 | 3.9939 | 0.0210 | 0.3721 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema655_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.8297 | 0.6636 | 3.7377 | 0.0129 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema655_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8125 | 0.6584 | 3.5498 | 0.0128 | 0.3366 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema655_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.6732 | 0.6439 | 2.5130 | 0.0099 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema655_above_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 1.2778 | 0.6096 | 1.2475 | 0.0095 | 0.1986 | ok | RAN |
| SOLUSDT | 8 | `ema655_above_at_h` | one_head_filter_pi_star | 160 | 13.1208 | 1.5921 | 0.6125 | 2.4741 | 0.0093 | 0.3000 | ok | RAN |
| ETHUSDT | 8 | `ema655_above_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.1129 | 0.5948 | 0.5588 | 0.0042 | 0.1830 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema655_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema655_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
