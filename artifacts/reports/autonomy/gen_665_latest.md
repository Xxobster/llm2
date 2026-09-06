# Autonomy public-indicator hunt gen 665

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T044430Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1220_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema1220_below_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.7242 | 0.6557 | 3.8345 | 0.0179 | 0.3223 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1220_below_at_h` | one_head_filter_pi_star | 263 | 21.4847 | 1.6572 | 0.6426 | 3.4644 | 0.0162 | 0.3194 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1220_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 1.7004 | 0.6303 | 3.7960 | 0.0113 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1220_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.6250 | 0.6341 | 3.4549 | 0.0103 | 0.3116 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1220_above_at_h` | one_head_filter_pi_star | 109 | 8.9589 | 1.5039 | 0.6330 | 1.8100 | 0.0077 | 0.2936 | ok | RAN |
| SOLUSDT | 8 | `ema1220_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.4611 | 0.6325 | 1.7261 | 0.0073 | 0.2821 | ok | RAN |
| ETHUSDT | 8 | `ema1220_above_at_h` | one_head_filter_pi_star | 86 | 7.0974 | 1.1386 | 0.5698 | 0.5263 | 0.0059 | 0.2209 | ok | RAN |
| ETHUSDT | 4 | `ema1220_above_at_h` | one_head_filter_pi_star | 100 | 8.2528 | 1.0967 | 0.5700 | 0.3944 | 0.0038 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1220_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0295 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1220_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
