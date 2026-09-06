# Autonomy public-indicator hunt gen 1331

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T231313Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma649_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8940 | 0.6842 | 4.0151 | 0.0223 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma649_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.8671 | 0.6701 | 4.0146 | 0.0213 | 0.3553 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma649_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 1.8213 | 0.6682 | 3.5769 | 0.0125 | 0.3270 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma649_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.7388 | 0.6555 | 3.3785 | 0.0115 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma649_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.6708 | 0.6258 | 2.7393 | 0.0103 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma649_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2483 | 0.6000 | 1.1658 | 0.0088 | 0.2188 | ok | RAN |
| SOLUSDT | 8 | `sma649_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5694 | 0.6250 | 2.2767 | 0.0088 | 0.3264 | ok | RAN |
| ETHUSDT | 8 | `sma649_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.2272 | 0.6138 | 1.0650 | 0.0084 | 0.2138 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma649_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma649_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma649_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma649_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma649_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma649_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
