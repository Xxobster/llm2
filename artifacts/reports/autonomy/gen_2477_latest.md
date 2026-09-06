# Autonomy public-indicator hunt gen 2477

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T224251Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret402_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2002 | 0.5988 | 1.0862 | 0.0061 | 0.1796 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret402_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2069 | 0.6069 | 1.1163 | 0.0061 | 0.1908 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret402_pos_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.0581 | 0.5652 | 0.2804 | 0.0011 | 0.1087 | ok | RAN |
| SOLUSDT | 8 | `ret402_pos_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0261 | 0.5481 | 0.1243 | 0.0005 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret402_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9476 | 0.5538 | -0.3196 | -0.0011 | 0.1436 | ok | RAN |
| SOLUSDT | 4 | `ret402_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9360 | 0.5604 | -0.3805 | -0.0013 | 0.1319 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret402_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8446 | 0.5414 | -0.9711 | -0.0066 | 0.1215 | ok | RAN |
| ETHUSDT | 4 | `ret402_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.7586 | 0.5146 | -1.5148 | -0.0109 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret402_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0581 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret402_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0701 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret402_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret402_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret402_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret402_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
