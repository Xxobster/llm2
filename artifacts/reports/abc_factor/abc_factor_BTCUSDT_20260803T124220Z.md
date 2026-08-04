# ABC distance-factor study — BTCUSDT (20260803T124220Z)

**Readiness: RESEARCH_ONLY.** Train window ends `2026-05-01`.

Definition: three consecutive confirmed swings A→B→C; `factor = |BC| / |AB|`; known only when C is confirmed.

## BTCUSDT 1h

- triples: 10155, median factor 0.944, fraction near 1.0: 4.9%, near 0.618: 8.5%, near 1.618: 2.6%
- effects: 60, FDR survivors q≤0.05: 4

| name | statistic | n | p | q | significant |
|---|---|---|---|---|---|
| abc_factor|bc_continuation|equal|fwd6 | -0.00388 | 493 | 0.0000 | 0.0000 | True |
| abc_factor|bc_continuation|1618|fwd6 | -0.00432 | 269 | 0.0000 | 0.0000 | True |
| abc_factor|bc_continuation|0618|fwd24 | -0.00298 | 866 | 0.0000 | 0.0004 | True |
| abc_factor|bc_continuation|equal|fwd24 | -0.00449 | 493 | 0.0052 | 0.0619 | False |
| abc_factor|bc_continuation|equal|fwd96 | -0.00824 | 493 | 0.0083 | 0.0828 | False |
| abc_factor|classical|1.272|fwd6 | 0.00170 | 468 | 0.0126 | 0.1084 | False |
| abc_factor|classical|1.618|fwd96 | -0.00389 | 267 | 0.0273 | 0.2046 | False |
| abc_factor|bc_continuation|0618|fwd96 | -0.00248 | 865 | 0.0587 | 0.3915 | False |
| abc_factor|classical|1.000|fwd6 | -0.00136 | 493 | 0.0760 | 0.4558 | False |
| abc_factor|classical|1.618|fwd6 | -0.00109 | 269 | 0.1089 | 0.5497 | False |
| abc_factor|linear_corr|fwd6 | 0.00292 | 10153 | 0.1099 | 0.5497 | False |
| abc_factor|bc_continuation|1618|fwd96 | -0.00338 | 267 | 0.1466 | 0.6767 | False |
| abc_factor|classical|0.618|fwd24 | -0.00112 | 866 | 0.2086 | 0.7479 | False |
| abc_factor|classical|1.000|fwd24 | -0.00189 | 493 | 0.1896 | 0.7479 | False |
| abc_factor|linear_corr|fwd24 | 0.00397 | 10149 | 0.2244 | 0.7479 | False |
| abc_factor|bc_continuation|1618|fwd24 | -0.00134 | 268 | 0.2117 | 0.7479 | False |
| abc_factor|placebo|1.150|fwd96 | -0.00398 | 469 | 0.2163 | 0.7479 | False |
| abc_factor|linear_corr|fwd96 | 0.01310 | 10139 | 0.3130 | 0.9885 | False |
| abc_factor|classical|0.500|fwd6 | -0.00033 | 721 | 0.5180 | 0.9923 | False |
| abc_factor|classical|0.618|fwd6 | -0.00035 | 866 | 0.4781 | 0.9923 | False |

## BTCUSDT 4h

- triples: 2436, median factor 0.961, fraction near 1.0: 5.0%, near 0.618: 8.8%, near 1.618: 2.6%
- effects: 60, FDR survivors q≤0.05: 7

| name | statistic | n | p | q | significant |
|---|---|---|---|---|---|
| abc_factor|classical|1.272|fwd96 | -0.02417 | 104 | 0.0000 | 0.0001 | True |
| abc_factor|bc_continuation|equal|fwd6 | -0.00973 | 121 | 0.0000 | 0.0013 | True |
| abc_factor|bc_continuation|0618|fwd6 | -0.01208 | 215 | 0.0001 | 0.0013 | True |
| abc_factor|bc_continuation|0618|fwd24 | -0.01054 | 215 | 0.0006 | 0.0075 | True |
| abc_factor|bc_continuation|1618|fwd96 | -0.02352 | 63 | 0.0006 | 0.0075 | True |
| abc_factor|bc_continuation|1618|fwd24 | -0.01323 | 63 | 0.0009 | 0.0087 | True |
| abc_factor|classical|1.272|fwd6 | -0.00734 | 106 | 0.0013 | 0.0112 | True |
| abc_factor|classical|1.618|fwd6 | -0.00993 | 63 | 0.0100 | 0.0752 | False |
| abc_factor|placebo|0.900|fwd24 | 0.00989 | 178 | 0.0143 | 0.0943 | False |
| abc_factor|bc_continuation|equal|fwd24 | -0.00922 | 121 | 0.0157 | 0.0943 | False |
| abc_factor|placebo|0.900|fwd6 | 0.00539 | 178 | 0.0242 | 0.1209 | False |
| abc_factor|bc_continuation|0618|fwd96 | -0.00886 | 214 | 0.0229 | 0.1209 | False |
| abc_factor|classical|1.272|fwd24 | -0.01310 | 104 | 0.0340 | 0.1568 | False |
| abc_factor|classical|1.000|fwd24 | -0.00802 | 121 | 0.0498 | 0.2134 | False |
| abc_factor|placebo|1.400|fwd6 | 0.00654 | 96 | 0.0586 | 0.2155 | False |
| abc_factor|classical|0.500|fwd24 | 0.01037 | 157 | 0.0583 | 0.2155 | False |
| abc_factor|placebo|1.400|fwd96 | 0.00632 | 96 | 0.0610 | 0.2155 | False |
| abc_factor|placebo|1.150|fwd96 | 0.01455 | 128 | 0.0687 | 0.2290 | False |
| abc_factor|bc_continuation|1618|fwd6 | -0.00716 | 63 | 0.1002 | 0.3164 | False |
| abc_factor|linear_corr|fwd6 | -0.04579 | 2433 | 0.1415 | 0.4244 | False |

