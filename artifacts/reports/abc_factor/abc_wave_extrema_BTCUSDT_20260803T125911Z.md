# ABC wave-extrema factor arm — BTCUSDT (20260803T125911Z)

**Readiness: RESEARCH_ONLY.** Train window ends `2026-05-01`.

Separate arm from warehouse `indicators.legs`. Labels are `abc_wave|*`. Not a substitute for audited confirmation times on swing legs.

## BTCUSDT 1h

- triples: 6719, median factor 0.9256535048118324
- effects: 60, FDR survivors q≤0.05: 0

| name | statistic | n | p | q | significant |
|---|---|---|---|---|---|
| abc_wave|classical|1.000|fwd6 | 0.00242 | 182 | 0.0455 | 0.5854 | False |
| abc_wave|placebo|0.900|fwd6 | -0.00175 | 213 | 0.0512 | 0.5854 | False |
| abc_wave|placebo|0.900|fwd24 | -0.00386 | 213 | 0.0585 | 0.5854 | False |
| abc_wave|placebo|1.150|fwd24 | 0.00464 | 133 | 0.0155 | 0.5854 | False |
| abc_wave|bc_continuation|0618|fwd24 | 0.00322 | 302 | 0.0540 | 0.5854 | False |
| abc_wave|bc_continuation|equal|fwd96 | -0.00670 | 182 | 0.0304 | 0.5854 | False |
| abc_wave|classical|0.500|fwd6 | 0.00029 | 319 | 0.6575 | 0.9843 | False |
| abc_wave|classical|0.618|fwd6 | -0.00089 | 302 | 0.2591 | 0.9843 | False |
| abc_wave|classical|0.786|fwd6 | 0.00064 | 252 | 0.3566 | 0.9843 | False |
| abc_wave|classical|1.272|fwd6 | 0.00084 | 123 | 0.5768 | 0.9843 | False |
| abc_wave|classical|1.618|fwd6 | 0.00030 | 119 | 0.7745 | 0.9843 | False |
| abc_wave|placebo|0.350|fwd6 | -0.00052 | 385 | 0.4331 | 0.9843 | False |
| abc_wave|placebo|0.450|fwd6 | 0.00022 | 355 | 0.7908 | 0.9843 | False |
| abc_wave|placebo|0.720|fwd6 | -0.00035 | 288 | 0.6983 | 0.9843 | False |
| abc_wave|placebo|1.150|fwd6 | 0.00123 | 133 | 0.2746 | 0.9843 | False |
| abc_wave|placebo|1.400|fwd6 | -0.00105 | 125 | 0.3536 | 0.9843 | False |
| abc_wave|knn_k10|fwd6 | -0.01996 | 2016 | 0.7144 | 0.9843 | False |
| abc_wave|PLACEBO_knn_k10|fwd6 | 0.00541 | 2016 | 0.9210 | 0.9843 | False |
| abc_wave|knn_k50|fwd6 | -0.02555 | 2016 | 0.6395 | 0.9843 | False |
| abc_wave|PLACEBO_knn_k50|fwd6 | -0.01130 | 2016 | 0.8360 | 0.9843 | False |

## BTCUSDT 4h

- triples: 1133, median factor 0.9029899182207527
- effects: 30, FDR survivors q≤0.05: 0

| name | statistic | n | p | q | significant |
|---|---|---|---|---|---|
| abc_wave|placebo|0.350|fwd96 | -0.01884 | 63 | 0.0298 | 0.4849 | False |
| abc_wave|placebo|0.450|fwd96 | -0.01369 | 57 | 0.0323 | 0.4849 | False |
| abc_wave|placebo|0.350|fwd24 | -0.00659 | 63 | 0.0568 | 0.5680 | False |
| abc_wave|classical|0.500|fwd6 | 0.00393 | 49 | 0.1050 | 0.7013 | False |
| abc_wave|classical|0.500|fwd24 | 0.00959 | 49 | 0.1636 | 0.7013 | False |
| abc_wave|classical|0.786|fwd24 | 0.00912 | 48 | 0.1196 | 0.7013 | False |
| abc_wave|linear_corr|fwd24 | -0.04524 | 1131 | 0.1612 | 0.7013 | False |
| abc_wave|classical|0.786|fwd6 | -0.00125 | 48 | 0.8124 | 0.9655 | False |
| abc_wave|placebo|0.350|fwd6 | -0.00171 | 63 | 0.5411 | 0.9655 | False |
| abc_wave|placebo|0.450|fwd6 | 0.00289 | 57 | 0.3473 | 0.9655 | False |
| abc_wave|placebo|0.720|fwd6 | -0.00220 | 42 | 0.6465 | 0.9655 | False |
| abc_wave|knn_k10|fwd6 | 0.03406 | 340 | 0.7976 | 0.9655 | False |
| abc_wave|PLACEBO_knn_k10|fwd6 | 0.02854 | 340 | 0.8299 | 0.9655 | False |
| abc_wave|knn_k50|fwd6 | 0.03571 | 340 | 0.7880 | 0.9655 | False |
| abc_wave|PLACEBO_knn_k50|fwd6 | -0.12970 | 340 | 0.3262 | 0.9655 | False |
| abc_wave|linear_corr|fwd6 | 0.00167 | 1132 | 0.6840 | 0.9655 | False |
| abc_wave|placebo|0.450|fwd24 | 0.00139 | 57 | 0.8191 | 0.9655 | False |
| abc_wave|placebo|0.720|fwd24 | 0.00426 | 42 | 0.5440 | 0.9655 | False |
| abc_wave|knn_k10|fwd24 | -0.06038 | 340 | 0.8200 | 0.9655 | False |
| abc_wave|knn_k50|fwd24 | -0.05268 | 340 | 0.8427 | 0.9655 | False |

