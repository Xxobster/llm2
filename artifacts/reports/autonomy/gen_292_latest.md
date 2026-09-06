# Autonomy public-indicator hunt gen 292

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T045511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema135_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0641 | 0.7010 | 4.7725 | 0.0245 | 0.3660 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema135_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0091 | 0.6931 | 4.5685 | 0.0236 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema135_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2032 | 0.6923 | 4.1903 | 0.0176 | 0.3905 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema135_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2344 | 0.6910 | 4.3794 | 0.0174 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema135_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3610 | 0.5922 | 1.8652 | 0.0055 | 0.2718 | ok | RAN |
| ETHUSDT | 4 | `ema135_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1406 | 0.5907 | 0.7592 | 0.0051 | 0.2228 | ok | RAN |
| ETHUSDT | 8 | `ema135_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.1366 | 0.5855 | 0.7154 | 0.0048 | 0.2280 | ok | RAN |
| SOLUSDT | 4 | `ema135_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3066 | 0.5891 | 1.6093 | 0.0047 | 0.2673 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema135_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema135_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema135_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema135_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
