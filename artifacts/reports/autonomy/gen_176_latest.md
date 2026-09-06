# Autonomy public-indicator hunt gen 176

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T210146Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma18_cross_down` | one_head_filter_pi_star | 22 | 1.8628 | 4.7478 | 0.8636 | 2.5206 | 0.0215 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma18_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8292 | 0.6847 | 3.9596 | 0.0212 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma18_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7921 | 0.6787 | 3.8248 | 0.0203 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma18_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma18_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1640 | 0.6890 | 3.9888 | 0.0177 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma18_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2454 | 0.5938 | 1.1155 | 0.0078 | 0.2062 | ok | RAN |
| ETHUSDT | 4 | `sma18_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2301 | 0.5951 | 1.0547 | 0.0073 | 0.2025 | ok | RAN |
| SOLUSDT | 8 | `sma18_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3925 | 0.5943 | 2.1074 | 0.0058 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `sma18_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3605 | 0.5896 | 1.9634 | 0.0054 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma18_cross_down` | one_head_filter_pi_star | 16 | 1.4971 | 0.6327 | 0.4375 | -0.7174 | -0.0116 | 0.1250 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma18_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma18_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
