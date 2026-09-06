# Autonomy public-indicator hunt gen 529

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T195159Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema880_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.9121 | 0.6725 | 4.1052 | 0.0209 | 0.3493 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema880_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.7835 | 0.6696 | 3.7126 | 0.0191 | 0.3524 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema880_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.8690 | 0.6638 | 3.9934 | 0.0128 | 0.3064 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema880_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.7981 | 0.6515 | 3.8036 | 0.0122 | 0.3112 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema880_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.7423 | 0.6412 | 2.5415 | 0.0103 | 0.3206 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema880_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.5462 | 0.6129 | 2.0548 | 0.0082 | 0.2984 | ok | RAN |
| ETHUSDT | 8 | `ema880_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 1.1804 | 0.5827 | 0.8684 | 0.0070 | 0.2230 | ok | RAN |
| ETHUSDT | 4 | `ema880_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 1.1874 | 0.5846 | 0.8531 | 0.0070 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema880_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema880_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
