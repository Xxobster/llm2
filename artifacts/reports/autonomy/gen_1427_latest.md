# Autonomy public-indicator hunt gen 1427

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T125727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma663_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0730 | 0.6862 | 4.5152 | 0.0245 | 0.3723 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma663_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.9910 | 0.6816 | 4.1456 | 0.0231 | 0.3966 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma663_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.8080 | 0.6699 | 3.5850 | 0.0122 | 0.3206 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma663_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7404 | 0.6634 | 3.3582 | 0.0118 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma663_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.5671 | 0.6165 | 2.2508 | 0.0092 | 0.3233 | ok | RAN |
| SOLUSDT | 4 | `sma663_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.4536 | 0.5985 | 1.8867 | 0.0074 | 0.3066 | ok | RAN |
| ETHUSDT | 8 | `sma663_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1906 | 0.5969 | 1.0084 | 0.0066 | 0.2094 | ok | RAN |
| ETHUSDT | 4 | `sma663_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1576 | 0.5965 | 0.8187 | 0.0059 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma663_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0409 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma663_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma663_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma663_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma663_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma663_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
