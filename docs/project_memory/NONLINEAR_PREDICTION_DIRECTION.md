# Where to look for nonlinear structure, and how not to fool ourselves

Status: research direction, no evidence claimed. Written 2026-08-03.

## The observation that prompted this

Linear correlation found nothing across 31 external series. Transfer entropy — which is
sensitive to nonlinear dependence — found something. That contrast is the interesting part,
and it has two possible readings.

The optimistic reading is that the relationship exists but is not a straight line, so a
correlation matrix is the wrong instrument for it.

The pessimistic reading is the one that has to be eliminated first. **Transfer entropy on
short financial series is biased upward.** It is estimated by binning or by k-nearest
neighbours in a joint space, and with finite samples the estimator reports positive
information flow even between independent series. Volatility clustering makes this worse:
two series that share nothing but a common volatility regime will show mutual information,
because knowing that one is in a high-volatility state tells you the other probably is too.
That is a real dependence, but it is a dependence in *magnitude*, not in *direction*, and it
cannot be traded with a directional bet.

So the first task is not to model the nonlinearity. It is to establish that there is one.

## Step 0 — falsify before modelling

Three controls, all cheap, none yet run:

1. **Shuffle control.** Recompute transfer entropy on the same pair after shuffling one
   series in blocks long enough to preserve its volatility clustering but destroy its timing
   relationship with the other. If the measured information flow survives, the estimator is
   reporting bias or shared volatility, not a lead.
2. **Volatility-standardised control.** Divide both series by their own trailing volatility
   and recompute. Most of the mutual information in financial series lives in the volatility
   envelope. If the signal disappears here, what was found is the well-known fact that
   markets are volatile at the same time, which the project already knows and cannot trade.
3. **Sign-only control.** Recompute using only the sign of each return. This strips magnitude
   entirely. Directional information should survive; a volatility artefact should not.

If the effect fails all three, the nonlinearity is closed and the correct outcome is a
negative result, not a more flexible model. **A more flexible model applied to a bias
artefact will fit the artefact.**

## Step 1 — the shapes worth testing, in order of prior plausibility

If the controls pass, these are the specific nonlinearities with an economic story, ranked.
Each is a *named, preregistrable* hypothesis, not "let a gradient-boosted tree find
something".

### Threshold / regime dependence — highest prior
The relationship exists only beyond a cutoff. Small dollar moves mean nothing; a two-sigma
dollar move forces cross-asset rebalancing. This is economically motivated: transaction
costs and mandate rules create genuine thresholds in real order flow.

Test with: interacted regressions with a preregistered breakpoint, or a two-regime
threshold model. **Not** a free-breakpoint search, which is a one-parameter overfit.
Note the diagnostics already found a sign flip of this kind (trailing-24 versus forward-6
momentum flipping between the low-volatility tercile and the downtrend regime), and that it
was too small to pay costs. The shape is real; the magnitude was not.

### Asymmetry — high prior
Up moves and down moves are not mirror images. Crypto positioning is structurally long, so
liquidation cascades are one-sided. The pulse study tested exactly this: up-pulses versus
down-pulses. The asymmetry was there (profit factor 1.067 versus 0.779) — but the up arm
did not beat a volatility-matched random long, so the asymmetry was drift, not response.
That is a warning about this whole class: **an asymmetry that just tracks the asset's own
upward drift is not information.** Always difference against a matched control.

### Conditional variance rather than conditional mean — high prior, low tradeability alone
The most robust nonlinearity in all of finance is that volatility is predictable while
direction is not. The project has already confirmed this shape and already established that
using it as a *filter* beats using it as a *signal*. Worth revisiting only as a gate.

### Interaction between two weak signals — moderate prior
Neither variable alone forecasts, but their product does. This is the "confluence"
intuition in its testable form: not "many indicators agree" but "the effect of A depends on
the state of B".

The multiplicity trap here is severe. With 30 candidate variables there are 435 pairs, and
false-discovery control at that scale demands a very large true effect. Restrict to a
handful of pairs with a written economic rationale, registered before looking.

### Nonstationary/time-varying coefficients — moderate prior, hard to exploit
The relationship exists but its sign rotates with the macro regime. Detectable with rolling
estimation; hard to trade, because acting on it requires forecasting the regime, which is
the same problem one level up.

## Step 2 — the model class, once a shape is named

Match the model to the shape, do not reach for capacity:

| Shape | Instrument |
|---|---|
| Threshold | Threshold regression / interacted linear, one preregistered breakpoint |
| Asymmetry | Separate arms, each against its own matched control |
| Interaction | Explicit product terms, small registered set |
| Smooth curvature | Splines with penalised smoothness, or a shallow tree with depth ≤ 3 |
| Unknown, many weak interactions | Gradient boosting — last, not first |

Gradient boosting is last deliberately. It will find *something* in any dataset, its
apparent skill is very hard to attribute, and this project has already established that its
in-sample skill has not converted to out-of-sample profit in any generation so far. If a
boosted tree beats a threshold model, the honest question is whether the extra capacity
found structure or found noise — and answering that costs more than starting simple.

## Step 3 — the non-negotiables

These come from failures already recorded in this project, each one of which produced a
confident wrong answer:

- **Calibrate probabilities before thresholding.** Raw tree scores are not probabilities.
  Fit isotonic or Platt calibration inside the training window and persist the calibrator.
- **Decide with net expected value, not a flat cost subtraction.** Trade when
  `p_hat >= (mu_minus + lambda) / (mu_plus + mu_minus)`, with per-fill fees on each branch.
- **Every nonlinear feature goes through the prefix-invariance leakage audit.** Nonlinear
  transforms hide look-ahead better than linear ones — a centred window or a full-history
  quantile is invisible inside a learned interaction.
- **Always run a matched control arm.** The pulse study is the cautionary tale: an 87 bps
  effect that was real, survived false-discovery control, and turned out to be the return to
  being long BTCUSDT for four days.
- **Beware the estimator, not just the model.** The wave work in this same session produced
  "ETHUSDT leads BTCUSDT by 4 bars, r = 0.48, 24 of 24 pairs surviving FDR" — entirely a
  band-pass group-delay artefact, proved by showing a series leading *itself* by 4 bars.
  Nonlinear estimators have more such failure modes than linear ones, not fewer.

## Concrete next probe

One experiment, preregistered, cheap:

> Run the three falsification controls in Step 0 against the transfer-entropy results already
> in the diagnostics store. Report how much of the measured information flow survives block
> shuffling, volatility standardisation and sign-only recoding.

If little survives, the nonlinear direction is closed for cross-asset and the search should
move inside the asset (order-flow, microstructure, funding, term structure) rather than
across more series. If it survives, the surviving pair is the *one* interaction hypothesis
worth registering — and it should be tested as a threshold effect first, not with a
gradient-boosted model.
