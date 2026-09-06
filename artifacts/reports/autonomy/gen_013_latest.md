# Autonomy public-indicator hunt gen 013

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T081943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `atr_rel_high_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7502 | 0.6757 | 3.8266 | 0.0222 | 0.3559 | EBR>35% | RAN |
| ETHUSDT | 8 | `atr_rel_high_at_h` | one_head_filter_pi_star | 235 | 19.1177 | 1.5916 | 0.6426 | 3.1765 | 0.0186 | 0.3660 | EBR>35% | RAN |
| SOLUSDT | 8 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 72 | 5.9988 | 2.1235 | 0.6667 | 2.7439 | 0.0164 | 0.1806 | GATE_CAND | RAN |
| ETHUSDT | 4 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 50 | 4.2959 | 1.3676 | 0.6600 | 0.9546 | 0.0159 | 0.2400 | ok | RAN |
| SOLUSDT | 4 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 61 | 5.0823 | 1.9116 | 0.6230 | 2.1806 | 0.0153 | 0.1803 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `atr_rel_high_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.6238 | 0.6215 | 2.7036 | 0.0112 | 0.4520 | EBR>35% | RAN |
| SOLUSDT | 8 | `atr_rel_high_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.5723 | 0.6302 | 2.5640 | 0.0101 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 81 | 6.9074 | 1.1848 | 0.5802 | 0.6469 | 0.0078 | 0.2222 | ok | RAN |
| BTCUSDT | 8 | `atr_rel_high_at_h` | one_head_filter_pi_star | 26 | 2.2125 | 1.0181 | 0.4231 | 0.0369 | 0.0019 | 0.1154 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `atr_rel_high_at_h` | one_head_filter_pi_star | 24 | 2.0423 | 0.9778 | 0.4167 | -0.0450 | -0.0024 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 4 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atr_rel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atr_rel_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `atr_rel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
