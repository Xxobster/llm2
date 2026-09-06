# Autonomy public-indicator hunt gen 392

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T002753Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma580_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1277 | 0.6923 | 4.6495 | 0.0248 | 0.3956 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma580_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1137 | 0.7005 | 4.5771 | 0.0247 | 0.4011 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma580_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8509 | 0.6736 | 3.6353 | 0.0125 | 0.3420 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma580_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.7358 | 0.6613 | 3.2222 | 0.0111 | 0.3280 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma580_above_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.6665 | 0.6280 | 2.7138 | 0.0100 | 0.3110 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma580_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.5372 | 0.6024 | 2.3819 | 0.0085 | 0.2952 | ok | RAN |
| ETHUSDT | 8 | `sma580_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2058 | 0.5906 | 1.0354 | 0.0073 | 0.2281 | ok | RAN |
| ETHUSDT | 4 | `sma580_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.1966 | 0.6069 | 0.9961 | 0.0069 | 0.2081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma580_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
