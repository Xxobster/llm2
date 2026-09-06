# Autonomy public-indicator hunt gen 1267

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T170516Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma638_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.1311 | 0.6974 | 4.7313 | 0.0252 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma638_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0440 | 0.6837 | 4.4815 | 0.0237 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma638_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 1.7466 | 0.6618 | 3.4070 | 0.0117 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma638_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.6937 | 0.6555 | 3.1887 | 0.0111 | 0.3254 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma638_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.2465 | 0.6220 | 1.2075 | 0.0088 | 0.2195 | ok | RAN |
| SOLUSDT | 4 | `sma638_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5746 | 0.6115 | 2.3258 | 0.0087 | 0.3185 | ok | RAN |
| SOLUSDT | 8 | `sma638_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.4858 | 0.6014 | 1.9324 | 0.0076 | 0.3188 | ok | RAN |
| ETHUSDT | 4 | `sma638_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.0887 | 0.5890 | 0.4564 | 0.0033 | 0.2086 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma638_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma638_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma638_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma638_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma638_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma638_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
