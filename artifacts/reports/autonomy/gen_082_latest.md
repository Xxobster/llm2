# Autonomy public-indicator hunt gen 082

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T145449Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `brk_any_low` | one_head_filter_pi_star | 200 | 16.3382 | 1.7859 | 0.6750 | 3.5013 | 0.0202 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `brk_any_low` | one_head_filter_pi_star | 213 | 17.4002 | 1.7854 | 0.6761 | 3.6875 | 0.0200 | 0.3803 | EBR>35% | RAN |
| SOLUSDT | 8 | `brk_any_low` | one_head_filter_pi_star | 162 | 13.2469 | 2.2309 | 0.6975 | 4.1130 | 0.0183 | 0.4259 | EBR>35% | RAN |
| SOLUSDT | 4 | `brk_any_low` | one_head_filter_pi_star | 159 | 13.0016 | 2.2092 | 0.6981 | 4.1177 | 0.0180 | 0.4277 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `brk_any_high` | one_head_filter_pi_star | 146 | 12.0481 | 1.2924 | 0.6027 | 1.2660 | 0.0089 | 0.1986 | ok | RAN |
| ETHUSDT | 8 | `brk_any_high` | one_head_filter_pi_star | 154 | 12.7083 | 1.2706 | 0.5909 | 1.1844 | 0.0082 | 0.2078 | ok | RAN |
| SOLUSDT | 4 | `brk_any_high` | one_head_filter_pi_star | 202 | 16.4712 | 1.2857 | 0.5842 | 1.5697 | 0.0045 | 0.2525 | ok | RAN |
| SOLUSDT | 8 | `brk_any_high` | one_head_filter_pi_star | 208 | 16.9604 | 1.2853 | 0.5817 | 1.5874 | 0.0044 | 0.2452 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `brk_any_high` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `brk_any_high` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `brk_any_low` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `brk_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `brk_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `brk_any_low` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
