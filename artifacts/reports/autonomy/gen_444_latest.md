# Autonomy public-indicator hunt gen 444

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T125418Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema315_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9946 | 0.6895 | 4.3622 | 0.0233 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema315_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8052 | 0.6750 | 3.8162 | 0.0200 | 0.3650 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema315_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9750 | 0.6719 | 3.9495 | 0.0145 | 0.3594 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema315_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8378 | 0.6598 | 3.5953 | 0.0136 | 0.3608 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema315_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2365 | 0.6011 | 1.2344 | 0.0081 | 0.2128 | ok | RAN |
| SOLUSDT | 4 | `ema315_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5028 | 0.6120 | 2.3501 | 0.0077 | 0.2787 | ok | RAN |
| SOLUSDT | 8 | `ema315_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4783 | 0.6133 | 2.2784 | 0.0074 | 0.2707 | ok | RAN |
| ETHUSDT | 4 | `ema315_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.1634 | 0.5902 | 0.8773 | 0.0058 | 0.2131 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema315_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema315_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema315_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema315_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
