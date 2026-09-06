# Autonomy public-indicator hunt gen 2413

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T152132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret388_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.2920 | 0.6184 | 1.4594 | 0.0085 | 0.1974 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret388_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.2706 | 0.6125 | 1.3943 | 0.0081 | 0.1938 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret388_pos_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.0977 | 0.5390 | 0.4924 | 0.0018 | 0.0974 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret388_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 0.9851 | 0.5352 | -0.0753 | -0.0003 | 0.1127 | ok | RAN |
| SOLUSDT | 4 | `ret388_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9557 | 0.5665 | -0.2619 | -0.0009 | 0.1618 | ok | RAN |
| SOLUSDT | 8 | `ret388_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9328 | 0.5615 | -0.4155 | -0.0014 | 0.1390 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret388_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8430 | 0.5389 | -0.9666 | -0.0066 | 0.1056 | ok | RAN |
| ETHUSDT | 4 | `ret388_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.8072 | 0.5349 | -1.1716 | -0.0078 | 0.1163 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret388_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5207 | 0.3158 | -1.0568 | -0.0448 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret388_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0681 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret388_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret388_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret388_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret388_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
