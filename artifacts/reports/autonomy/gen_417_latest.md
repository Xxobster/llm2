# Autonomy public-indicator hunt gen 417

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T061244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema600_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8977 | 0.6808 | 4.0869 | 0.0210 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema600_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8216 | 0.6650 | 3.6916 | 0.0194 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema600_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.9648 | 0.6636 | 4.1353 | 0.0135 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema600_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.7967 | 0.6558 | 3.5570 | 0.0121 | 0.3209 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema600_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.5845 | 0.6194 | 2.4440 | 0.0090 | 0.3161 | ok | RAN |
| SOLUSDT | 8 | `ema600_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.5758 | 0.6241 | 2.2452 | 0.0089 | 0.3233 | ok | RAN |
| ETHUSDT | 4 | `ema600_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2329 | 0.6013 | 1.0917 | 0.0083 | 0.2092 | ok | RAN |
| ETHUSDT | 8 | `ema600_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1501 | 0.6000 | 0.7271 | 0.0054 | 0.1871 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
