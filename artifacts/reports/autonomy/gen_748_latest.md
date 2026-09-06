# Autonomy public-indicator hunt gen 748

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T103951Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema695_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0207 | 0.6862 | 4.3240 | 0.0232 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema695_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0058 | 0.6834 | 4.1465 | 0.0225 | 0.3819 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema695_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.8186 | 0.6638 | 3.7995 | 0.0125 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema695_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.7627 | 0.6544 | 3.4683 | 0.0122 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema695_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.6513 | 0.6434 | 2.4116 | 0.0097 | 0.3333 | ok | RAN |
| ETHUSDT | 4 | `ema695_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2600 | 0.6111 | 1.2072 | 0.0090 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `ema695_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.5229 | 0.6190 | 2.1820 | 0.0084 | 0.3129 | ok | RAN |
| ETHUSDT | 8 | `ema695_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.2175 | 0.6065 | 1.0230 | 0.0076 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema695_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema695_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0415 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
