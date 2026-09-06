# Autonomy public-indicator hunt gen 472

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T160527Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma780_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.7039 | 0.7278 | 5.1329 | 0.0303 | 0.4083 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma780_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.2825 | 0.7059 | 4.6365 | 0.0260 | 0.4176 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma780_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.9304 | 0.6695 | 2.8765 | 0.0131 | 0.3305 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma780_below_at_h` | one_head_filter_pi_star | 228 | 18.6438 | 1.7988 | 0.6579 | 3.7517 | 0.0126 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma780_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.7450 | 0.6538 | 3.3525 | 0.0115 | 0.3173 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma780_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.7588 | 0.6325 | 2.5103 | 0.0109 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma780_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1798 | 0.5989 | 0.9078 | 0.0063 | 0.2086 | ok | RAN |
| ETHUSDT | 4 | `sma780_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1655 | 0.5909 | 0.8208 | 0.0062 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma780_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma780_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
