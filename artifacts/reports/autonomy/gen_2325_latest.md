# Autonomy public-indicator hunt gen 2325

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T034054Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret375_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2329 | 0.5915 | 1.2037 | 0.0066 | 0.1829 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret375_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1584 | 0.5847 | 0.9301 | 0.0047 | 0.1694 | ok | RAN |
| SOLUSDT | 4 | `ret375_pos_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.0463 | 0.5390 | 0.2378 | 0.0009 | 0.0974 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret375_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0034 | 0.5211 | 0.0176 | 0.0001 | 0.1056 | ok | RAN |
| SOLUSDT | 8 | `ret375_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9890 | 0.5784 | -0.0673 | -0.0002 | 0.1471 | ok | RAN |
| SOLUSDT | 4 | `ret375_neg_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9326 | 0.5415 | -0.4373 | -0.0014 | 0.1463 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret375_pos_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 0.8607 | 0.5567 | -0.8594 | -0.0058 | 0.1084 | ok | RAN |
| ETHUSDT | 8 | `ret375_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7912 | 0.5414 | -1.2872 | -0.0087 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret375_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5901 | 0.2353 | -0.8024 | -0.0327 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret375_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret375_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret375_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret375_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret375_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
