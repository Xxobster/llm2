# Autonomy public-indicator hunt gen 907

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T021311Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma594_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0275 | 0.6848 | 4.3807 | 0.0239 | 0.3967 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma594_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.9693 | 0.6882 | 3.8959 | 0.0227 | 0.4176 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma594_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.7720 | 0.6632 | 3.3456 | 0.0117 | 0.3263 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma594_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7507 | 0.6600 | 3.3911 | 0.0117 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma594_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.5550 | 0.6203 | 2.3294 | 0.0090 | 0.3228 | ok | RAN |
| SOLUSDT | 8 | `sma594_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.5061 | 0.6119 | 2.0331 | 0.0080 | 0.3134 | ok | RAN |
| ETHUSDT | 8 | `sma594_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1827 | 0.6012 | 0.9319 | 0.0065 | 0.2209 | ok | RAN |
| ETHUSDT | 4 | `sma594_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1704 | 0.5989 | 0.9035 | 0.0061 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma594_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma594_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma594_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma594_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma594_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma594_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
