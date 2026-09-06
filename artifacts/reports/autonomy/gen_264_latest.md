# Autonomy public-indicator hunt gen 264

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T025718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma260_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9420 | 0.6898 | 4.2922 | 0.0230 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma260_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8317 | 0.6804 | 3.9744 | 0.0209 | 0.3814 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma260_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1303 | 0.6826 | 3.9641 | 0.0163 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma260_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1379 | 0.6810 | 3.9575 | 0.0162 | 0.3742 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma260_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2017 | 0.5907 | 1.0407 | 0.0070 | 0.2228 | ok | RAN |
| ETHUSDT | 8 | `sma260_above_at_h` | one_head_filter_pi_star | 204 | 16.7685 | 1.1977 | 0.5980 | 1.0730 | 0.0069 | 0.2304 | ok | RAN |
| SOLUSDT | 8 | `sma260_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.4026 | 0.6039 | 2.0819 | 0.0063 | 0.2560 | ok | RAN |
| SOLUSDT | 4 | `sma260_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3664 | 0.5920 | 1.8784 | 0.0057 | 0.2587 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma260_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma260_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
