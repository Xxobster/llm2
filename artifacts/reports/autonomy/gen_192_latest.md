# Autonomy public-indicator hunt gen 192

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T220244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma85_cross_up` | one_head_filter_pi_star | 16 | 1.5601 | 5.6770 | 0.7500 | 2.5374 | 0.0445 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma85_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9795 | 0.7005 | 4.4463 | 0.0240 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma85_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8879 | 0.6935 | 4.1422 | 0.0225 | 0.3668 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma85_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3158 | 0.6964 | 4.4520 | 0.0194 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma85_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2878 | 0.6923 | 4.3910 | 0.0189 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma85_above_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.4135 | 0.6171 | 1.8640 | 0.0119 | 0.2229 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma85_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2711 | 0.6000 | 1.3232 | 0.0085 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `sma85_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3375 | 0.6000 | 1.7759 | 0.0051 | 0.2571 | ok | RAN |
| SOLUSDT | 4 | `sma85_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3156 | 0.5952 | 1.6846 | 0.0048 | 0.2571 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
