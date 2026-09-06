# Autonomy public-indicator hunt gen 1340

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T000442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema949_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7937 | 0.6622 | 3.6625 | 0.0190 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema949_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.7582 | 0.6507 | 3.5969 | 0.0181 | 0.3406 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema949_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.7589 | 0.6486 | 3.8562 | 0.0120 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema949_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.7310 | 0.6429 | 3.5312 | 0.0116 | 0.3025 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema949_above_at_h` | one_head_filter_pi_star | 147 | 12.1306 | 1.3166 | 0.6122 | 1.4843 | 0.0113 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `ema949_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.7454 | 0.6364 | 2.5929 | 0.0106 | 0.3106 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema949_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.2197 | 0.5909 | 0.9742 | 0.0084 | 0.2273 | ok | RAN |
| SOLUSDT | 8 | `ema949_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.5414 | 0.6303 | 1.9767 | 0.0083 | 0.3193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema949_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema949_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema949_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema949_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema949_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema949_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
