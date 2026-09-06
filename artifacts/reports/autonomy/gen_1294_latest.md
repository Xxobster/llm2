# Autonomy public-indicator hunt gen 1294

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T194100Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma715_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0724 | 0.6954 | 4.5972 | 0.0241 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma715_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8432 | 0.6699 | 3.9876 | 0.0203 | 0.3592 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma715_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9379 | 0.6872 | 3.8548 | 0.0136 | 0.3487 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma715_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7969 | 0.6684 | 3.4758 | 0.0122 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma715_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.7330 | 0.6270 | 3.0997 | 0.0108 | 0.2973 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma715_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2403 | 0.6074 | 1.1687 | 0.0085 | 0.2086 | ok | RAN |
| SOLUSDT | 8 | `wma715_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5069 | 0.6077 | 2.3418 | 0.0080 | 0.2818 | ok | RAN |
| ETHUSDT | 4 | `wma715_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1191 | 0.5753 | 0.6497 | 0.0043 | 0.2097 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma715_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma715_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma715_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma715_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma715_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
