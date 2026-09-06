# Autonomy public-indicator hunt gen 738

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T095616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret592_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1789 | 0.7045 | 4.5041 | 0.0245 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret592_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0293 | 0.7010 | 4.2525 | 0.0228 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret592_neg_at_h` | one_head_filter_pi_star | 230 | 18.8342 | 1.7847 | 0.6652 | 3.7496 | 0.0127 | 0.3087 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret592_neg_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.7065 | 0.6550 | 3.4659 | 0.0120 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret592_pos_at_h` | one_head_filter_pi_star | 119 | 9.8904 | 1.7124 | 0.6471 | 2.4800 | 0.0107 | 0.3109 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret592_pos_at_h` | one_head_filter_pi_star | 137 | 11.3865 | 1.5029 | 0.5985 | 2.1178 | 0.0076 | 0.2847 | ok | RAN |
| ETHUSDT | 4 | `ret592_pos_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.0868 | 0.5629 | 0.4637 | 0.0036 | 0.2216 | ok | RAN |
| ETHUSDT | 8 | `ret592_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.0744 | 0.5642 | 0.4064 | 0.0030 | 0.2291 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret592_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0421 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret592_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret592_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret592_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret592_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret592_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
