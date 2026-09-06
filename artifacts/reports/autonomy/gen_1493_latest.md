# Autonomy public-indicator hunt gen 1493

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T020920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret257_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.2349 | 0.7083 | 4.5100 | 0.0273 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret257_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.9626 | 0.6868 | 4.2317 | 0.0239 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret257_neg_at_h` | one_head_filter_pi_star | 165 | 13.5815 | 2.0621 | 0.6848 | 3.9435 | 0.0153 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret257_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8487 | 0.6531 | 3.6730 | 0.0132 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret257_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2286 | 0.5956 | 1.1080 | 0.0077 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `ret257_pos_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.4641 | 0.6199 | 2.0776 | 0.0075 | 0.2807 | ok | RAN |
| SOLUSDT | 4 | `ret257_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4595 | 0.6031 | 2.2160 | 0.0071 | 0.2732 | ok | RAN |
| ETHUSDT | 8 | `ret257_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.1805 | 0.6000 | 0.9082 | 0.0063 | 0.2171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret257_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0385 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret257_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret257_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret257_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret257_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret257_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
