# Autonomy public-indicator hunt gen 891

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T003137Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma582_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1787 | 0.7056 | 4.6755 | 0.0259 | 0.4056 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma582_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.1090 | 0.6902 | 4.5700 | 0.0255 | 0.4022 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma582_below_at_h` | one_head_filter_pi_star | 210 | 17.0839 | 1.9113 | 0.6714 | 3.9909 | 0.0132 | 0.3286 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma582_above_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 1.3597 | 0.6164 | 1.6098 | 0.0122 | 0.2192 | ok | RAN |
| SOLUSDT | 8 | `sma582_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7877 | 0.6736 | 3.4876 | 0.0120 | 0.3420 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma582_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.6000 | 0.6207 | 2.3197 | 0.0092 | 0.2966 | ok | RAN |
| ETHUSDT | 8 | `sma582_above_at_h` | one_head_filter_pi_star | 144 | 11.8831 | 1.2520 | 0.6111 | 1.1812 | 0.0088 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `sma582_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.5442 | 0.6267 | 2.2629 | 0.0086 | 0.3000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma582_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma582_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma582_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma582_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma582_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma582_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
