# Autonomy public-indicator hunt gen 1091

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T215355Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma610_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1328 | 0.6915 | 4.5684 | 0.0252 | 0.3936 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma610_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9548 | 0.6809 | 4.1869 | 0.0223 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma610_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8661 | 0.6716 | 3.8174 | 0.0127 | 0.3137 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma610_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.6630 | 0.6537 | 3.0768 | 0.0106 | 0.3220 | ok | RAN |
| SOLUSDT | 4 | `sma610_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.6877 | 0.6209 | 2.6134 | 0.0100 | 0.3072 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma610_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.5536 | 0.6139 | 2.3552 | 0.0089 | 0.3101 | ok | RAN |
| ETHUSDT | 8 | `sma610_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1924 | 0.6051 | 0.9669 | 0.0073 | 0.2357 | ok | RAN |
| ETHUSDT | 4 | `sma610_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1411 | 0.5924 | 0.7257 | 0.0053 | 0.2166 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma610_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma610_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma610_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma610_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
