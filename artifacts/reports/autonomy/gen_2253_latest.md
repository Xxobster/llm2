# Autonomy public-indicator hunt gen 2253

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T190103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret365_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2356 | 0.5952 | 1.2465 | 0.0069 | 0.1905 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret365_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.0727 | 0.5767 | 0.4143 | 0.0023 | 0.1902 | ok | RAN |
| SOLUSDT | 8 | `ret365_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.0784 | 0.5509 | 0.4162 | 0.0015 | 0.1138 | ok | RAN |
| SOLUSDT | 4 | `ret365_pos_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.0511 | 0.5467 | 0.2593 | 0.0010 | 0.1133 | ok | RAN |
| SOLUSDT | 8 | `ret365_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.0158 | 0.5691 | 0.0957 | 0.0003 | 0.1489 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret365_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9419 | 0.5572 | -0.3725 | -0.0012 | 0.1493 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret365_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 0.8483 | 0.5621 | -0.8290 | -0.0067 | 0.0947 | ok | RAN |
| ETHUSDT | 4 | `ret365_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7618 | 0.5340 | -1.5034 | -0.0103 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret365_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret365_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0625 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret365_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret365_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret365_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret365_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
