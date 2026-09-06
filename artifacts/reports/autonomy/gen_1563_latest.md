# Autonomy public-indicator hunt gen 1563

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T165042Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma683_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.3714 | 0.7174 | 5.1316 | 0.0280 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma683_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1158 | 0.6906 | 4.4608 | 0.0240 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma683_below_at_h` | one_head_filter_pi_star | 217 | 17.6534 | 1.8388 | 0.6682 | 3.7318 | 0.0127 | 0.3041 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma683_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.6774 | 0.6582 | 3.0918 | 0.0111 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma683_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.5370 | 0.6129 | 2.2558 | 0.0086 | 0.3161 | ok | RAN |
| ETHUSDT | 4 | `sma683_above_at_h` | one_head_filter_pi_star | 131 | 10.8103 | 1.2132 | 0.5878 | 0.9352 | 0.0078 | 0.2214 | ok | RAN |
| SOLUSDT | 8 | `sma683_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.3910 | 0.5942 | 1.6650 | 0.0067 | 0.3188 | ok | RAN |
| ETHUSDT | 8 | `sma683_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1470 | 0.5962 | 0.7160 | 0.0053 | 0.2179 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma683_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma683_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma683_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma683_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma683_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma683_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
