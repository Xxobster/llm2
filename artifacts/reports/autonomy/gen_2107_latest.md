# Autonomy public-indicator hunt gen 2107

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T230853Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma754_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1648 | 0.5824 | 0.9354 | 0.0047 | 0.1868 | ok | RAN |
| SOLUSDT | 8 | `sma754_above_at_h` | one_head_filter_pi_star | 110 | 9.1429 | 1.2421 | 0.5909 | 0.9369 | 0.0041 | 0.1364 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma754_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.0684 | 0.5657 | 0.4159 | 0.0021 | 0.1771 | ok | RAN |
| SOLUSDT | 4 | `sma754_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0685 | 0.5547 | 0.3317 | 0.0013 | 0.1241 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma754_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9347 | 0.5502 | -0.4105 | -0.0014 | 0.1244 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma754_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9152 | 0.5529 | -0.5447 | -0.0019 | 0.1346 | ok | RAN |
| ETHUSDT | 8 | `sma754_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 0.9036 | 0.5644 | -0.5199 | -0.0038 | 0.1043 | ok | RAN |
| ETHUSDT | 4 | `sma754_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8481 | 0.5548 | -0.7942 | -0.0065 | 0.1096 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma754_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma754_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma754_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma754_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma754_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma754_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
