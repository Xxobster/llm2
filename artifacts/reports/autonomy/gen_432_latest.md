# Autonomy public-indicator hunt gen 432

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T095811Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma680_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1886 | 0.7037 | 4.6930 | 0.0263 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma680_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8466 | 0.6701 | 3.8578 | 0.0210 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma680_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.8031 | 0.6636 | 3.5616 | 0.0121 | 0.3084 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma680_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.6962 | 0.6571 | 3.2634 | 0.0111 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma680_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.5600 | 0.6210 | 2.1501 | 0.0084 | 0.3226 | ok | RAN |
| SOLUSDT | 4 | `sma680_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.4541 | 0.5942 | 1.8240 | 0.0072 | 0.2971 | ok | RAN |
| ETHUSDT | 8 | `sma680_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1835 | 0.5975 | 0.9114 | 0.0064 | 0.2201 | ok | RAN |
| ETHUSDT | 4 | `sma680_above_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.1488 | 0.5897 | 0.7312 | 0.0055 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma680_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma680_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
