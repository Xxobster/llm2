# Autonomy public-indicator hunt gen 1339

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T235855Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma650_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0112 | 0.6796 | 4.1581 | 0.0235 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma650_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.8702 | 0.6685 | 3.7109 | 0.0214 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma650_below_at_h` | one_head_filter_pi_star | 193 | 15.7009 | 1.8691 | 0.6788 | 3.6248 | 0.0131 | 0.3420 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma650_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 1.8002 | 0.6667 | 3.5601 | 0.0125 | 0.3237 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma650_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.7052 | 0.6325 | 2.4761 | 0.0105 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma650_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.5596 | 0.6107 | 2.3064 | 0.0087 | 0.3020 | ok | RAN |
| ETHUSDT | 8 | `sma650_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2219 | 0.6090 | 1.0789 | 0.0083 | 0.2244 | ok | RAN |
| ETHUSDT | 4 | `sma650_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1704 | 0.5988 | 0.8572 | 0.0062 | 0.2275 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma650_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma650_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma650_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma650_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
