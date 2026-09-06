# Autonomy public-indicator hunt gen 494

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T173122Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma215_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0426 | 0.6952 | 4.6144 | 0.0240 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma215_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9593 | 0.6872 | 4.3316 | 0.0226 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma215_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.3305 | 0.7039 | 4.6230 | 0.0187 | 0.3855 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma215_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1932 | 0.6941 | 4.2117 | 0.0174 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma215_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2458 | 0.6085 | 1.2193 | 0.0084 | 0.2275 | ok | RAN |
| ETHUSDT | 4 | `wma215_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.1731 | 0.5947 | 0.8917 | 0.0060 | 0.2158 | ok | RAN |
| SOLUSDT | 8 | `wma215_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3866 | 0.6010 | 1.9817 | 0.0059 | 0.2709 | ok | RAN |
| SOLUSDT | 4 | `wma215_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.2794 | 0.5850 | 1.4741 | 0.0043 | 0.2600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma215_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma215_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma215_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma215_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
