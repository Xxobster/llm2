# Autonomy public-indicator hunt gen 524

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T193154Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema415_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1757 | 0.7059 | 4.7740 | 0.0257 | 0.3957 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema415_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 2.0119 | 0.6829 | 4.4401 | 0.0230 | 0.3707 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema415_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8606 | 0.6587 | 3.7600 | 0.0131 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema415_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.8705 | 0.6651 | 3.7783 | 0.0130 | 0.3541 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema415_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2687 | 0.6037 | 1.2920 | 0.0094 | 0.2073 | ok | RAN |
| SOLUSDT | 4 | `ema415_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.6041 | 0.6230 | 2.7556 | 0.0094 | 0.2787 | ok | RAN |
| SOLUSDT | 8 | `ema415_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4541 | 0.6067 | 2.1431 | 0.0072 | 0.2697 | ok | RAN |
| ETHUSDT | 8 | `ema415_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1692 | 0.5901 | 0.8472 | 0.0060 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema415_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema415_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema415_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema415_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema415_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema415_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
