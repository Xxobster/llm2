# Autonomy public-indicator hunt gen 425

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T080427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema620_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.9619 | 0.6743 | 4.4462 | 0.0224 | 0.3578 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema620_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9650 | 0.6802 | 4.0548 | 0.0218 | 0.3909 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema620_below_at_h` | one_head_filter_pi_star | 223 | 18.2349 | 1.8648 | 0.6682 | 3.8771 | 0.0129 | 0.3229 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema620_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.7295 | 0.6490 | 3.3079 | 0.0118 | 0.3269 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema620_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2837 | 0.6135 | 1.2764 | 0.0097 | 0.2086 | ok | RAN |
| SOLUSDT | 8 | `ema620_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5829 | 0.6250 | 2.3086 | 0.0090 | 0.3125 | ok | RAN |
| SOLUSDT | 4 | `ema620_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.5587 | 0.6190 | 2.0769 | 0.0086 | 0.3413 | ok | RAN |
| ETHUSDT | 8 | `ema620_above_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.2234 | 0.6133 | 1.0505 | 0.0079 | 0.1933 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema620_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
