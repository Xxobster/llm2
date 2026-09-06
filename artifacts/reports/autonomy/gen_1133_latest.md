# Autonomy public-indicator hunt gen 1133

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T025329Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret205_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.1777 | 0.6982 | 4.6654 | 0.0255 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret205_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.9837 | 0.6966 | 4.3380 | 0.0240 | 0.3933 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret205_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 2.0186 | 0.6736 | 4.0668 | 0.0153 | 0.3523 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret205_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0031 | 0.6667 | 3.7825 | 0.0152 | 0.3631 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret205_pos_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.5675 | 0.6343 | 2.5381 | 0.0085 | 0.2800 | ok | RAN |
| SOLUSDT | 8 | `ret205_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.4416 | 0.6074 | 1.9841 | 0.0069 | 0.2945 | ok | RAN |
| ETHUSDT | 8 | `ret205_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1457 | 0.5759 | 0.7873 | 0.0053 | 0.2199 | ok | RAN |
| ETHUSDT | 4 | `ret205_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1301 | 0.5842 | 0.6762 | 0.0047 | 0.2316 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret205_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret205_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret205_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret205_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret205_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret205_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
