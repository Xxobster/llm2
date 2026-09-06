# Autonomy public-indicator hunt gen 1637

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T213437Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret277_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 1.2869 | 0.6107 | 1.4303 | 0.0079 | 0.1879 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret277_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1047 | 0.5934 | 0.6420 | 0.0033 | 0.1868 | ok | RAN |
| SOLUSDT | 8 | `ret277_pos_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.1225 | 0.5600 | 0.6389 | 0.0022 | 0.1086 | ok | RAN |
| SOLUSDT | 4 | `ret277_neg_at_h` | one_head_filter_pi_star | 150 | 12.2656 | 1.0560 | 0.5533 | 0.2900 | 0.0012 | 0.1467 | ok | RAN |
| SOLUSDT | 4 | `ret277_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0244 | 0.5470 | 0.1305 | 0.0005 | 0.0994 | ok | RAN |
| SOLUSDT | 8 | `ret277_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.0068 | 0.5652 | 0.0391 | 0.0001 | 0.1522 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret277_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8596 | 0.5506 | -0.7865 | -0.0054 | 0.1013 | ok | RAN |
| ETHUSDT | 8 | `ret277_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8240 | 0.5337 | -1.0762 | -0.0072 | 0.0955 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret277_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret277_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4390 | 0.3333 | -1.3058 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret277_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret277_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret277_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret277_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
