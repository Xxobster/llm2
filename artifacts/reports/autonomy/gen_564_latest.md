# Autonomy public-indicator hunt gen 564

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T220937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema465_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1099 | 0.7037 | 4.6249 | 0.0242 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema465_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9506 | 0.6780 | 4.2639 | 0.0227 | 0.3659 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema465_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.7771 | 0.6557 | 3.4638 | 0.0121 | 0.3396 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema465_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7793 | 0.6485 | 3.3981 | 0.0118 | 0.3366 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema465_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.6741 | 0.6221 | 2.8472 | 0.0101 | 0.2791 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema465_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.6042 | 0.6193 | 2.6232 | 0.0092 | 0.2727 | ok | RAN |
| ETHUSDT | 4 | `ema465_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1999 | 0.6000 | 0.9989 | 0.0072 | 0.1938 | ok | RAN |
| ETHUSDT | 8 | `ema465_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.1278 | 0.5976 | 0.6593 | 0.0048 | 0.2130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema465_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema465_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema465_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema465_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema465_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema465_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
