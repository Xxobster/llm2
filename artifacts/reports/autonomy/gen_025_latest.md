# Autonomy public-indicator hunt gen 025

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T102820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `cmo_cross_up_0` | one_head_filter_pi_star | 21 | 1.8256 | 3.8840 | 0.7619 | 2.3902 | 0.0398 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cmo_cross_down_0` | one_head_filter_pi_star | 13 | 1.0920 | 2.5442 | 0.6154 | 1.3617 | 0.0258 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cmo_cross_up_0` | one_head_filter_pi_star | 28 | 2.3040 | 1.6538 | 0.6786 | 1.1360 | 0.0255 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cmo_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8191 | 0.6816 | 3.9430 | 0.0208 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `cmo_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7603 | 0.6771 | 3.7263 | 0.0199 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `cmo_cross_down_0` | one_head_filter_pi_star | 27 | 2.2300 | 1.6001 | 0.6296 | 0.9886 | 0.0189 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cmo_cross_up_0` | one_head_filter_pi_star | 14 | 1.1938 | 1.4015 | 0.6429 | 0.5479 | 0.0182 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `cmo_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2014 | 0.6970 | 4.0972 | 0.0179 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 8 | `cmo_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1462 | 0.6890 | 3.9427 | 0.0174 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `cmo_cross_down_0` | one_head_filter_pi_star | 19 | 1.5631 | 1.8414 | 0.5789 | 1.1015 | 0.0132 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `cmo_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2562 | 0.5963 | 1.1634 | 0.0080 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `cmo_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2130 | 0.5938 | 0.9751 | 0.0068 | 0.2062 | ok | RAN |
| SOLUSDT | 4 | `cmo_pos_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3797 | 0.5933 | 2.0341 | 0.0056 | 0.2440 | ok | RAN |
| SOLUSDT | 8 | `cmo_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3661 | 0.5924 | 1.9727 | 0.0054 | 0.2370 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `cmo_cross_down_0` | one_head_filter_pi_star | 22 | 1.8098 | 1.0086 | 0.5455 | 0.0167 | 0.0002 | 0.1818 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cmo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `cmo_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `cmo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cmo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cmo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cmo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cmo_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `cmo_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cmo_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
