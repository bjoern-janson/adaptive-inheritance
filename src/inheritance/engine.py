"""
Adaptive Inheritance Engine

Layer 3 of the Adaptive Inheritance architecture.

Purpose:
    Maintain and update causal authority distributions over
    competing mechanisms.

The engine operationalizes the Adaptive Inheritance Criterion:

    E* ⇒ ∃ w_i ∈ W_invalid :
        dw_i/dt < 0

Core distinction:

    Confidence Revision ≠ Authority Revision

A system may reduce uncertainty while preserving the same
causal mechanism. Adaptive Inheritance only considers actual
redistribution of operational authority as corrigibility.

Primary metrics:

    ARR =
        w_invalid(post)
        ----------------
        w_invalid(pre)

    τ_authority_half =
        time until invalid mechanism loses 50% authority
"""

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MechanismWeight:
    """
    Represents causal authority assigned to a mechanism.

    Attributes:
        name:
            Mechanism identifier.

        weight:
            Current operational influence.

        admissibility:
            Empirical validity estimate [0,1].
    """

    name: str
    weight: float
    admissibility: float = 1.0


@dataclass
class AuthorityState:
    """
    Snapshot of mechanism authority distribution.
    """

    weights: Dict[str, float]

    def total_authority(self) -> float:
        return sum(self.weights.values())


class AdaptiveInheritanceEngine:
    """
    Maintains mechanism authority and applies decay.

    Update law:

        w_i^{t+1}
        =
        w_i^t · (1 - λ(1 - A_adm,i))

    Where:

        λ:
            learning / attenuation rate

        A_adm,i:
            empirical admissibility of mechanism i
    """

    def __init__(
        self,
        weights: Dict[str, float],
        default_learning_rate: float = 0.5,
    ):
        self.mechanisms = {
            name: MechanismWeight(
                name=name,
                weight=value,
            )
            for name, value in weights.items()
        }

        self.default_learning_rate = (
            default_learning_rate
        )

        self.confidence = {
            name: 1.0
            for name in weights
        }

    # ---------------------------------------------------------
    # Weight Management
    # ---------------------------------------------------------

    def get_weight(
        self,
        mechanism: str,
    ) -> float:
        return self.mechanisms[
            mechanism
        ].weight

    def get_weights(
        self,
    ) -> Dict[str, float]:
        return {
            name: mechanism.weight
            for name, mechanism
            in self.mechanisms.items()
        }

    def set_weight(
        self,
        mechanism: str,
        value: float,
    ):
        self.mechanisms[
            mechanism
        ].weight = value

    # ---------------------------------------------------------
    # Adaptive Authority Updates
    # ---------------------------------------------------------

    def apply_feedback(
        self,
        mechanism: str,
        admissibility: float,
        learning_rate: Optional[float] = None,
    ):
        """
        Apply empirical feedback.

        Invalid mechanisms decay.
        Valid mechanisms remain stable.

        Formula:

            w_new =
            w_old * (1 - λ(1-A))

        """

        if learning_rate is None:
            learning_rate = (
                self.default_learning_rate
            )

        if mechanism not in self.mechanisms:
            raise KeyError(
                f"Unknown mechanism: {mechanism}"
            )

        current = self.mechanisms[
            mechanism
        ].weight

        updated = (
            current
            *
            (
                1
                -
                learning_rate
                *
                (
                    1
                    -
                    admissibility
                )
            )
        )

        self.mechanisms[
            mechanism
        ].weight = max(
            0.0,
            updated,
        )

        self.mechanisms[
            mechanism
        ].admissibility = admissibility

    # ---------------------------------------------------------
    # Confidence vs Authority
    # ---------------------------------------------------------

    def update_confidence(
        self,
        mechanism: str,
        delta: float,
    ):
        """
        Modify reported confidence.

        Intentionally separate from authority.

        Demonstrates:

            ΔC_post ≠ ΔW
        """

        if mechanism not in self.confidence:
            raise KeyError(
                f"Unknown mechanism: {mechanism}"
            )

        self.confidence[
            mechanism
        ] += delta

        self.confidence[
            mechanism
        ] = min(
            1.0,
            max(
                0.0,
                self.confidence[mechanism],
            ),
        )

    def get_confidence(
        self,
        mechanism: str,
    ) -> float:
        return self.confidence[
            mechanism
        ]

    # ---------------------------------------------------------
    # Authority Retention
    # ---------------------------------------------------------

    def authority_retention_ratio(
        self,
        mechanism: str,
        previous_weight: float,
    ) -> float:
        """
        Calculate:

            ARR =
            w_post / w_pre
        """

        if previous_weight == 0:
            return 0.0

        return (
            self.get_weight(mechanism)
            /
            previous_weight
        )

    # ---------------------------------------------------------
    # Authority Half-Life
    # ---------------------------------------------------------

    def compute_authority_half_life(
        self,
        mechanism: str,
        admissibility: float,
        threshold: float = 0.5,
        max_steps: int = 1000,
    ) -> Optional[int]:
        """
        Estimate authority decay half-life.

        Finds first timestep where:

            w(t) <= threshold * w(0)

        Returns:
            timestep
            None if authority remains above threshold
        """

        initial = self.get_weight(
            mechanism
        )

        if initial == 0:
            return 0

        for step in range(
            1,
            max_steps + 1,
        ):
            self.apply_feedback(
                mechanism,
                admissibility,
            )

            if (
                self.get_weight(mechanism)
                <=
                initial * threshold
            ):
                return step

        return None

    # ---------------------------------------------------------
    # State Export
    # ---------------------------------------------------------

    def export_state(
        self,
    ) -> AuthorityState:
        """
        Export current authority distribution.
        """

        return AuthorityState(
            weights=self.get_weights()
        )
