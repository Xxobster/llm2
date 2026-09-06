# Autonomy public-indicator hunt gen 732

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T092945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema675_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.1548 | 0.6935 | 4.5497 | 0.0248 | 0.3819 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema675_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 1.9124 | 0.6812 | 4.0094 | 0.0214 | 0.3768 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema675_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.8438 | 0.6667 | 3.7174 | 0.0125 | 0.3192 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema675_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.7926 | 0.6553 | 3.5140 | 0.0122 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema675_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.7611 | 0.6345 | 2.8214 | 0.0108 | 0.3172 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema675_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.6928 | 0.6562 | 2.5030 | 0.0105 | 0.3359 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema675_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2148 | 0.5988 | 1.0194 | 0.0076 | 0.1975 | ok | RAN |
| ETHUSDT | 8 | `ema675_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.1905 | 0.6037 | 0.9223 | 0.0069 | 0.2012 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema675_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema675_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
