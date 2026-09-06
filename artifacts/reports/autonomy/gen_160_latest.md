# Autonomy public-indicator hunt gen 160

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T195830Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma25_cross_up` | one_head_filter_pi_star | 26 | 2.1465 | 1.7185 | 0.6538 | 1.2195 | 0.0323 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma25_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma25_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma25_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1907 | 0.6951 | 4.0606 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma25_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0179 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma25_cross_down` | one_head_filter_pi_star | 15 | 1.3879 | 2.1206 | 0.7333 | 1.1623 | 0.0116 | 0.1333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma25_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2444 | 0.5949 | 1.1276 | 0.0077 | 0.2089 | ok | RAN |
| ETHUSDT | 4 | `sma25_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1890 | 0.5901 | 0.8787 | 0.0060 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `sma25_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.4004 | 0.5991 | 2.1548 | 0.0059 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `sma25_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3565 | 0.5953 | 1.9372 | 0.0053 | 0.2419 | ok | RAN |
| ETHUSDT | 8 | `sma25_cross_down` | one_head_filter_pi_star | 24 | 2.8024 | 1.0593 | 0.5417 | 0.1413 | 0.0025 | 0.2917 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma25_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma25_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma25_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma25_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma25_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma25_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
