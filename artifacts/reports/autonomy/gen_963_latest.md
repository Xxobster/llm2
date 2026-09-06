# Autonomy public-indicator hunt gen 963

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T171815Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma642_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1165 | 0.6968 | 4.6060 | 0.0258 | 0.3936 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma642_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0087 | 0.6845 | 4.2913 | 0.0237 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma642_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8130 | 0.6650 | 3.6103 | 0.0125 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma642_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.7100 | 0.6557 | 3.3068 | 0.0114 | 0.3255 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma642_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.5605 | 0.6065 | 2.3315 | 0.0090 | 0.3161 | ok | RAN |
| SOLUSDT | 8 | `sma642_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.5886 | 0.6210 | 2.2671 | 0.0085 | 0.3065 | ok | RAN |
| ETHUSDT | 4 | `sma642_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.2385 | 0.6014 | 1.1189 | 0.0083 | 0.2095 | ok | RAN |
| ETHUSDT | 8 | `sma642_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2052 | 0.6013 | 0.9914 | 0.0075 | 0.2152 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma642_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma642_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma642_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma642_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma642_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma642_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
