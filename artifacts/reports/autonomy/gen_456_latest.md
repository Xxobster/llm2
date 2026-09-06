# Autonomy public-indicator hunt gen 456

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T150427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma740_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.2039 | 0.6923 | 4.7741 | 0.0256 | 0.3901 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma740_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.2369 | 0.7006 | 4.5669 | 0.0249 | 0.3832 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma740_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 1.7642 | 0.6550 | 3.3270 | 0.0117 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma740_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.7431 | 0.6618 | 3.3068 | 0.0116 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma740_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.4881 | 0.6045 | 1.9159 | 0.0079 | 0.2985 | ok | RAN |
| SOLUSDT | 8 | `sma740_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.4867 | 0.6032 | 1.9134 | 0.0079 | 0.3175 | ok | RAN |
| ETHUSDT | 8 | `sma740_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1493 | 0.5901 | 0.7513 | 0.0055 | 0.2112 | ok | RAN |
| ETHUSDT | 4 | `sma740_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1348 | 0.5912 | 0.6568 | 0.0050 | 0.2138 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma740_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma740_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
