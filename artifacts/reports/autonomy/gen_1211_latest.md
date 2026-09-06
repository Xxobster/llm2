# Autonomy public-indicator hunt gen 1211

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T112531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma629_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1635 | 0.6947 | 4.7707 | 0.0254 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma629_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0585 | 0.6806 | 4.3696 | 0.0245 | 0.3874 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma629_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.8757 | 0.6699 | 3.7393 | 0.0129 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma629_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.7738 | 0.6618 | 3.4668 | 0.0119 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma629_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.6860 | 0.6485 | 2.8168 | 0.0106 | 0.3152 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma629_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.4897 | 0.5926 | 1.9476 | 0.0079 | 0.3185 | ok | RAN |
| ETHUSDT | 4 | `sma629_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2178 | 0.6076 | 1.0754 | 0.0078 | 0.2089 | ok | RAN |
| ETHUSDT | 8 | `sma629_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.1473 | 0.5921 | 0.7259 | 0.0054 | 0.2171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma629_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma629_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma629_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma629_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma629_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma629_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
