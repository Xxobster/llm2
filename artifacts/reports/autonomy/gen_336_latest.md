# Autonomy public-indicator hunt gen 336

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T121427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma440_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9986 | 0.6990 | 4.3967 | 0.0228 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma440_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9426 | 0.6935 | 4.3633 | 0.0224 | 0.3769 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma440_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.0146 | 0.6816 | 3.9178 | 0.0146 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma440_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.8510 | 0.6685 | 3.4741 | 0.0126 | 0.3536 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma440_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5294 | 0.6042 | 2.4783 | 0.0083 | 0.2604 | ok | RAN |
| ETHUSDT | 8 | `sma440_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2240 | 0.5978 | 1.1447 | 0.0080 | 0.2228 | ok | RAN |
| ETHUSDT | 4 | `sma440_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2276 | 0.6010 | 1.2249 | 0.0080 | 0.2176 | ok | RAN |
| SOLUSDT | 4 | `sma440_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4693 | 0.6041 | 2.2579 | 0.0078 | 0.2741 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
