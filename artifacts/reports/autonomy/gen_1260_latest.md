# Autonomy public-indicator hunt gen 1260

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T161923Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema937_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.7858 | 0.6652 | 3.7435 | 0.0189 | 0.3478 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema937_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.7286 | 0.6524 | 3.5768 | 0.0179 | 0.3476 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema937_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.7875 | 0.6582 | 3.7589 | 0.0120 | 0.3038 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema937_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.7147 | 0.6443 | 3.6203 | 0.0114 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema937_above_at_h` | one_head_filter_pi_star | 122 | 10.1398 | 1.6238 | 0.6393 | 2.2664 | 0.0094 | 0.3033 | ok | RAN |
| SOLUSDT | 8 | `ema937_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.6440 | 0.6142 | 2.3355 | 0.0094 | 0.3228 | ok | RAN |
| ETHUSDT | 8 | `ema937_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.2519 | 0.6014 | 1.1729 | 0.0091 | 0.2162 | ok | RAN |
| ETHUSDT | 4 | `ema937_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.0595 | 0.5758 | 0.2831 | 0.0025 | 0.2348 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema937_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema937_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0568 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema937_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema937_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema937_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema937_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
