# Autonomy public-indicator hunt gen 1549

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T072352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret265_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.1912 | 0.7030 | 4.5356 | 0.0266 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret265_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 2.1134 | 0.7025 | 4.1278 | 0.0251 | 0.4051 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret265_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9364 | 0.6737 | 3.8072 | 0.0136 | 0.3526 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret265_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.8374 | 0.6647 | 3.4207 | 0.0128 | 0.3353 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret265_pos_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.6509 | 0.6275 | 2.5578 | 0.0102 | 0.2941 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret265_pos_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.5202 | 0.6242 | 2.2820 | 0.0085 | 0.2848 | ok | RAN |
| ETHUSDT | 4 | `ret265_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1846 | 0.5864 | 0.9635 | 0.0063 | 0.2147 | ok | RAN |
| ETHUSDT | 8 | `ret265_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.1227 | 0.5909 | 0.6354 | 0.0044 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret265_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret265_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret265_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret265_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret265_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret265_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
