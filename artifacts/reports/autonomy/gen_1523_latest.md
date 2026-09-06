# Autonomy public-indicator hunt gen 1523

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T045455Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma677_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9978 | 0.6906 | 4.1279 | 0.0227 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma677_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9297 | 0.6721 | 3.9051 | 0.0223 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma677_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.7651 | 0.6649 | 3.3227 | 0.0123 | 0.3246 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma677_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.7604 | 0.6617 | 3.3977 | 0.0120 | 0.3184 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma677_above_at_h` | one_head_filter_pi_star | 160 | 13.1208 | 1.5220 | 0.6062 | 2.2268 | 0.0082 | 0.3063 | ok | RAN |
| ETHUSDT | 8 | `sma677_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.2199 | 0.6104 | 1.0566 | 0.0080 | 0.2143 | ok | RAN |
| ETHUSDT | 4 | `sma677_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.1885 | 0.6000 | 0.9852 | 0.0070 | 0.2229 | ok | RAN |
| SOLUSDT | 8 | `sma677_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.3955 | 0.6014 | 1.7161 | 0.0066 | 0.3043 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma677_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma677_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma677_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma677_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma677_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma677_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
