# Autonomy public-indicator hunt gen 036

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T115317Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `bop_cross_up_0` | one_head_filter_pi_star | 33 | 2.7142 | 5.1845 | 0.7576 | 3.3305 | 0.0454 | 0.3030 | TPM<MIN | RAN |
| ETHUSDT | 8 | `bop_cross_up_0` | one_head_filter_pi_star | 80 | 6.5787 | 2.2414 | 0.6375 | 2.9882 | 0.0285 | 0.3375 | GATE_CAND | RAN |
| SOLUSDT | 8 | `bop_cross_down_0` | one_head_filter_pi_star | 70 | 5.7559 | 2.6222 | 0.7000 | 2.9740 | 0.0231 | 0.3000 | GATE_CAND | RAN |
| ETHUSDT | 4 | `bop_neg_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.9119 | 0.6995 | 4.0025 | 0.0221 | 0.3695 | EBR>35% | RAN |
| SOLUSDT | 4 | `bop_cross_up_0` | one_head_filter_pi_star | 31 | 2.9899 | 3.4923 | 0.7419 | 2.8624 | 0.0216 | 0.2903 | TPM<MIN | RAN |
| SOLUSDT | 4 | `bop_cross_down_0` | one_head_filter_pi_star | 36 | 2.9883 | 1.9085 | 0.6111 | 1.4969 | 0.0188 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `bop_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.6937 | 0.6750 | 3.3640 | 0.0179 | 0.3550 | EBR>35% | RAN |
| SOLUSDT | 8 | `bop_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1708 | 0.7055 | 3.9178 | 0.0168 | 0.3926 | EBR>35% | RAN |
| SOLUSDT | 8 | `bop_cross_up_0` | one_head_filter_pi_star | 68 | 5.7548 | 2.0292 | 0.6618 | 2.6061 | 0.0165 | 0.3088 | GATE_CAND | RAN |
| ETHUSDT | 4 | `bop_cross_down_0` | one_head_filter_pi_star | 58 | 5.0157 | 1.4019 | 0.6379 | 1.1547 | 0.0160 | 0.3103 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `bop_cross_down_0` | one_head_filter_pi_star | 84 | 6.9121 | 1.4018 | 0.6310 | 1.2909 | 0.0151 | 0.2381 | ok | RAN |
| SOLUSDT | 4 | `bop_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.0102 | 0.6795 | 3.6107 | 0.0151 | 0.3910 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `bop_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.2280 | 0.5966 | 1.0891 | 0.0078 | 0.2216 | ok | RAN |
| SOLUSDT | 4 | `bop_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4770 | 0.6114 | 2.4212 | 0.0070 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `bop_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4030 | 0.5952 | 2.1475 | 0.0061 | 0.2571 | ok | RAN |
| ETHUSDT | 4 | `bop_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1266 | 0.5679 | 0.6257 | 0.0045 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `bop_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `bop_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `bop_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `bop_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bop_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bop_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `bop_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bop_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
