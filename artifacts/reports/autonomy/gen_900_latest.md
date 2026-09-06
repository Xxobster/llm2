# Autonomy public-indicator hunt gen 900

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T012706Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema885_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 2.0069 | 0.6741 | 4.3149 | 0.0218 | 0.3661 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema885_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7513 | 0.6603 | 3.4842 | 0.0185 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema885_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.7943 | 0.6568 | 3.7788 | 0.0122 | 0.3093 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema885_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.7773 | 0.6403 | 3.8036 | 0.0119 | 0.2925 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema885_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.6617 | 0.6336 | 2.3948 | 0.0099 | 0.3206 | ok | RAN |
| SOLUSDT | 8 | `ema885_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.6600 | 0.6296 | 2.4353 | 0.0098 | 0.3185 | ok | RAN |
| ETHUSDT | 8 | `ema885_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2147 | 0.5957 | 0.9951 | 0.0082 | 0.2270 | ok | RAN |
| ETHUSDT | 4 | `ema885_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.1815 | 0.5882 | 0.8899 | 0.0068 | 0.2288 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema885_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0383 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema885_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema885_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema885_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema885_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema885_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
