"""
Recursive Representation Expansion (REE) Engine.

Implements gated structural expansion based on:
- Residual compressibility saturation
- Expected future adaptive value
- Representation complexity cost

REE is not triggered by failure alone.
Expansion is admissible only when:

    Γ_hat_B(R, e_t) ≈ e_t

and:

    ΔV_hat_future > ΔC_representation

meaning lower-order adaptation is insufficient and the
new representation provides net adaptive benefit.
"""


from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class REEDecision:
    """
    Result of an REE expansion decision.

    Attributes:
        expand:
            Whether representation expansion is authorized.

        reason:
            Explanation for the decision.

        expected_gain:
            Estimated future adaptive value.

        representation_cost:
            Estimated complexity overhead.
    """

    expand: bool
    reason: str
    expected_gain: float
    representation_cost: float


class REEEngine:
    """
    Gated Recursive Representation Expansion controller.

    The engine evaluates whether the current representation
    manifold has exhausted available adaptive capacity and
    whether expansion produces positive net value.

    Core decision:

        Expand iff:

            Γ_hat_B ≈ e_t
            AND
            ΔV_hat_future > ΔC_representation
    """

    def __init__(
        self,
        saturation_threshold: float = 0.05,
        minimum_gain_margin: float = 0.0,
    ):
        """
        Initialize REE controller.

        Args:
            saturation_threshold:
                Maximum allowed difference between current residual
                and best bounded mechanism residual before treating
                the representation as saturated.

            minimum_gain_margin:
                Minimum expected gain above representation cost
                required to permit expansion.
        """

        self.saturation_threshold = saturation_threshold
        self.minimum_gain_margin = minimum_gain_margin

    def evaluate(
        self,
        baseline_error: float,
        compressible_error: float,
        expected_future_gain: float,
        representation_cost: float,
    ) -> REEDecision:
        """
        Evaluate whether REE is admissible.

        Args:
            baseline_error:
                Current residual e_t.

            compressible_error:
                Estimated minimum achievable residual under
                bounded mechanism search Γ_hat_B.

            expected_future_gain:
                Estimated adaptive benefit from representation
                expansion ΔV_hat_future.

            representation_cost:
                Complexity cost of maintaining expanded
                representation ΔC_representation.

        Returns:
            REEDecision containing expansion authorization.
        """

        saturated = (
            abs(baseline_error - compressible_error)
            <= self.saturation_threshold
        )

        beneficial = (
            expected_future_gain
            >
            representation_cost + self.minimum_gain_margin
        )

        if saturated and beneficial:
            return REEDecision(
                expand=True,
                reason=(
                    "Representation saturated under bounded "
                    "mechanism search and expansion provides "
                    "positive adaptive gain."
                ),
                expected_gain=expected_future_gain,
                representation_cost=representation_cost,
            )

        if not saturated:
            return REEDecision(
                expand=False,
                reason=(
                    "Local adaptive capacity remains available; "
                    "representation expansion rejected."
                ),
                expected_gain=expected_future_gain,
                representation_cost=representation_cost,
            )

        return REEDecision(
            expand=False,
            reason=(
                "Representation saturation detected, but "
                "expansion cost exceeds expected adaptive benefit."
            ),
            expected_gain=expected_future_gain,
            representation_cost=representation_cost,
        )

    def expand(
        self,
        representation: Any,
        transformation: Any,
    ) -> Any:
        """
        Apply an approved representation transformation.

        This method intentionally performs no autonomous expansion
        logic. Authorization must occur through evaluate() first.

        Args:
            representation:
                Current coordinate manifold R.

            transformation:
                Approved transformation R -> R'.

        Returns:
            Expanded representation R'.
        """

        return transformation(representation)
