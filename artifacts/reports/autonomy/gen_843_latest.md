# Autonomy public-indicator hunt gen 843

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T194513Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma546_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.9859 | 0.6864 | 4.0670 | 0.0232 | 0.4142 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma546_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0163 | 0.6862 | 4.3660 | 0.0231 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma546_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8965 | 0.6784 | 3.8700 | 0.0131 | 0.3417 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma546_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8874 | 0.6718 | 3.7941 | 0.0130 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma546_above_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.7023 | 0.6287 | 2.8734 | 0.0102 | 0.2994 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma546_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.6390 | 0.6222 | 2.7705 | 0.0096 | 0.2833 | ok | RAN |
| ETHUSDT | 8 | `sma546_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1690 | 0.5890 | 0.8497 | 0.0063 | 0.2209 | ok | RAN |
| ETHUSDT | 4 | `sma546_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.1638 | 0.5900 | 0.8810 | 0.0058 | 0.2100 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma546_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma546_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma546_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma546_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
