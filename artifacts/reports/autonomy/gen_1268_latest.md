# Autonomy public-indicator hunt gen 1268

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T171125Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema938_below_at_h` | one_head_filter_pi_star | 248 | 20.2593 | 1.8455 | 0.6694 | 4.2154 | 0.0205 | 0.3427 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema938_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.7466 | 0.6531 | 3.6750 | 0.0185 | 0.3347 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema938_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.9041 | 0.6652 | 4.1204 | 0.0134 | 0.3176 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema938_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 1.3224 | 0.6077 | 1.3404 | 0.0113 | 0.2231 | ok | RAN |
| SOLUSDT | 4 | `ema938_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.6767 | 0.6342 | 3.4664 | 0.0108 | 0.3035 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema938_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.6108 | 0.6281 | 2.2135 | 0.0090 | 0.3223 | ok | RAN |
| SOLUSDT | 8 | `ema938_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.5509 | 0.6250 | 2.0355 | 0.0085 | 0.3083 | ok | RAN |
| ETHUSDT | 4 | `ema938_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.1707 | 0.5862 | 0.8376 | 0.0065 | 0.2276 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema938_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema938_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema938_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema938_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema938_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema938_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
