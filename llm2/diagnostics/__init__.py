"""Descriptive measurement layer.

These modules answer "what structure is present in the data" with numbers and uncertainty.
They do not select strategies, do not rank candidates for deployment and never read past
the training cutoff they are given. Anything they surface becomes a preregistered
hypothesis before it is allowed near the nested walk-forward.
"""
