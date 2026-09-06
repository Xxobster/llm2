# Autonomy public-indicator hunt gen 736

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T094659Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1440_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.7604 | 0.6531 | 3.7558 | 0.0181 | 0.3347 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1440_below_at_h` | one_head_filter_pi_star | 270 | 22.0565 | 1.7118 | 0.6556 | 3.8436 | 0.0176 | 0.3259 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1440_above_at_h` | one_head_filter_pi_star | 61 | 5.0708 | 1.9436 | 0.6885 | 2.3050 | 0.0134 | 0.2787 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1440_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.7549 | 0.6316 | 4.0203 | 0.0113 | 0.3289 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1440_below_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 1.7222 | 0.6299 | 3.9147 | 0.0108 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1440_above_at_h` | one_head_filter_pi_star | 66 | 5.4864 | 1.4694 | 0.6515 | 1.3253 | 0.0082 | 0.3182 | ok | RAN |
| ETHUSDT | 4 | `sma1440_above_at_h` | one_head_filter_pi_star | 89 | 7.3450 | 1.2070 | 0.5955 | 0.7425 | 0.0079 | 0.2472 | ok | RAN |
| ETHUSDT | 8 | `sma1440_above_at_h` | one_head_filter_pi_star | 94 | 7.7577 | 1.1658 | 0.5745 | 0.6454 | 0.0067 | 0.2021 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1440_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1440_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3380 | 0.2500 | -1.4955 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
