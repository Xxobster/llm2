# Autonomy public-indicator hunt gen 962

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T082422Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret816_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0923 | 0.7035 | 4.0859 | 0.0232 | 0.3837 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret816_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9396 | 0.6780 | 4.0132 | 0.0206 | 0.3463 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret816_neg_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8518 | 0.6505 | 3.6037 | 0.0144 | 0.3447 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret816_neg_at_h` | one_head_filter_pi_star | 194 | 16.0951 | 1.8545 | 0.6546 | 3.4723 | 0.0140 | 0.3505 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret816_pos_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.2156 | 0.5680 | 0.9174 | 0.0088 | 0.2320 | ok | RAN |
| SOLUSDT | 8 | `ret816_pos_at_h` | one_head_filter_pi_star | 92 | 7.5017 | 1.4907 | 0.6413 | 1.6128 | 0.0073 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ret816_pos_at_h` | one_head_filter_pi_star | 59 | 4.8493 | 1.4263 | 0.6610 | 1.1682 | 0.0064 | 0.2203 | ok | RAN |
| ETHUSDT | 4 | `ret816_pos_at_h` | one_head_filter_pi_star | 97 | 7.9733 | 1.0896 | 0.5979 | 0.3832 | 0.0044 | 0.2577 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret816_pos_at_h` | one_head_filter_pi_star | 13 | 1.3655 | 0.9607 | 0.4615 | -0.0653 | -0.0032 | 0.0769 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret816_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.8101 | 0.4118 | -0.3412 | -0.0142 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret816_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret816_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret816_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret816_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
