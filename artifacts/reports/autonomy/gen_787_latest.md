# Autonomy public-indicator hunt gen 787

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T142832Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma496_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0929 | 0.6949 | 4.4860 | 0.0250 | 0.3898 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma496_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0149 | 0.6842 | 4.4101 | 0.0229 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma496_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.8879 | 0.6684 | 3.6933 | 0.0129 | 0.3422 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma496_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.8690 | 0.6703 | 3.6549 | 0.0127 | 0.3514 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma496_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.3055 | 0.6093 | 1.3813 | 0.0109 | 0.2119 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma496_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2719 | 0.6023 | 1.3769 | 0.0098 | 0.2159 | ok | RAN |
| SOLUSDT | 4 | `sma496_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5863 | 0.6207 | 2.5310 | 0.0091 | 0.2874 | ok | RAN |
| SOLUSDT | 8 | `sma496_above_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.5027 | 0.6127 | 2.2690 | 0.0082 | 0.2832 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma496_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma496_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma496_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma496_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
