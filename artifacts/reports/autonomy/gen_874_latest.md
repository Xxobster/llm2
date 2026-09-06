# Autonomy public-indicator hunt gen 874

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T224841Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret728_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.2999 | 0.7143 | 4.3285 | 0.0247 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret728_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1638 | 0.7037 | 4.3897 | 0.0236 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret728_neg_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.9426 | 0.6667 | 4.0732 | 0.0146 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret728_neg_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.8266 | 0.6514 | 3.5514 | 0.0129 | 0.3349 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret728_pos_at_h` | one_head_filter_pi_star | 84 | 6.8884 | 1.7805 | 0.6548 | 2.1757 | 0.0112 | 0.2857 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret728_pos_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.2770 | 0.5923 | 1.2319 | 0.0049 | 0.2923 | ok | RAN |
| ETHUSDT | 8 | `ret728_pos_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.0968 | 0.5676 | 0.4840 | 0.0041 | 0.2365 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret728_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.9936 | 0.5407 | -0.0373 | -0.0003 | 0.2209 | ok | RAN |
| BTCUSDT | 4 | `ret728_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4745 | 0.2941 | -1.1358 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret728_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5129 | 0.3125 | -0.9813 | -0.0582 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret728_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret728_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret728_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret728_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
