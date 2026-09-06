# Autonomy public-indicator hunt gen 1204

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T103856Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema929_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema929_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 1.7891 | 0.6585 | 3.8624 | 0.0191 | 0.3374 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema929_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 1.7771 | 0.6543 | 3.8393 | 0.0185 | 0.3457 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema929_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.7748 | 0.6459 | 3.8649 | 0.0120 | 0.2996 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema929_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7266 | 0.6392 | 3.6378 | 0.0115 | 0.3059 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema929_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.7696 | 0.6452 | 2.6332 | 0.0105 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema929_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.2525 | 0.6087 | 1.1240 | 0.0095 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `ema929_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.5610 | 0.6212 | 2.1227 | 0.0088 | 0.3182 | ok | RAN |
| ETHUSDT | 4 | `ema929_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.1814 | 0.5896 | 0.8295 | 0.0071 | 0.2239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema929_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema929_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema929_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema929_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema929_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
