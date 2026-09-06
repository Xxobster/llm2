# Autonomy public-indicator hunt gen 2181

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T100322Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret355_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2364 | 0.5977 | 1.2971 | 0.0071 | 0.1897 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret355_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.1982 | 0.5901 | 1.0725 | 0.0062 | 0.2112 | ok | RAN |
| SOLUSDT | 8 | `ret355_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.2671 | 0.5848 | 1.3213 | 0.0047 | 0.1111 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret355_pos_at_h` | one_head_filter_pi_star | 158 | 12.8834 | 1.1734 | 0.5696 | 0.8362 | 0.0033 | 0.1139 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret355_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9420 | 0.5517 | -0.3772 | -0.0012 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret355_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.9030 | 0.5445 | -0.5911 | -0.0021 | 0.1361 | ok | RAN |
| ETHUSDT | 8 | `ret355_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 0.7951 | 0.5367 | -1.2317 | -0.0085 | 0.0960 | ok | RAN |
| ETHUSDT | 4 | `ret355_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.7801 | 0.5365 | -1.3624 | -0.0093 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret355_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret355_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0762 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret355_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret355_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret355_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret355_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
