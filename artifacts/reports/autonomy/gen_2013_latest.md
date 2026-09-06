# Autonomy public-indicator hunt gen 2013

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T104657Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret331_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2594 | 0.5954 | 1.4290 | 0.0075 | 0.1908 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret331_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2245 | 0.5988 | 1.2195 | 0.0067 | 0.1914 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret331_pos_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.2224 | 0.5562 | 1.1112 | 0.0040 | 0.1183 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret331_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.1870 | 0.5562 | 0.9504 | 0.0033 | 0.1124 | ok | RAN |
| SOLUSDT | 4 | `ret331_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0098 | 0.5738 | 0.0575 | 0.0002 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret331_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 0.9620 | 0.5600 | -0.2239 | -0.0008 | 0.1486 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret331_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 0.8092 | 0.5431 | -1.2140 | -0.0080 | 0.1015 | ok | RAN |
| ETHUSDT | 4 | `ret331_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.7717 | 0.5385 | -1.3975 | -0.0094 | 0.1044 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret331_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret331_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret331_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret331_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret331_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret331_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
