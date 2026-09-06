# Autonomy public-indicator hunt gen 724

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T085448Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema665_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.1552 | 0.6919 | 4.6553 | 0.0246 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema665_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9226 | 0.6784 | 4.0171 | 0.0212 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema665_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8410 | 0.6580 | 3.8742 | 0.0126 | 0.3203 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema665_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 1.7584 | 0.6574 | 3.4712 | 0.0119 | 0.3102 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema665_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.6217 | 0.6288 | 2.3194 | 0.0097 | 0.3333 | ok | RAN |
| ETHUSDT | 8 | `ema665_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2603 | 0.6144 | 1.1850 | 0.0091 | 0.2092 | ok | RAN |
| SOLUSDT | 4 | `ema665_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.5703 | 0.6320 | 2.1478 | 0.0087 | 0.3280 | ok | RAN |
| ETHUSDT | 4 | `ema665_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1994 | 0.5988 | 0.9554 | 0.0070 | 0.2037 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema665_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0385 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema665_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
