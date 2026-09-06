# Autonomy public-indicator hunt gen 596

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T001721Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema505_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0589 | 0.7005 | 4.5044 | 0.0236 | 0.3858 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema505_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.9297 | 0.6810 | 4.3081 | 0.0220 | 0.3667 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema505_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8849 | 0.6617 | 3.7493 | 0.0133 | 0.3433 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema505_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8332 | 0.6533 | 3.5580 | 0.0125 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema505_above_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.5769 | 0.6159 | 2.4425 | 0.0086 | 0.2927 | ok | RAN |
| SOLUSDT | 8 | `ema505_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5215 | 0.6115 | 2.2237 | 0.0082 | 0.2930 | ok | RAN |
| ETHUSDT | 8 | `ema505_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2185 | 0.6013 | 1.0364 | 0.0077 | 0.1962 | ok | RAN |
| ETHUSDT | 4 | `ema505_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1879 | 0.5928 | 0.9339 | 0.0067 | 0.1916 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema505_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema505_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema505_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema505_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
