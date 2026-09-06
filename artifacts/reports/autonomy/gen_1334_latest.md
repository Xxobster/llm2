# Autonomy public-indicator hunt gen 1334

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T233020Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma740_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0573 | 0.6919 | 4.4621 | 0.0241 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma740_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9668 | 0.6947 | 4.1911 | 0.0225 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma740_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8991 | 0.6732 | 3.8708 | 0.0135 | 0.3415 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma740_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8324 | 0.6618 | 3.6586 | 0.0124 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma740_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.2741 | 0.6053 | 1.2962 | 0.0093 | 0.2237 | ok | RAN |
| SOLUSDT | 4 | `wma740_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.5612 | 0.6127 | 2.4933 | 0.0089 | 0.2890 | ok | RAN |
| SOLUSDT | 8 | `wma740_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5605 | 0.6089 | 2.5684 | 0.0089 | 0.2849 | ok | RAN |
| ETHUSDT | 8 | `wma740_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2208 | 0.6071 | 1.0925 | 0.0077 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma740_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma740_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
