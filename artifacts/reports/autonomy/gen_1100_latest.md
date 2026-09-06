# Autonomy public-indicator hunt gen 1100

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T230717Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema913_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.8763 | 0.6696 | 3.9762 | 0.0208 | 0.3612 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema913_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.7772 | 0.6549 | 3.6570 | 0.0184 | 0.3496 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema913_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.7750 | 0.6488 | 3.7686 | 0.0121 | 0.3058 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema913_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7610 | 0.6502 | 3.7131 | 0.0118 | 0.3004 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema913_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.6833 | 0.6328 | 2.4631 | 0.0099 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema913_above_at_h` | one_head_filter_pi_star | 119 | 9.7814 | 1.5777 | 0.6303 | 2.1587 | 0.0088 | 0.3361 | ok | RAN |
| ETHUSDT | 4 | `ema913_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.1718 | 0.5862 | 0.8114 | 0.0065 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `ema913_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.1684 | 0.5782 | 0.7982 | 0.0063 | 0.2177 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema913_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema913_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema913_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema913_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema913_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema913_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
