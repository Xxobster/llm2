# Autonomy public-indicator hunt gen 604

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T004743Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema515_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0750 | 0.6954 | 4.5245 | 0.0246 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema515_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9842 | 0.6800 | 4.3266 | 0.0232 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema515_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.7752 | 0.6507 | 3.4877 | 0.0120 | 0.3397 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema515_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7740 | 0.6450 | 3.4097 | 0.0119 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema515_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5912 | 0.6207 | 2.5541 | 0.0089 | 0.2759 | ok | RAN |
| SOLUSDT | 4 | `ema515_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5255 | 0.5988 | 2.3376 | 0.0083 | 0.3023 | ok | RAN |
| ETHUSDT | 4 | `ema515_above_at_h` | one_head_filter_pi_star | 154 | 12.7083 | 1.1125 | 0.5909 | 0.5545 | 0.0042 | 0.1883 | ok | RAN |
| ETHUSDT | 8 | `ema515_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.0876 | 0.5813 | 0.4483 | 0.0034 | 0.2062 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema515_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema515_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema515_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema515_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
