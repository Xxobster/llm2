# Autonomy public-indicator hunt gen 248

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T014928Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma220_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1818 | 0.7127 | 4.9117 | 0.0266 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma220_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0851 | 0.7039 | 4.5704 | 0.0247 | 0.3911 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma220_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1772 | 0.6901 | 4.1424 | 0.0168 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma220_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1503 | 0.6864 | 4.0234 | 0.0163 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma220_above_at_h` | one_head_filter_pi_star | 194 | 16.0092 | 1.1975 | 0.5928 | 1.0449 | 0.0069 | 0.2165 | ok | RAN |
| SOLUSDT | 8 | `sma220_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3558 | 0.6000 | 1.8041 | 0.0056 | 0.2684 | ok | RAN |
| SOLUSDT | 4 | `sma220_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3467 | 0.5951 | 1.8114 | 0.0055 | 0.2585 | ok | RAN |
| ETHUSDT | 4 | `sma220_above_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.1519 | 0.5879 | 0.8136 | 0.0054 | 0.2261 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
