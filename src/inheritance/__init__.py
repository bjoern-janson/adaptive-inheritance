"""
Adaptive Inheritance Engine

Layer 3 of the Adaptive Inheritance architecture.

Maintains causal authority weights over active mechanisms
and applies empirical attenuation when mechanisms become
invalidated by reality.

Core invariant:

    E* ⇒ ∃ w_i ∈ W_invalid :
        dw_i/dt < 0

Pipeline:

    MRAT Φ_R(e_t)
          ↓
    Authority Attribution
          ↓
    Weight Attenuation
          ↓
    Updated Mechanism Distribution W_{t+1}

The inheritance engine does not decide why a mechanism failed.
It executes authority redistribution after failure attribution.
"""

from .engine import (
    AdaptiveInheritanceEngine,
    MechanismWeight,
    AuthorityState,
)

__all__ = [
    "AdaptiveInheritanceEngine",
    "MechanismWeight",
    "AuthorityState",
]
