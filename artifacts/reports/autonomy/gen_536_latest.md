# Autonomy public-indicator hunt gen 536

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T202017Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma940_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.2079 | 0.7062 | 4.4622 | 0.0246 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma940_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.1456 | 0.7011 | 4.4073 | 0.0243 | 0.3908 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma940_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.7884 | 0.6473 | 3.7387 | 0.0125 | 0.3278 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma940_below_at_h` | one_head_filter_pi_star | 232 | 18.9708 | 1.7248 | 0.6466 | 3.5025 | 0.0116 | 0.3233 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma940_above_at_h` | one_head_filter_pi_star | 136 | 11.0895 | 1.7852 | 0.6397 | 2.7944 | 0.0110 | 0.3015 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma940_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.7432 | 0.6555 | 2.5120 | 0.0109 | 0.3361 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma940_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.0313 | 0.5494 | 0.1675 | 0.0013 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `sma940_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.0301 | 0.5550 | 0.1655 | 0.0012 | 0.2042 | ok | RAN |
| BTCUSDT | 4 | `sma940_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma940_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
