# Autonomy public-indicator hunt gen 489

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T171211Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema780_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0697 | 0.6919 | 4.2544 | 0.0233 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema780_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.9170 | 0.6761 | 4.2414 | 0.0212 | 0.3709 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema780_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.8894 | 0.6612 | 4.0812 | 0.0131 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema780_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.7608 | 0.6606 | 3.4911 | 0.0118 | 0.3257 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema780_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.3172 | 0.6115 | 1.4045 | 0.0114 | 0.2230 | ok | RAN |
| SOLUSDT | 8 | `ema780_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.7042 | 0.6410 | 2.4281 | 0.0103 | 0.3419 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema780_above_at_h` | one_head_filter_pi_star | 137 | 11.1710 | 1.6358 | 0.6277 | 2.4210 | 0.0093 | 0.3285 | ok | RAN |
| ETHUSDT | 4 | `ema780_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.1577 | 0.5862 | 0.7521 | 0.0056 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema780_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema780_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
