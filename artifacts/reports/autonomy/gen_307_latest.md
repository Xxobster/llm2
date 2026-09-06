# Autonomy public-indicator hunt gen 307

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T055954Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma102_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9767 | 0.6904 | 4.4631 | 0.0235 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma102_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.7053 | 0.6650 | 3.5599 | 0.0189 | 0.3592 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma102_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2655 | 0.6923 | 4.3614 | 0.0185 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma102_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2971 | 0.6977 | 4.4475 | 0.0185 | 0.3953 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma102_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2708 | 0.6077 | 1.3021 | 0.0086 | 0.2320 | ok | RAN |
| ETHUSDT | 4 | `sma102_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2417 | 0.6054 | 1.2064 | 0.0080 | 0.2162 | ok | RAN |
| SOLUSDT | 4 | `sma102_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2709 | 0.5960 | 1.4500 | 0.0042 | 0.2626 | ok | RAN |
| SOLUSDT | 8 | `sma102_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2710 | 0.5825 | 1.4690 | 0.0042 | 0.2573 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma102_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma102_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma102_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma102_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
