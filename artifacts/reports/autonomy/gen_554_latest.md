# Autonomy public-indicator hunt gen 554

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T213040Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret408_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.6316 | 0.7235 | 5.3465 | 0.0309 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret408_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.2234 | 0.7095 | 4.5166 | 0.0267 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret408_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.8240 | 0.6744 | 3.2929 | 0.0129 | 0.3547 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret408_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.7916 | 0.6778 | 3.2869 | 0.0119 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret408_pos_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.7585 | 0.6389 | 3.1996 | 0.0118 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret408_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.4853 | 0.5949 | 2.0727 | 0.0082 | 0.3101 | ok | RAN |
| ETHUSDT | 8 | `ret408_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1474 | 0.5906 | 0.7636 | 0.0055 | 0.2105 | ok | RAN |
| ETHUSDT | 4 | `ret408_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.0539 | 0.5783 | 0.2841 | 0.0021 | 0.2169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret408_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7388 | 0.2778 | -0.4910 | -0.0212 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret408_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret408_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret408_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret408_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret408_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
