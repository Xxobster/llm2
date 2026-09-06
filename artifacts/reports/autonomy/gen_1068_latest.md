# Autonomy public-indicator hunt gen 1068

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T190438Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema909_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.9923 | 0.6854 | 4.1675 | 0.0222 | 0.3662 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema909_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8247 | 0.6639 | 4.0138 | 0.0197 | 0.3487 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema909_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.7674 | 0.6441 | 3.6782 | 0.0118 | 0.3051 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema909_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.7097 | 0.6441 | 3.4930 | 0.0112 | 0.3051 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema909_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.8073 | 0.6480 | 2.6830 | 0.0110 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema909_above_at_h` | one_head_filter_pi_star | 127 | 10.5553 | 1.7125 | 0.6378 | 2.5926 | 0.0106 | 0.3150 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema909_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.2116 | 0.5933 | 0.9993 | 0.0080 | 0.2267 | ok | RAN |
| ETHUSDT | 4 | `ema909_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.2087 | 0.6000 | 0.9254 | 0.0080 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema909_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema909_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema909_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema909_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema909_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema909_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
