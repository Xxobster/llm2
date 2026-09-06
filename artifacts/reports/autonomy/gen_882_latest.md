# Autonomy public-indicator hunt gen 882

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T233731Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret736_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0518 | 0.6882 | 4.0669 | 0.0217 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret736_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.9786 | 0.6839 | 3.5613 | 0.0200 | 0.3806 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret736_neg_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.8707 | 0.6565 | 3.8073 | 0.0140 | 0.3348 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret736_neg_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.8890 | 0.6618 | 3.6161 | 0.0140 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret736_pos_at_h` | one_head_filter_pi_star | 83 | 6.8219 | 1.7443 | 0.6747 | 2.2808 | 0.0102 | 0.3012 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret736_pos_at_h` | one_head_filter_pi_star | 86 | 7.0524 | 1.5627 | 0.6628 | 1.8245 | 0.0084 | 0.3140 | ok | RAN |
| ETHUSDT | 8 | `ret736_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.0996 | 0.5647 | 0.5206 | 0.0041 | 0.2176 | ok | RAN |
| ETHUSDT | 4 | `ret736_pos_at_h` | one_head_filter_pi_star | 178 | 14.5834 | 1.0915 | 0.5618 | 0.4896 | 0.0037 | 0.2135 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret736_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4739 | 0.2778 | -1.1388 | -0.0510 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret736_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5072 | 0.2857 | -0.9902 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret736_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret736_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret736_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret736_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
