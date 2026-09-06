# Autonomy public-indicator hunt gen 1187

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T090413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma626_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1215 | 0.6906 | 4.5785 | 0.0252 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma626_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9149 | 0.6701 | 4.0571 | 0.0221 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma626_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.9420 | 0.6834 | 3.9273 | 0.0139 | 0.3216 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma626_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8059 | 0.6667 | 3.5574 | 0.0124 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma626_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.7103 | 0.6391 | 2.6491 | 0.0104 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma626_above_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.4557 | 0.6014 | 1.8906 | 0.0074 | 0.3077 | ok | RAN |
| ETHUSDT | 4 | `sma626_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1277 | 0.5951 | 0.6552 | 0.0049 | 0.2147 | ok | RAN |
| ETHUSDT | 8 | `sma626_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1311 | 0.5935 | 0.6576 | 0.0048 | 0.2258 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma626_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma626_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma626_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma626_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma626_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma626_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
