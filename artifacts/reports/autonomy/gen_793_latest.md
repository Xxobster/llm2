# Autonomy public-indicator hunt gen 793

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T150127Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1540_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.6423 | 0.6495 | 3.7258 | 0.0164 | 0.3248 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1540_below_at_h` | one_head_filter_pi_star | 330 | 26.9580 | 1.5612 | 0.6424 | 3.4841 | 0.0153 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1540_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.7249 | 0.6350 | 3.7714 | 0.0118 | 0.3232 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1540_above_at_h` | one_head_filter_pi_star | 70 | 5.9565 | 1.3005 | 0.6000 | 0.9190 | 0.0117 | 0.2429 | ok | RAN |
| SOLUSDT | 8 | `ema1540_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.6710 | 0.6380 | 3.6436 | 0.0110 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1540_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.7688 | 0.6792 | 2.4442 | 0.0107 | 0.2547 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1540_above_at_h` | one_head_filter_pi_star | 98 | 8.0548 | 1.5669 | 0.6531 | 1.8453 | 0.0087 | 0.2755 | ok | RAN |
| ETHUSDT | 4 | `ema1540_above_at_h` | one_head_filter_pi_star | 44 | 3.8694 | 1.1020 | 0.5682 | 0.2662 | 0.0040 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1540_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1540_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
