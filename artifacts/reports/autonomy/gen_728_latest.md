# Autonomy public-indicator hunt gen 728

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T091149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1420_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7602 | 0.6578 | 3.5445 | 0.0184 | 0.3511 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1420_below_at_h` | one_head_filter_pi_star | 256 | 20.9129 | 1.6312 | 0.6406 | 3.5182 | 0.0162 | 0.3281 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1420_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 2.1054 | 0.7115 | 2.4008 | 0.0141 | 0.3269 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1420_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7727 | 0.6307 | 4.1074 | 0.0117 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1420_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.7546 | 0.6328 | 4.0705 | 0.0112 | 0.3246 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1420_above_at_h` | one_head_filter_pi_star | 75 | 6.1654 | 1.6653 | 0.6533 | 1.8219 | 0.0105 | 0.3200 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1420_above_at_h` | one_head_filter_pi_star | 104 | 8.5830 | 1.1396 | 0.5865 | 0.5810 | 0.0057 | 0.2115 | ok | RAN |
| ETHUSDT | 8 | `sma1420_above_at_h` | one_head_filter_pi_star | 93 | 7.6751 | 1.0760 | 0.5484 | 0.2976 | 0.0030 | 0.2151 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1420_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0740 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1420_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3380 | 0.2500 | -1.4955 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
