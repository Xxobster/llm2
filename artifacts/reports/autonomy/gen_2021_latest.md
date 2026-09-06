# Autonomy public-indicator hunt gen 2021

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T113512Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret332_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2838 | 0.6163 | 1.5715 | 0.0084 | 0.1919 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret332_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.2590 | 0.5956 | 1.4629 | 0.0074 | 0.1803 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret332_pos_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1809 | 0.5576 | 0.9016 | 0.0032 | 0.1212 | ok | RAN |
| SOLUSDT | 4 | `ret332_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.1699 | 0.5581 | 0.8635 | 0.0030 | 0.1047 | ok | RAN |
| SOLUSDT | 8 | `ret332_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0326 | 0.5771 | 0.1823 | 0.0006 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret332_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9825 | 0.5635 | -0.1085 | -0.0004 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret332_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.8077 | 0.5367 | -1.1296 | -0.0080 | 0.0960 | ok | RAN |
| ETHUSDT | 8 | `ret332_pos_at_h` | one_head_filter_pi_star | 164 | 13.5526 | 0.7841 | 0.5366 | -1.2654 | -0.0092 | 0.0976 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret332_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret332_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0768 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret332_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret332_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret332_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret332_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
