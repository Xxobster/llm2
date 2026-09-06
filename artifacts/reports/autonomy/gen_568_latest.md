# Autonomy public-indicator hunt gen 568

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T222506Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1020_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1632 | 0.6968 | 4.4425 | 0.0244 | 0.3936 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1020_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8743 | 0.6782 | 3.8694 | 0.0207 | 0.3564 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1020_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.8491 | 0.6598 | 3.9164 | 0.0131 | 0.3195 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1020_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 1.8043 | 0.6578 | 3.6860 | 0.0128 | 0.3244 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1020_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.6703 | 0.6288 | 2.3816 | 0.0093 | 0.2803 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1020_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.6302 | 0.6308 | 2.2656 | 0.0092 | 0.3231 | ok | RAN |
| ETHUSDT | 4 | `sma1020_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1690 | 0.5732 | 0.7983 | 0.0063 | 0.2102 | ok | RAN |
| ETHUSDT | 8 | `sma1020_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1650 | 0.5743 | 0.7510 | 0.0062 | 0.1959 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1020_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6372 | 0.2941 | -0.6851 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1020_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5901 | 0.2353 | -0.8024 | -0.0346 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
