# Autonomy public-indicator hunt gen 2229

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T161056Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret362_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.2230 | 0.5987 | 1.1048 | 0.0068 | 0.2237 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret362_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2208 | 0.5952 | 1.1974 | 0.0067 | 0.1905 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret362_pos_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.1515 | 0.5797 | 0.7149 | 0.0029 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `ret362_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.0485 | 0.5298 | 0.2634 | 0.0009 | 0.1071 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret362_neg_at_h` | one_head_filter_pi_star | 180 | 14.8162 | 0.9607 | 0.5611 | -0.2325 | -0.0008 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret362_neg_at_h` | one_head_filter_pi_star | 195 | 16.0509 | 0.8880 | 0.5487 | -0.7289 | -0.0024 | 0.1436 | ok | RAN |
| ETHUSDT | 8 | `ret362_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7902 | 0.5309 | -1.3007 | -0.0087 | 0.1082 | ok | RAN |
| ETHUSDT | 4 | `ret362_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 0.7661 | 0.5204 | -1.4810 | -0.0106 | 0.1020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret362_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5942 | 0.2500 | -0.7892 | -0.0361 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret362_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0591 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret362_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret362_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret362_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret362_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
