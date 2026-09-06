# Autonomy public-indicator hunt gen 321

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T074455Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema360_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0163 | 0.6939 | 4.4808 | 0.0235 | 0.3878 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema360_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8484 | 0.6716 | 3.9436 | 0.0207 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema360_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8058 | 0.6548 | 3.5126 | 0.0133 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema360_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8155 | 0.6505 | 3.6045 | 0.0126 | 0.3447 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema360_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2319 | 0.6111 | 1.2036 | 0.0081 | 0.2111 | ok | RAN |
| SOLUSDT | 4 | `ema360_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4825 | 0.6077 | 2.2717 | 0.0078 | 0.2762 | ok | RAN |
| ETHUSDT | 8 | `ema360_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2078 | 0.6126 | 1.0678 | 0.0075 | 0.2199 | ok | RAN |
| SOLUSDT | 8 | `ema360_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.4716 | 0.6056 | 2.2356 | 0.0073 | 0.2722 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema360_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
