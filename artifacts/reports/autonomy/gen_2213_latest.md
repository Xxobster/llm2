# Autonomy public-indicator hunt gen 2213

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T141223Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret359_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2747 | 0.6024 | 1.3958 | 0.0081 | 0.2048 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret359_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.2159 | 0.6013 | 1.1654 | 0.0069 | 0.2089 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret359_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.2124 | 0.5750 | 1.0330 | 0.0038 | 0.1187 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret359_pos_at_h` | one_head_filter_pi_star | 151 | 12.3126 | 1.1526 | 0.5629 | 0.7449 | 0.0028 | 0.1258 | ok | RAN |
| SOLUSDT | 4 | `ret359_neg_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.0263 | 0.5680 | 0.1651 | 0.0006 | 0.1359 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret359_neg_at_h` | one_head_filter_pi_star | 181 | 14.8985 | 0.9743 | 0.5691 | -0.1571 | -0.0005 | 0.1381 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret359_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7655 | 0.5309 | -1.4876 | -0.0101 | 0.1031 | ok | RAN |
| ETHUSDT | 4 | `ret359_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7331 | 0.5249 | -1.6517 | -0.0126 | 0.1050 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret359_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0607 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret359_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0679 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret359_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret359_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret359_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret359_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
