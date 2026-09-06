# Autonomy public-indicator hunt gen 560

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T215349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1000_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.0779 | 0.6900 | 4.3520 | 0.0231 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1000_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.8973 | 0.6854 | 3.7950 | 0.0199 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1000_below_at_h` | one_head_filter_pi_star | 232 | 18.9708 | 1.8206 | 0.6552 | 3.7202 | 0.0129 | 0.3276 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1000_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 1.7694 | 0.6533 | 3.5517 | 0.0122 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1000_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.8374 | 0.6538 | 2.8086 | 0.0114 | 0.2923 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1000_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.8079 | 0.6400 | 2.6439 | 0.0103 | 0.3040 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1000_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2580 | 0.5957 | 1.1393 | 0.0096 | 0.2199 | ok | RAN |
| ETHUSDT | 4 | `sma1000_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2061 | 0.5776 | 0.9843 | 0.0075 | 0.2236 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1000_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1000_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
