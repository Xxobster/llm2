# Autonomy public-indicator hunt gen 355

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T153937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma136_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9154 | 0.6856 | 4.2673 | 0.0221 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma136_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8624 | 0.6859 | 4.0705 | 0.0210 | 0.3665 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma136_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.3136 | 0.6977 | 4.4469 | 0.0179 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma136_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.2910 | 0.6919 | 4.5784 | 0.0176 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma136_above_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.2391 | 0.6051 | 1.2440 | 0.0082 | 0.2256 | ok | RAN |
| ETHUSDT | 8 | `sma136_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2305 | 0.6022 | 1.1884 | 0.0080 | 0.2258 | ok | RAN |
| SOLUSDT | 8 | `sma136_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3071 | 0.5916 | 1.5992 | 0.0049 | 0.2723 | ok | RAN |
| SOLUSDT | 4 | `sma136_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2955 | 0.5879 | 1.5612 | 0.0047 | 0.2563 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma136_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma136_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma136_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma136_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma136_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma136_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
