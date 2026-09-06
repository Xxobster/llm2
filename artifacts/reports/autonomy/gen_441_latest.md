# Autonomy public-indicator hunt gen 441

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T120526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema660_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9413 | 0.6780 | 4.2220 | 0.0221 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema660_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8309 | 0.6732 | 3.7571 | 0.0201 | 0.3707 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema660_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8724 | 0.6714 | 3.7912 | 0.0128 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema660_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.7999 | 0.6605 | 3.6007 | 0.0125 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema660_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.6983 | 0.6351 | 2.7181 | 0.0105 | 0.3243 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema660_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.6042 | 0.6400 | 2.4171 | 0.0091 | 0.3133 | ok | RAN |
| ETHUSDT | 8 | `ema660_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.2157 | 0.6184 | 0.9996 | 0.0077 | 0.2039 | ok | RAN |
| ETHUSDT | 4 | `ema660_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1870 | 0.6000 | 0.8943 | 0.0069 | 0.2065 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
