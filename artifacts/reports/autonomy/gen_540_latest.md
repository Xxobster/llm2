# Autonomy public-indicator hunt gen 540

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T203600Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema435_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9852 | 0.6733 | 4.4181 | 0.0224 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema435_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8250 | 0.6716 | 3.9166 | 0.0201 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema435_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.9451 | 0.6650 | 3.9807 | 0.0138 | 0.3495 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema435_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8028 | 0.6520 | 3.5135 | 0.0120 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema435_above_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.2808 | 0.6118 | 1.3697 | 0.0096 | 0.2118 | ok | RAN |
| SOLUSDT | 8 | `ema435_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5549 | 0.6136 | 2.4459 | 0.0086 | 0.2784 | ok | RAN |
| SOLUSDT | 4 | `ema435_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5243 | 0.6087 | 2.4731 | 0.0081 | 0.2663 | ok | RAN |
| ETHUSDT | 8 | `ema435_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2124 | 0.6048 | 1.0627 | 0.0073 | 0.2036 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema435_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema435_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema435_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema435_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema435_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema435_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
