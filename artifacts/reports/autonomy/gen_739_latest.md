# Autonomy public-indicator hunt gen 739

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T100045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma454_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0574 | 0.7005 | 4.4788 | 0.0241 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma454_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0523 | 0.6947 | 4.6186 | 0.0237 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma454_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.9565 | 0.6833 | 3.7965 | 0.0139 | 0.3667 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma454_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.8412 | 0.6611 | 3.4968 | 0.0129 | 0.3556 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma454_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.7063 | 0.6310 | 3.0647 | 0.0104 | 0.2781 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma454_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2489 | 0.6062 | 1.2170 | 0.0087 | 0.2062 | ok | RAN |
| SOLUSDT | 4 | `sma454_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5313 | 0.6022 | 2.4122 | 0.0085 | 0.2873 | ok | RAN |
| ETHUSDT | 8 | `sma454_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2077 | 0.5928 | 1.0178 | 0.0073 | 0.2096 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma454_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma454_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma454_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma454_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma454_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma454_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
