# Autonomy public-indicator hunt gen 426

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T082002Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret280_neg_at_h` | one_head_filter_pi_star | 141 | 11.5184 | 2.5784 | 0.7447 | 4.6964 | 0.0301 | 0.4468 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret280_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.0816 | 0.7055 | 4.1324 | 0.0250 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret280_neg_at_h` | one_head_filter_pi_star | 149 | 12.1839 | 1.9593 | 0.6711 | 3.4869 | 0.0153 | 0.3758 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret280_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.8641 | 0.6706 | 3.3904 | 0.0135 | 0.3412 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret280_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.6837 | 0.6384 | 2.8999 | 0.0101 | 0.2994 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret280_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.6635 | 0.6284 | 2.8082 | 0.0098 | 0.2951 | ok | RAN |
| ETHUSDT | 4 | `ret280_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1270 | 0.5876 | 0.6984 | 0.0047 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `ret280_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1187 | 0.5876 | 0.6290 | 0.0044 | 0.2034 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret280_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret280_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret280_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret280_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret280_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret280_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
