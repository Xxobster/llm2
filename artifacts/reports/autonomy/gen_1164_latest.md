# Autonomy public-indicator hunt gen 1164

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T064328Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema923_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.8405 | 0.6667 | 3.8849 | 0.0194 | 0.3553 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema923_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7639 | 0.6555 | 3.7132 | 0.0187 | 0.3403 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema923_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.8431 | 0.6532 | 4.0710 | 0.0128 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema923_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.7620 | 0.6529 | 3.6985 | 0.0118 | 0.2975 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema923_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.7021 | 0.6349 | 2.4604 | 0.0104 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema923_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.4590 | 0.6142 | 1.8555 | 0.0073 | 0.3071 | ok | RAN |
| ETHUSDT | 4 | `ema923_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.1591 | 0.5850 | 0.7977 | 0.0062 | 0.2177 | ok | RAN |
| ETHUSDT | 8 | `ema923_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1360 | 0.5779 | 0.6862 | 0.0054 | 0.2208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema923_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema923_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema923_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema923_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema923_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema923_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
