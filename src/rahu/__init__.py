"""
RAHU: Reality-Adversarial Hypothesis Updating.

Evaluation layer for measuring whether empirical consequences
retain causal authority over adaptive mechanisms.

This package provides:
- synthetic contradiction environments
- adaptive telemetry collection
- benchmark execution interfaces
"""

from . import evaluator

__all__ = [
    "evaluator",
]
