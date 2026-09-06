# Autonomy public-indicator hunt gen 1132

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T024645Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema918_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 2.0024 | 0.6909 | 4.5683 | 0.0228 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema918_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7561 | 0.6622 | 3.5562 | 0.0185 | 0.3604 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema918_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.8138 | 0.6553 | 3.7800 | 0.0127 | 0.3106 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema918_above_at_h` | one_head_filter_pi_star | 116 | 9.6411 | 1.8221 | 0.6638 | 2.6167 | 0.0120 | 0.3362 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema918_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7636 | 0.6420 | 3.7130 | 0.0116 | 0.2963 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema918_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.6251 | 0.6202 | 2.3785 | 0.0091 | 0.3101 | ok | RAN |
| ETHUSDT | 4 | `ema918_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1451 | 0.5797 | 0.6800 | 0.0054 | 0.2101 | ok | RAN |
| ETHUSDT | 8 | `ema918_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.1190 | 0.5760 | 0.5442 | 0.0047 | 0.2080 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema918_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema918_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema918_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema918_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema918_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema918_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
