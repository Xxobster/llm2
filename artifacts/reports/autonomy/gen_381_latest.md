# Autonomy public-indicator hunt gen 381

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T215859Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret43_cross_down_0` | one_head_filter_pi_star | 26 | 2.5226 | 1.7236 | 0.6154 | 1.2701 | 0.0260 | 0.1923 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret43_neg_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 1.7878 | 0.6715 | 3.8329 | 0.0212 | 0.3623 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret43_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7629 | 0.6716 | 3.6657 | 0.0201 | 0.3578 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret43_cross_up_0` | one_head_filter_pi_star | 24 | 2.0873 | 2.0934 | 0.6250 | 1.6403 | 0.0178 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret43_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0584 | 0.6855 | 3.7807 | 0.0161 | 0.4025 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret43_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 1.9502 | 0.6730 | 3.5009 | 0.0156 | 0.3899 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret43_cross_down_0` | one_head_filter_pi_star | 35 | 2.9163 | 1.5508 | 0.5429 | 1.0416 | 0.0103 | 0.1143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret43_cross_up_0` | one_head_filter_pi_star | 51 | 4.3595 | 1.2467 | 0.5294 | 0.7144 | 0.0090 | 0.2157 | ok | RAN |
| ETHUSDT | 4 | `ret43_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2815 | 0.6087 | 1.3513 | 0.0088 | 0.2283 | ok | RAN |
| SOLUSDT | 8 | `ret43_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.5815 | 0.6239 | 2.8692 | 0.0079 | 0.2661 | ok | RAN |
| ETHUSDT | 8 | `ret43_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2236 | 0.5967 | 1.1225 | 0.0073 | 0.2376 | ok | RAN |
| SOLUSDT | 4 | `ret43_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.4842 | 0.6127 | 2.4350 | 0.0068 | 0.2598 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret43_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret43_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret43_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret43_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret43_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret43_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret43_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret43_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret43_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret43_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret43_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret43_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
