# Autonomy public-indicator hunt gen 867

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T220649Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma564_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1598 | 0.6989 | 4.5857 | 0.0259 | 0.4205 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma564_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0598 | 0.6927 | 4.5087 | 0.0232 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma564_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.9376 | 0.6769 | 3.9056 | 0.0133 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma564_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7671 | 0.6600 | 3.4197 | 0.0117 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma564_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.6123 | 0.6196 | 2.5809 | 0.0095 | 0.3190 | ok | RAN |
| SOLUSDT | 8 | `sma564_above_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.5294 | 0.6000 | 2.4001 | 0.0080 | 0.2743 | ok | RAN |
| ETHUSDT | 4 | `sma564_above_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.1858 | 0.5939 | 0.9382 | 0.0066 | 0.2242 | ok | RAN |
| ETHUSDT | 8 | `sma564_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1298 | 0.5749 | 0.6629 | 0.0048 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma564_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.7439 | 0.2941 | -0.4783 | -0.0211 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma564_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma564_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma564_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
