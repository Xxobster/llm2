# Autonomy public-indicator hunt gen 1236

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T134314Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema933_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 2.0836 | 0.6844 | 4.6757 | 0.0234 | 0.3644 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema933_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.7899 | 0.6652 | 3.7979 | 0.0189 | 0.3522 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema933_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7369 | 0.6454 | 3.6929 | 0.0116 | 0.3068 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema933_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.7338 | 0.6504 | 3.6762 | 0.0116 | 0.3008 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema933_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.2873 | 0.6058 | 1.3215 | 0.0106 | 0.2336 | ok | RAN |
| SOLUSDT | 4 | `ema933_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.7442 | 0.6480 | 2.5562 | 0.0106 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema933_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.5980 | 0.6212 | 2.3034 | 0.0090 | 0.3106 | ok | RAN |
| ETHUSDT | 8 | `ema933_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.2103 | 0.5971 | 0.9690 | 0.0080 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema933_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema933_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema933_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema933_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema933_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema933_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
