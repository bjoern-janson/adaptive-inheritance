"""
MRAT Router Module

Minimal Residual Attribution Test.

Layer 2 of Adaptive Inheritance.

Purpose:
    Route empirical residuals to the lowest-cost structural
    explanation capable of restoring predictive alignment.

The routing operator:

    Φ_R(e_t) → a

where:

    a = (a_N, a_S, a_M, a_R, a_G)

and:

    Σ a_i = 1

Attribution dimensions:

    N = Noise
    S = State Error
    M = Mechanism Deficit
    R = Representation Saturation
    G = Generator Decoupling

MRAT enforces Adaptive Parsimony:

    Select the lowest-complexity intervention capable of
    restoring empirical coupling.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, Optional


class FailureLayer(Enum):
    """
    Possible residual attribution targets.

    Ordered by increasing adaptive cost.
    """

    NOISE = "N"
    STATE = "S"
    MECHANISM = "M"
    REPRESENTATION = "R"
    GENERATOR = "G"


@dataclass
class AttributionVector:
    """
    Continuous residual attribution distribution.

    Represents:

        Φ_R(e_t) → (a_N, a_S, a_M, a_R, a_G)

    Each value represents proportional attribution mass.
    """

    noise: float
    state: float
    mechanism: float
    representation: float
    generator: float

    def as_dict(self) -> Dict[str, float]:
        return {
            "N": self.noise,
            "S": self.state,
            "M": self.mechanism,
            "R": self.representation,
            "G": self.generator,
        }

    def validate(self) -> bool:
        """
        Validate simplex constraint:

            a_i ∈ [0,1]
            Σa_i = 1
        """

        values = [
            self.noise,
            self.state,
            self.mechanism,
            self.representation,
            self.generator,
        ]

        return (
            all(
                0.0 <= value <= 1.0
                for value in values
            )
            and abs(sum(values) - 1.0) < 1e-6
        )

    def dominant_layer(self) -> FailureLayer:
        """
        Discrete routing decision.

        Selects:

            argmax_i(a_i)
        """

        attribution = self.as_dict()

        dominant = max(
            attribution,
            key=attribution.get,
        )

        return {
            "N": FailureLayer.NOISE,
            "S": FailureLayer.STATE,
            "M": FailureLayer.MECHANISM,
            "R": FailureLayer.REPRESENTATION,
            "G": FailureLayer.GENERATOR,
        }[dominant]


class MRATRouter:
    """
    Minimal Residual Attribution Controller.

    Converts empirical residual telemetry into
    adaptive routing decisions.
    """

    def __init__(
        self,
        noise_threshold: float = 0.1,
        representation_threshold: float = 0.8,
        generator_threshold: float = 0.9,
    ):
        self.noise_threshold = noise_threshold
        self.representation_threshold = (
            representation_threshold
        )
        self.generator_threshold = (
            generator_threshold
        )

    def route(
        self,
        residual: float,
        *,
        noise_score: Optional[float] = None,
        state_score: Optional[float] = None,
        mechanism_score: Optional[float] = None,
        representation_score: Optional[float] = None,
        generator_score: Optional[float] = None,
    ) -> AttributionVector:
        """
        Compute continuous attribution vector.

        In production systems, scores may come from:
        - Bayesian diagnostics
        - ensemble disagreement
        - residual compressibility
        - causal probes

        This implementation provides a deterministic baseline.
        """

        if all(
            score is not None
            for score in [
                noise_score,
                state_score,
                mechanism_score,
                representation_score,
                generator_score,
            ]
        ):
            vector = AttributionVector(
                noise=noise_score,
                state=state_score,
                mechanism=mechanism_score,
                representation=representation_score,
                generator=generator_score,
            )

            if not vector.validate():
                raise ValueError(
                    "Attribution vector must sum to 1"
                )

            return vector

        return self._default_route(
            residual
        )

    def _default_route(
        self,
        residual: float,
    ) -> AttributionVector:
        """
        Conservative baseline routing.

        Low residual:
            noise dominated

        Moderate residual:
            mechanism dominated

        Persistent high residual:
            representation/generator dominated
        """

        if residual <= self.noise_threshold:
            return AttributionVector(
                noise=1.0,
                state=0.0,
                mechanism=0.0,
                representation=0.0,
                generator=0.0,
            )

        if residual < self.representation_threshold:
            return AttributionVector(
                noise=0.1,
                state=0.2,
                mechanism=0.7,
                representation=0.0,
                generator=0.0,
            )

        if residual < self.generator_threshold:
            return AttributionVector(
                noise=0.05,
                state=0.05,
                mechanism=0.1,
                representation=0.8,
                generator=0.0,
            )

        return AttributionVector(
            noise=0.02,
            state=0.03,
            mechanism=0.05,
            representation=0.2,
            generator=0.7,
        )

    def route_intervention(
        self,
        attribution: AttributionVector,
    ) -> FailureLayer:
        """
        Convert attribution into intervention target.

        The highest attribution mass receives authority
        for corrective action.
        """

        if not attribution.validate():
            raise ValueError(
                "Invalid attribution vector"
            )

        return attribution.dominant_layer()

    def adaptive_cost_level(
        self,
        layer: FailureLayer,
    ) -> int:
        """
        Return adaptive intervention hierarchy level.

        L0 Noise
        L1 State
        L2 Mechanism
        L3 Representation
        L4 Generator
        """

        return {
            FailureLayer.NOISE: 0,
            FailureLayer.STATE: 1,
            FailureLayer.MECHANISM: 2,
            FailureLayer.REPRESENTATION: 3,
            FailureLayer.GENERATOR: 4,
        }[layer]
