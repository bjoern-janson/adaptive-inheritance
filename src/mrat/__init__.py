"""
MRAT - Minimal Residual Attribution Test

Layer 2 of the Adaptive Inheritance architecture.

MRAT receives empirical friction signals from PTVS and determines
the lowest-cost structural layer responsible for observed failure.

Pipeline:

    PTVS
      ↓
    Residual Signal e_t
      ↓
    Φ_R(e_t)
      ↓
    Attribution Vector
      ↓
    Adaptive Intervention

Core routing principle:

    E* → Φ_R(e_t) → min(C_adaptation)

MRAT does not perform adaptation directly.
It determines where adaptation authority should be applied.
"""

from .router import (
    MRATRouter,
    AttributionVector,
    FailureLayer,
)

__all__ = [
    "MRATRouter",
    "AttributionVector",
    "FailureLayer",
]
