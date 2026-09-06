# Autonomy public-indicator hunt gen 015

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T082811Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma_cross_down` | one_head_filter_pi_star | 26 | 2.3269 | 2.2227 | 0.7308 | 1.6827 | 0.0294 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma_cross_up` | one_head_filter_pi_star | 40 | 3.8450 | 1.9671 | 0.6250 | 1.6605 | 0.0253 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma_cross_down` | one_head_filter_pi_star | 23 | 2.1220 | 2.1933 | 0.6957 | 1.7503 | 0.0236 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma_cross_down` | one_head_filter_pi_star | 37 | 3.0922 | 1.9159 | 0.6216 | 1.5921 | 0.0232 | 0.2162 | TPM<MIN | RAN |
| ETHUSDT | 8 | `close_below_sma50_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7797 | 0.6771 | 3.8244 | 0.0207 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `close_below_sma50_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7682 | 0.6773 | 3.7792 | 0.0206 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma_cross_down` | one_head_filter_pi_star | 43 | 3.5829 | 1.9220 | 0.6512 | 2.0941 | 0.0197 | 0.3953 | EBR>35% | RAN |
| SOLUSDT | 4 | `close_below_sma50_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2240 | 0.6951 | 4.2301 | 0.0184 | 0.4146 | EBR>35% | RAN |
| SOLUSDT | 8 | `close_below_sma50_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2019 | 0.6871 | 4.1317 | 0.0183 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma_cross_up` | one_head_filter_pi_star | 21 | 2.0186 | 1.3566 | 0.4762 | 0.5449 | 0.0089 | 0.2381 | TPM<MIN | RAN |
| ETHUSDT | 4 | `close_above_sma50_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2748 | 0.6025 | 1.2357 | 0.0083 | 0.2112 | ok | RAN |
| ETHUSDT | 8 | `close_above_sma50_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2419 | 0.5975 | 1.1005 | 0.0074 | 0.2013 | ok | RAN |
| SOLUSDT | 4 | `close_above_sma50_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3183 | 0.5935 | 1.7468 | 0.0047 | 0.2430 | ok | RAN |
| SOLUSDT | 8 | `close_above_sma50_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3008 | 0.5924 | 1.6486 | 0.0045 | 0.2464 | ok | RAN |
| SOLUSDT | 8 | `sma_cross_up` | one_head_filter_pi_star | 55 | 4.8976 | 1.1710 | 0.5455 | 0.4965 | 0.0037 | 0.1455 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma_cross_up` | one_head_filter_pi_star | 34 | 3.0276 | 0.9277 | 0.5588 | -0.1895 | -0.0018 | 0.1471 | TPM<MIN | RAN |
| BTCUSDT | 4 | `close_above_sma50_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `close_above_sma50_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `close_below_sma50_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `close_below_sma50_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
