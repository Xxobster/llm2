# Autonomy public-indicator hunt gen 007

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T064747Z`. Arms: 51.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `macd_cross_up` | one_head_filter_pi_star | 14 | 1.4192 | 10.9675 | 0.8571 | 2.9356 | 0.0532 | 0.2143 | TPM<MIN | RAN |
| ETHUSDT | 4 | `macd_cross_down` | one_head_filter_pi_star | 20 | 1.7838 | 1.6072 | 0.6000 | 1.0423 | 0.0291 | 0.4500 | EBR>35% | RAN |
| ETHUSDT | 4 | `minus_di_dom_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.8080 | 0.6744 | 3.7991 | 0.0208 | 0.3674 | EBR>35% | RAN |
| ETHUSDT | 8 | `macd_cross_up` | one_head_filter_pi_star | 36 | 3.0624 | 2.0054 | 0.7222 | 1.8764 | 0.0207 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `stoch_cross_up_20` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0204 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `minus_di_dom_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7916 | 0.6729 | 3.7783 | 0.0202 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 212 | 17.3185 | 1.7461 | 0.6792 | 3.5381 | 0.0197 | 0.3821 | EBR>35% | RAN |
| SOLUSDT | 4 | `minus_di_dom_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1639 | 0.6860 | 4.1971 | 0.0178 | 0.4128 | EBR>35% | RAN |
| SOLUSDT | 8 | `macd_cross_up` | one_head_filter_pi_star | 43 | 3.6806 | 2.3500 | 0.7209 | 2.2824 | 0.0176 | 0.3023 | TPM<MIN | RAN |
| SOLUSDT | 8 | `stoch_cross_up_20` | one_head_filter_pi_star | 160 | 13.0833 | 2.1227 | 0.6813 | 3.8351 | 0.0174 | 0.4188 | EBR>35% | RAN |
| SOLUSDT | 8 | `minus_di_dom_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.0957 | 0.6805 | 4.0007 | 0.0170 | 0.4024 | EBR>35% | RAN |
| SOLUSDT | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 148 | 12.1021 | 2.0058 | 0.6757 | 3.4209 | 0.0160 | 0.4122 | EBR>35% | RAN |
| ETHUSDT | 8 | `macd_cross_down` | one_head_filter_pi_star | 39 | 3.4785 | 1.3445 | 0.5641 | 0.8402 | 0.0154 | 0.2821 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `stoch_cross_down_80` | one_head_filter_pi_star | 158 | 13.0384 | 1.2237 | 0.5886 | 1.0210 | 0.0073 | 0.1962 | ok | RAN |
| ETHUSDT | 8 | `plus_di_dom_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2232 | 0.6037 | 1.0174 | 0.0071 | 0.2012 | ok | RAN |
| ETHUSDT | 4 | `plus_di_dom_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.2074 | 0.6000 | 0.9712 | 0.0066 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `plus_di_dom_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3937 | 0.6039 | 2.0460 | 0.0057 | 0.2464 | ok | RAN |
| SOLUSDT | 4 | `stoch_cross_down_80` | one_head_filter_pi_star | 196 | 15.9819 | 1.3700 | 0.5816 | 1.8619 | 0.0054 | 0.2296 | ok | RAN |
| SOLUSDT | 8 | `stoch_cross_down_80` | one_head_filter_pi_star | 212 | 17.2866 | 1.3468 | 0.5849 | 1.8642 | 0.0052 | 0.2453 | ok | RAN |
| SOLUSDT | 8 | `plus_di_dom_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3138 | 0.5902 | 1.6822 | 0.0047 | 0.2488 | ok | RAN |
| ETHUSDT | 4 | `stoch_cross_down_80` | one_head_filter_pi_star | 148 | 12.2132 | 1.1234 | 0.5811 | 0.5655 | 0.0042 | 0.1757 | ok | RAN |
| SOLUSDT | 4 | `macd_cross_up` | one_head_filter_pi_star | 17 | 1.5284 | 1.1939 | 0.5882 | 0.3353 | 0.0037 | 0.1176 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `stoch_overbought_at_h` | one_head_filter_pi_star | 14 | 1.9644 | 0.9061 | 0.5000 | -0.2392 | -0.0033 | 0.6429 | EBR>35% | RAN |
| SOLUSDT | 8 | `macd_cross_down` | one_head_filter_pi_star | 41 | 3.3644 | 0.7689 | 0.5366 | -0.7589 | -0.0042 | 0.1463 | TPM<MIN | RAN |
| SOLUSDT | 4 | `macd_cross_down` | one_head_filter_pi_star | 12 | 1.1345 | 0.4293 | 0.4167 | -1.2174 | -0.0226 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `plus_di_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `stoch_cross_down_80` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `plus_di_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `stoch_cross_down_80` | one_head_filter_pi_star | 16 | 1.3616 | 0.1082 | 0.1875 | -2.3673 | -0.0983 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `stoch_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `stoch_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `stoch_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stoch_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `macd_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `macd_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `minus_di_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `stoch_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stoch_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stoch_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `macd_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `macd_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `minus_di_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
