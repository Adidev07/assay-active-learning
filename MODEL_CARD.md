# Model / system card

## Intended use

Select informative points on a purely mathematical assay response surface using a Gaussian-process surrogate. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Use a fixed RBF kernel and Gaussian observation-noise term to compute posterior mean and variance. Sequentially choose the largest upper confidence bound among unobserved candidates.

## Evaluation protocol

Compare best true response found over a fixed query budget with seeded random selection. Both policies start from the same five points; hold the synthetic objective fixed.

## Known limits

Axes are dimensionless mathematical descriptors, not temperatures, doses, biological targets or instructions for a real experiment. Hyperparameters are fixed and no optimality guarantee is claimed.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Add repeated-seed comparisons, noisy objectives, cost-aware acquisition and domain-approved real data with a separate prospective validation plan.
