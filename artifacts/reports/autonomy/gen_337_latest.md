# Autonomy public-indicator hunt gen 337

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T123008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema400_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.9947 | 0.6845 | 4.4348 | 0.0236 | 0.3544 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema400_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8907 | 0.6859 | 4.0868 | 0.0219 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema400_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.9223 | 0.6667 | 3.9407 | 0.0138 | 0.3575 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema400_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.8966 | 0.6618 | 3.8725 | 0.0134 | 0.3430 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema400_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2680 | 0.6154 | 1.3500 | 0.0092 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `ema400_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5422 | 0.6154 | 2.5005 | 0.0085 | 0.2692 | ok | RAN |
| SOLUSDT | 8 | `ema400_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5246 | 0.6080 | 2.3711 | 0.0081 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `ema400_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2081 | 0.6023 | 1.0230 | 0.0074 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
