# Autonomy public-indicator hunt gen 300

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T052934Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema145_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0742 | 0.6968 | 4.6842 | 0.0242 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema145_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0340 | 0.6979 | 4.6403 | 0.0237 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema145_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2241 | 0.6982 | 4.2260 | 0.0179 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema145_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1603 | 0.6867 | 4.0805 | 0.0172 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema145_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2355 | 0.5957 | 1.1857 | 0.0080 | 0.2340 | ok | RAN |
| SOLUSDT | 8 | `ema145_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3237 | 0.5939 | 1.6945 | 0.0050 | 0.2690 | ok | RAN |
| SOLUSDT | 4 | `ema145_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3053 | 0.5871 | 1.6020 | 0.0048 | 0.2687 | ok | RAN |
| ETHUSDT | 4 | `ema145_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1188 | 0.5882 | 0.6326 | 0.0043 | 0.2193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema145_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema145_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema145_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema145_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema145_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema145_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
