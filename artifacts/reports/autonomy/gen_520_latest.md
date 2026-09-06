# Autonomy public-indicator hunt gen 520

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T191506Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma900_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.1289 | 0.7020 | 4.4476 | 0.0246 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma900_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1150 | 0.6989 | 4.1613 | 0.0237 | 0.3920 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma900_below_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.7893 | 0.6522 | 3.7046 | 0.0125 | 0.3174 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma900_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.7087 | 0.6391 | 2.5655 | 0.0108 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma900_below_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.6504 | 0.6455 | 3.1283 | 0.0105 | 0.3000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma900_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5652 | 0.6096 | 2.2732 | 0.0090 | 0.3082 | ok | RAN |
| ETHUSDT | 8 | `sma900_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1769 | 0.5783 | 0.8321 | 0.0067 | 0.1988 | ok | RAN |
| ETHUSDT | 4 | `sma900_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.1239 | 0.5740 | 0.6186 | 0.0049 | 0.2130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma900_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma900_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
