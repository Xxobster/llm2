# Autonomy public-indicator hunt gen 464

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T153453Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma760_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.1836 | 0.6943 | 4.5970 | 0.0249 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma760_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.1220 | 0.6936 | 4.4201 | 0.0236 | 0.3931 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma760_below_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.7430 | 0.6545 | 3.4347 | 0.0117 | 0.3136 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma760_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.7210 | 0.6505 | 3.2803 | 0.0115 | 0.3058 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma760_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.6255 | 0.6198 | 2.1990 | 0.0096 | 0.3058 | ok | RAN |
| ETHUSDT | 4 | `sma760_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.2151 | 0.5986 | 0.9891 | 0.0078 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `sma760_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.4274 | 0.5954 | 1.7122 | 0.0072 | 0.3053 | ok | RAN |
| ETHUSDT | 8 | `sma760_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1017 | 0.5767 | 0.5052 | 0.0039 | 0.2270 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0446 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma760_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
