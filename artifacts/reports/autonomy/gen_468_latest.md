# Autonomy public-indicator hunt gen 468

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T155022Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema345_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0270 | 0.6923 | 4.4242 | 0.0235 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema345_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9314 | 0.6839 | 4.1334 | 0.0224 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema345_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9212 | 0.6684 | 3.7872 | 0.0138 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema345_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8637 | 0.6599 | 3.7143 | 0.0132 | 0.3553 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema345_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5669 | 0.6250 | 2.6033 | 0.0087 | 0.2609 | ok | RAN |
| ETHUSDT | 8 | `ema345_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2218 | 0.6089 | 1.1532 | 0.0078 | 0.2235 | ok | RAN |
| SOLUSDT | 8 | `ema345_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4829 | 0.6054 | 2.3303 | 0.0076 | 0.2649 | ok | RAN |
| ETHUSDT | 4 | `ema345_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.1438 | 0.5989 | 0.7699 | 0.0051 | 0.2033 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema345_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema345_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema345_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema345_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
