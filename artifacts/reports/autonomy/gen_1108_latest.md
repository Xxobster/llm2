# Autonomy public-indicator hunt gen 1108

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T000154Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema914_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8939 | 0.6713 | 3.9466 | 0.0204 | 0.3657 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema914_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.7973 | 0.6624 | 3.8358 | 0.0191 | 0.3376 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema914_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.8535 | 0.6584 | 4.0304 | 0.0129 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema914_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.7058 | 0.6390 | 3.4557 | 0.0110 | 0.3029 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema914_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.5807 | 0.6202 | 2.1880 | 0.0087 | 0.3023 | ok | RAN |
| SOLUSDT | 4 | `ema914_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.5687 | 0.6212 | 2.1194 | 0.0086 | 0.3106 | ok | RAN |
| ETHUSDT | 8 | `ema914_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 1.1563 | 0.5820 | 0.6831 | 0.0060 | 0.2295 | ok | RAN |
| ETHUSDT | 4 | `ema914_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1009 | 0.5797 | 0.4839 | 0.0039 | 0.2101 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema914_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0314 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema914_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema914_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema914_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema914_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema914_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
