# Autonomy public-indicator hunt gen 1645

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T224131Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret278_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.1538 | 0.6026 | 0.9059 | 0.0048 | 0.2051 | ok | RAN |
| ETHUSDT | 4 | `ret278_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1566 | 0.5964 | 0.9207 | 0.0048 | 0.2048 | ok | RAN |
| SOLUSDT | 8 | `ret278_neg_at_h` | one_head_filter_pi_star | 163 | 13.2604 | 1.0897 | 0.5644 | 0.4749 | 0.0019 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `ret278_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0776 | 0.5538 | 0.4165 | 0.0014 | 0.1075 | ok | RAN |
| SOLUSDT | 8 | `ret278_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.0474 | 0.5549 | 0.2550 | 0.0009 | 0.1098 | ok | RAN |
| SOLUSDT | 4 | `ret278_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 1.0235 | 0.5671 | 0.1320 | 0.0005 | 0.1524 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret278_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8685 | 0.5435 | -0.7824 | -0.0052 | 0.0815 | ok | RAN |
| ETHUSDT | 8 | `ret278_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8033 | 0.5304 | -1.2371 | -0.0080 | 0.0829 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret278_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0659 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret278_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret278_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret278_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret278_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret278_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
