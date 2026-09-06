# Autonomy public-indicator hunt gen 1941

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T031727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret321_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2567 | 0.5988 | 1.3619 | 0.0077 | 0.1916 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret321_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1108 | 0.5926 | 0.6206 | 0.0034 | 0.1914 | ok | RAN |
| SOLUSDT | 8 | `ret321_pos_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.1833 | 0.5556 | 0.9451 | 0.0033 | 0.0994 | ok | RAN |
| SOLUSDT | 4 | `ret321_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.1253 | 0.5515 | 0.6803 | 0.0023 | 0.1031 | ok | RAN |
| SOLUSDT | 4 | `ret321_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0233 | 0.5754 | 0.1393 | 0.0005 | 0.1397 | ok | RAN |
| SOLUSDT | 8 | `ret321_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0122 | 0.5491 | 0.0728 | 0.0003 | 0.1503 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret321_pos_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8446 | 0.5394 | -0.8912 | -0.0063 | 0.1030 | ok | RAN |
| ETHUSDT | 8 | `ret321_pos_at_h` | one_head_filter_pi_star | 147 | 12.1306 | 0.8132 | 0.5374 | -1.0448 | -0.0079 | 0.0884 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret321_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0625 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret321_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0783 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret321_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret321_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret321_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret321_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
