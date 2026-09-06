# Autonomy public-indicator hunt gen 796

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T151842Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema755_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 2.0248 | 0.6847 | 4.1954 | 0.0231 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema755_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9982 | 0.6842 | 4.1279 | 0.0224 | 0.3732 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema755_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.9055 | 0.6624 | 4.0799 | 0.0135 | 0.3207 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema755_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.7787 | 0.6529 | 3.7017 | 0.0121 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema755_above_at_h` | one_head_filter_pi_star | 112 | 9.3086 | 1.7253 | 0.6607 | 2.4443 | 0.0106 | 0.3393 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema755_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.6729 | 0.6391 | 2.4863 | 0.0097 | 0.3233 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema755_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2677 | 0.6047 | 1.3205 | 0.0093 | 0.2035 | ok | RAN |
| ETHUSDT | 4 | `ema755_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.0728 | 0.5823 | 0.3663 | 0.0027 | 0.1899 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema755_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema755_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
