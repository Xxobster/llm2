# Work grid + adaptive cancel + model pass (`20260812T132018Z`)

**RESEARCH_ONLY**

## Execution (ETH/SOL P75)
### ETHUSDT
| tag | work | intent_N | fill% | trade_N | exp_intent | PF | ebr% |
|---|---:|---:|---:|---:|---:|---:|---:|
| ETHUSDT_p75_w2 | 2 | 2696 | 20.4% | 475 | 0.01224 | 2.002 | 29.3% |
| ETHUSDT_p75_w3 | 3 | 2696 | 26.1% | 589 | 0.01354 | 1.841 | 27.2% |
| ETHUSDT_p75_w4 | 4 | 2696 | 30.5% | 674 | 0.01474 | 1.780 | 27.2% |
| ETHUSDT_p75_w5 | 5 | 2696 | 33.8% | 731 | 0.01459 | 1.697 | 26.0% |
| ETHUSDT_p75_w6 | 6 | 2696 | 36.4% | 781 | 0.01473 | 1.644 | 25.2% |
| ETHUSDT_p75_adaptive_time | None | 2696 | 27.7% | 622 | 0.01294 | 1.730 | 27.2% |
- prefer_shorter: `{'choice': 'ETHUSDT_p75_w4', 'work_bars': 4, 'fill_pct': 0.30452522255192876, 'expectancy_intent_all': 0.014743678931756642, 'profit_factor': 1.779732457614695, 'rule': 'among fill%>=15%, max expectancy_intent, tie -> shorter work'}`
- adaptive_vs_w4: `{'fixed_w4_pf': 1.779732457614695, 'fixed_w4_fill_pct': 0.30452522255192876, 'fixed_w4_exp_intent': 0.014743678931756642, 'adaptive_pf': 1.7295151491515526, 'adaptive_fill_pct': 0.2770771513353116, 'adaptive_exp_intent': 0.01293577266506098, 'adaptive_beats_w4_exp_intent': False}`

### SOLUSDT
| tag | work | intent_N | fill% | trade_N | exp_intent | PF | ebr% |
|---|---:|---:|---:|---:|---:|---:|---:|
| SOLUSDT_p75_w2 | 2 | 2512 | 18.6% | 423 | 0.00684 | 2.235 | 48.5% |
| SOLUSDT_p75_w3 | 3 | 2512 | 25.6% | 552 | 0.00843 | 2.107 | 46.7% |
| SOLUSDT_p75_w4 | 4 | 2512 | 29.5% | 619 | 0.00971 | 2.135 | 45.6% |
| SOLUSDT_p75_w5 | 5 | 2512 | 32.4% | 668 | 0.00990 | 2.059 | 44.2% |
| SOLUSDT_p75_w6 | 6 | 2512 | 35.4% | 715 | 0.00950 | 1.906 | 42.7% |
| SOLUSDT_p75_adaptive_time | None | 2512 | 27.3% | 585 | 0.00902 | 2.111 | 46.5% |
- prefer_shorter: `{'choice': 'SOLUSDT_p75_w5', 'work_bars': 5, 'fill_pct': 0.32404458598726116, 'expectancy_intent_all': 0.009901384275486015, 'profit_factor': 2.059148398865311, 'rule': 'among fill%>=15%, max expectancy_intent, tie -> shorter work'}`
- adaptive_vs_w4: `{'fixed_w4_pf': 2.134745633040173, 'fixed_w4_fill_pct': 0.294984076433121, 'fixed_w4_exp_intent': 0.009707999442683619, 'adaptive_pf': 2.1114673419536927, 'adaptive_fill_pct': 0.2726910828025478, 'adaptive_exp_intent': 0.009020419088381077, 'adaptive_beats_w4_exp_intent': False}`

## Model pass promotion
### ETHUSDT
- **baseline_level_vsa**: lift=0.1048 ece=0.0067 level_p90=0.0206 control_PF=1.779732457614695
- **rare_level_strong**: lift=0.1068 ece=0.0074 level_p90=0.0204 control_PF=1.7289288840379025
- **rare15_level_strong**: lift=0.1060 ece=0.0086 level_p90=0.0147 control_PF=1.0347948431121665
- promote `rare_level_strong`: **False** ({'pr_auc_lift_improved': True, 'ece_improved': False, 'pf_not_collapsed': True, 'promote': False, 'base_pf': 1.779732457614695, 'new_pf': 1.7289288840379025, 'base_lift': 0.10475683610300221, 'new_lift': 0.10679920256627143, 'base_ece': 0.006650250869834315, 'new_ece': 0.007431250342018074, 'level_p90': 0.02036993308013541, 'rule': 'lift>base AND ece<base AND pf>=0.85*base_pf'})
- promote `rare15_level_strong`: **False** ({'pr_auc_lift_improved': True, 'ece_improved': False, 'pf_not_collapsed': False, 'promote': False, 'base_pf': 1.779732457614695, 'new_pf': 1.0347948431121665, 'base_lift': 0.10475683610300221, 'new_lift': 0.10596891739467579, 'base_ece': 0.006650250869834315, 'new_ece': 0.008554734605621417, 'level_p90': 0.014685693451166895, 'rule': 'lift>base AND ece<base AND pf>=0.85*base_pf'})

### SOLUSDT
- **baseline_level_vsa**: lift=0.0982 ece=0.0054 level_p90=0.0281 control_PF=2.134745633040173
- **rare_level_strong**: lift=0.0985 ece=0.0074 level_p90=0.0282 control_PF=2.364790042496392
- **rare15_level_strong**: lift=0.0989 ece=0.0081 level_p90=0.0190 control_PF=1.378950549848718
- promote `rare_level_strong`: **False** ({'pr_auc_lift_improved': True, 'ece_improved': False, 'pf_not_collapsed': True, 'promote': False, 'base_pf': 2.134745633040173, 'new_pf': 2.364790042496392, 'base_lift': 0.09821662498584077, 'new_lift': 0.09850341161320755, 'base_ece': 0.005352879372836751, 'new_ece': 0.007404420516472974, 'level_p90': 0.028155358547640882, 'rule': 'lift>base AND ece<base AND pf>=0.85*base_pf'})
- promote `rare15_level_strong`: **False** ({'pr_auc_lift_improved': True, 'ece_improved': False, 'pf_not_collapsed': False, 'promote': False, 'base_pf': 2.134745633040173, 'new_pf': 1.378950549848718, 'base_lift': 0.09821662498584077, 'new_lift': 0.09892980700885473, 'base_ece': 0.005352879372836751, 'new_ece': 0.008136822091538957, 'level_p90': 0.019033482241654236, 'rule': 'lift>base AND ece<base AND pf>=0.85*base_pf'})
