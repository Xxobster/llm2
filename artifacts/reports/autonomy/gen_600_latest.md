# Autonomy public-indicator hunt gen 600

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T003205Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1100_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0240 | 0.6853 | 4.1510 | 0.0228 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1100_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8814 | 0.6700 | 3.7584 | 0.0199 | 0.3695 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1100_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.7512 | 0.6371 | 3.5781 | 0.0116 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1100_below_at_h` | one_head_filter_pi_star | 251 | 20.4193 | 1.7234 | 0.6414 | 3.5634 | 0.0114 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1100_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.7886 | 0.6581 | 2.4821 | 0.0107 | 0.3248 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1100_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.6712 | 0.6581 | 2.2285 | 0.0098 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1100_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2191 | 0.5745 | 0.9849 | 0.0085 | 0.2057 | ok | RAN |
| ETHUSDT | 4 | `sma1100_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.0781 | 0.5663 | 0.3944 | 0.0030 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
