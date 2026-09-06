# Autonomy public-indicator hunt gen 906

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T020640Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret760_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.3657 | 0.7143 | 5.0072 | 0.0261 | 0.3651 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret760_neg_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 2.1334 | 0.6991 | 4.7368 | 0.0232 | 0.3451 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret760_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.9795 | 0.6734 | 3.8789 | 0.0155 | 0.3367 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret760_neg_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8953 | 0.6546 | 3.5003 | 0.0143 | 0.3402 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret760_pos_at_h` | one_head_filter_pi_star | 75 | 6.1155 | 1.8287 | 0.6800 | 2.1950 | 0.0112 | 0.2800 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret760_pos_at_h` | one_head_filter_pi_star | 56 | 4.6027 | 1.4062 | 0.6250 | 1.1102 | 0.0062 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `ret760_pos_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.1112 | 0.5479 | 0.5220 | 0.0046 | 0.2192 | ok | RAN |
| ETHUSDT | 8 | `ret760_pos_at_h` | one_head_filter_pi_star | 145 | 11.8797 | 1.0851 | 0.5655 | 0.4096 | 0.0035 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret760_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4684 | 0.2500 | -1.1492 | -0.0588 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret760_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3012 | 0.2353 | -1.6925 | -0.0763 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret760_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret760_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
