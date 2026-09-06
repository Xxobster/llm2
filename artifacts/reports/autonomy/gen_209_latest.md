# Autonomy public-indicator hunt gen 209

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T231015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema85_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9057 | 0.6888 | 4.1161 | 0.0223 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema85_cross_down` | one_head_filter_pi_star | 14 | 1.3802 | 1.5997 | 0.6429 | 0.8224 | 0.0219 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema85_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9016 | 0.6850 | 4.2682 | 0.0218 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema85_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2054 | 0.6890 | 4.1120 | 0.0181 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema85_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2160 | 0.6905 | 4.2065 | 0.0178 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema85_cross_down` | one_head_filter_pi_star | 16 | 1.6273 | 1.9250 | 0.6875 | 1.1865 | 0.0134 | 0.1875 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema85_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2777 | 0.6066 | 1.3290 | 0.0089 | 0.2240 | ok | RAN |
| ETHUSDT | 8 | `ema85_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.1690 | 0.5936 | 0.8552 | 0.0057 | 0.2193 | ok | RAN |
| SOLUSDT | 8 | `ema85_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3450 | 0.5933 | 1.8077 | 0.0052 | 0.2536 | ok | RAN |
| SOLUSDT | 4 | `ema85_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3142 | 0.5885 | 1.6712 | 0.0048 | 0.2536 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
