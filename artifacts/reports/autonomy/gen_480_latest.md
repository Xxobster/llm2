# Autonomy public-indicator hunt gen 480

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T163628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma800_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.6539 | 0.7232 | 5.2172 | 0.0293 | 0.3898 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma800_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.4283 | 0.7191 | 5.1043 | 0.0279 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma800_below_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.7933 | 0.6591 | 3.6140 | 0.0123 | 0.3182 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma800_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7056 | 0.6585 | 3.1914 | 0.0111 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma800_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.6768 | 0.6351 | 2.7365 | 0.0101 | 0.3176 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma800_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.5484 | 0.6090 | 2.1271 | 0.0084 | 0.3008 | ok | RAN |
| ETHUSDT | 8 | `sma800_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2075 | 0.5938 | 1.0203 | 0.0076 | 0.2188 | ok | RAN |
| ETHUSDT | 4 | `sma800_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.1335 | 0.5893 | 0.6841 | 0.0051 | 0.2024 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma800_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma800_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
