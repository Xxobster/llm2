# Autonomy public-indicator hunt gen 1099

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T230023Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma611_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.1112 | 0.7016 | 4.6314 | 0.0250 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma611_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0598 | 0.6865 | 4.4041 | 0.0244 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma611_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8607 | 0.6716 | 3.7578 | 0.0126 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma611_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.7842 | 0.6631 | 3.3815 | 0.0123 | 0.3262 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma611_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.2739 | 0.6111 | 1.2471 | 0.0097 | 0.2292 | ok | RAN |
| SOLUSDT | 4 | `sma611_above_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.6002 | 0.6159 | 2.5251 | 0.0093 | 0.3171 | ok | RAN |
| SOLUSDT | 8 | `sma611_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5788 | 0.6170 | 2.2829 | 0.0091 | 0.3262 | ok | RAN |
| ETHUSDT | 4 | `sma611_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1032 | 0.5864 | 0.5305 | 0.0039 | 0.2037 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma611_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma611_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma611_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma611_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma611_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma611_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
