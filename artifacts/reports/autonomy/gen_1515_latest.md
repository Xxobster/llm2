# Autonomy public-indicator hunt gen 1515

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T041023Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma676_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.1389 | 0.7016 | 4.6509 | 0.0250 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma676_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9766 | 0.6862 | 4.1716 | 0.0227 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma676_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8270 | 0.6736 | 3.5200 | 0.0125 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma676_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.7189 | 0.6650 | 3.2490 | 0.0114 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma676_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.4462 | 0.5899 | 1.8259 | 0.0072 | 0.3237 | ok | RAN |
| SOLUSDT | 8 | `sma676_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.3657 | 0.5852 | 1.5644 | 0.0063 | 0.3185 | ok | RAN |
| ETHUSDT | 4 | `sma676_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.1747 | 0.5890 | 0.8200 | 0.0063 | 0.2123 | ok | RAN |
| ETHUSDT | 8 | `sma676_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1641 | 0.5987 | 0.8144 | 0.0059 | 0.2171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma676_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma676_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma676_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma676_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma676_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma676_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
