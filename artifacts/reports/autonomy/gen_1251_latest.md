# Autonomy public-indicator hunt gen 1251

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T152654Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma635_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.1145 | 0.6856 | 4.6145 | 0.0248 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma635_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0193 | 0.6906 | 4.2468 | 0.0231 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma635_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.7992 | 0.6617 | 3.4734 | 0.0120 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma635_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.6536 | 0.6599 | 3.0307 | 0.0107 | 0.3350 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma635_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.5304 | 0.6069 | 2.1780 | 0.0085 | 0.3241 | ok | RAN |
| SOLUSDT | 4 | `sma635_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.5174 | 0.6012 | 2.2066 | 0.0082 | 0.3067 | ok | RAN |
| ETHUSDT | 8 | `sma635_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.1859 | 0.6026 | 0.8993 | 0.0066 | 0.2252 | ok | RAN |
| ETHUSDT | 4 | `sma635_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1655 | 0.5878 | 0.8070 | 0.0061 | 0.2230 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma635_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma635_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
