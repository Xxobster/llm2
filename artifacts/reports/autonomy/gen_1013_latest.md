# Autonomy public-indicator hunt gen 1013

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T120417Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret396_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.6936 | 0.7456 | 5.2700 | 0.0320 | 0.4083 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret396_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.1453 | 0.6977 | 4.2400 | 0.0258 | 0.3953 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret396_neg_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 1.8583 | 0.6700 | 3.5929 | 0.0128 | 0.3202 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret396_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.7136 | 0.6614 | 3.1429 | 0.0108 | 0.3280 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret396_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.5938 | 0.6250 | 2.4589 | 0.0095 | 0.2763 | ok | RAN |
| SOLUSDT | 4 | `ret396_pos_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.6029 | 0.6154 | 2.2355 | 0.0094 | 0.3000 | ok | RAN |
| ETHUSDT | 4 | `ret396_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1801 | 0.6022 | 0.9572 | 0.0063 | 0.2258 | ok | RAN |
| ETHUSDT | 8 | `ret396_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1275 | 0.5904 | 0.6409 | 0.0050 | 0.2410 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret396_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5883 | 0.3500 | -0.8891 | -0.0429 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret396_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret396_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret396_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret396_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret396_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
