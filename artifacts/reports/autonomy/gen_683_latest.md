# Autonomy public-indicator hunt gen 683

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T055835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma412_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.2205 | 0.7182 | 4.8698 | 0.0260 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma412_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9598 | 0.6959 | 4.3673 | 0.0225 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma412_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0523 | 0.6684 | 4.1267 | 0.0150 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma412_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8757 | 0.6701 | 3.6879 | 0.0131 | 0.3660 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma412_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5345 | 0.6080 | 2.3891 | 0.0085 | 0.2784 | ok | RAN |
| SOLUSDT | 4 | `sma412_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.5324 | 0.6205 | 2.5201 | 0.0083 | 0.2615 | ok | RAN |
| ETHUSDT | 8 | `sma412_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2257 | 0.5904 | 1.1406 | 0.0078 | 0.2181 | ok | RAN |
| ETHUSDT | 4 | `sma412_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1951 | 0.5956 | 1.0566 | 0.0069 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma412_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma412_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma412_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma412_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
