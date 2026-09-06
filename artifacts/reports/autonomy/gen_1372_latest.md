# Autonomy public-indicator hunt gen 1372

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T030334Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema953_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.7799 | 0.6681 | 3.8252 | 0.0187 | 0.3537 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema953_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.7517 | 0.6552 | 3.6537 | 0.0184 | 0.3534 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema953_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.7614 | 0.6429 | 3.6637 | 0.0120 | 0.3109 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema953_above_at_h` | one_head_filter_pi_star | 122 | 10.0274 | 1.7359 | 0.6393 | 2.5864 | 0.0110 | 0.3197 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema953_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.6577 | 0.6375 | 3.4031 | 0.0106 | 0.2988 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema953_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.2681 | 0.6061 | 1.1556 | 0.0099 | 0.2273 | ok | RAN |
| SOLUSDT | 8 | `ema953_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.6331 | 0.6230 | 2.2668 | 0.0091 | 0.3115 | ok | RAN |
| ETHUSDT | 8 | `ema953_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.1977 | 0.5920 | 0.8865 | 0.0074 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema953_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema953_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema953_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema953_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema953_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema953_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
