# Autonomy public-indicator hunt gen 034

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T114615Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `cmf_cross_up_0` | one_head_filter_pi_star | 36 | 3.0475 | 2.7111 | 0.6667 | 2.3649 | 0.0283 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 4 | `cmf_cross_up_0` | one_head_filter_pi_star | 25 | 2.1728 | 3.0031 | 0.6800 | 2.0196 | 0.0271 | 0.3600 | EBR>35% | RAN |
| ETHUSDT | 4 | `cmf_neg_at_h` | one_head_filter_pi_star | 205 | 16.8579 | 1.8885 | 0.6976 | 3.9856 | 0.0223 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `cmf_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8617 | 0.6959 | 3.9987 | 0.0214 | 0.3733 | EBR>35% | RAN |
| SOLUSDT | 8 | `cmf_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.3710 | 0.7041 | 4.5755 | 0.0197 | 0.4083 | EBR>35% | RAN |
| SOLUSDT | 4 | `cmf_neg_at_h` | one_head_filter_pi_star | 165 | 13.5601 | 2.3823 | 0.7030 | 4.4061 | 0.0194 | 0.4303 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `cmf_pos_at_h` | one_head_filter_pi_star | 172 | 14.0918 | 1.2856 | 0.5930 | 1.3241 | 0.0096 | 0.2209 | ok | RAN |
| SOLUSDT | 8 | `cmf_cross_up_0` | one_head_filter_pi_star | 30 | 2.6219 | 1.4637 | 0.6667 | 0.8810 | 0.0087 | 0.2333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `cmf_cross_up_0` | one_head_filter_pi_star | 21 | 1.8353 | 1.4915 | 0.7143 | 0.7413 | 0.0080 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cmf_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1859 | 0.5901 | 0.8793 | 0.0064 | 0.1988 | ok | RAN |
| SOLUSDT | 8 | `cmf_pos_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3100 | 0.5933 | 1.7133 | 0.0049 | 0.2440 | ok | RAN |
| SOLUSDT | 4 | `cmf_pos_at_h` | one_head_filter_pi_star | 219 | 17.8161 | 1.2968 | 0.5890 | 1.6839 | 0.0047 | 0.2420 | ok | RAN |
| SOLUSDT | 4 | `cmf_cross_down_0` | one_head_filter_pi_star | 27 | 2.2140 | 1.1522 | 0.5556 | 0.3298 | 0.0029 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 8 | `cmf_cross_down_0` | one_head_filter_pi_star | 47 | 3.8540 | 1.1456 | 0.5532 | 0.4335 | 0.0029 | 0.1489 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cmf_cross_down_0` | one_head_filter_pi_star | 43 | 3.5921 | 0.9898 | 0.5581 | -0.0302 | -0.0004 | 0.1628 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cmf_cross_down_0` | one_head_filter_pi_star | 49 | 4.0934 | 0.8828 | 0.5306 | -0.3499 | -0.0041 | 0.2041 | ok | RAN |
| BTCUSDT | 8 | `cmf_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7040 | 0.3500 | -0.6085 | -0.0302 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cmf_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cmf_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cmf_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cmf_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cmf_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `cmf_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cmf_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
