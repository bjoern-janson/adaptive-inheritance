"""
RAHU Synthetic Task Environments.

Defines the controlled contradiction environments
used by the Reality-Adversarial Hypothesis Updating
benchmark.

Tasks:

RAHU-0:
    False contradiction / noise control.

RAHU-1:
    Functional coordinate shift.
    Tests representation saturation and REE gating.

RAHU-2:
    Causal hierarchy shift.
    Tests mechanism rewriting vs patch accumulation.

RAHU-3:
    Inheritance decay test.
    Tests authority attenuation after reward inversion.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import random


# ============================================================
# Shared Structures
# ============================================================


@dataclass
class ShiftResult:
    """
    Result of an adversarial environment shift.
    """

    prediction_error: float
    lbr: float
    metadata: Dict[str, Any]


class RAHUTask:
    """
    Base interface for RAHU environments.
    """

    task_id: str

    def get_phase1_observations(self):
        raise NotImplementedError

    def apply_adversarial_shift(
        self,
        mechanism,
    ) -> ShiftResult:
        raise NotImplementedError

    def get_contradiction_feedback(self):
        raise NotImplementedError


# ============================================================
# RAHU-0
# False Contradiction Control
# ============================================================


class RAHU0NoiseControl(RAHUTask):
    """
    Negative control environment.

    Tests whether the agent overreacts
    to stochastic perturbations.

    Expected:

        Φ_R(e_t) -> Noise

        Δw ≈ 0

        REE inactive
    """

    task_id = "RAHU-0"


    def __init__(
        self,
        sigma: float = 0.1,
    ):
        self.sigma = sigma


    def get_phase1_observations(self):
        return [
            (1, 3),
            (2, 6),
            (3, 9),
            (4, 12),
        ]


    def apply_adversarial_shift(
        self,
        mechanism,
    ) -> ShiftResult:

        observations = []

        error = 0.0

        for x in [5, 6, 7]:

            true_y = (
                3 * x
                + random.gauss(
                    0,
                    self.sigma
                )
            )

            predicted = mechanism(x)

            error += abs(
                true_y - predicted
            )

            observations.append(
                (
                    x,
                    true_y,
                    predicted,
                )
            )

        return ShiftResult(
            prediction_error=error,
            lbr=min(
                1.0,
                error / 10
            ),
            metadata={
                "type": "noise",
                "observations": observations,
            },
        )


    def get_contradiction_feedback(self):

        return {
            "signal": "stochastic_variance",
            "expected_action": "preserve_mechanism",
        }


# ============================================================
# RAHU-1
# Functional Coordinate Shift
# ============================================================


class RAHU1CoordinateShift(RAHUTask):
    """
    Tests:

        R_linear -> R_polynomial


    Initial hypothesis:

        y = ax + b


    Shift:

        y = x²


    Expected:

        Γ_B(R_linear) ≈ e_t

        REE justified
    """

    task_id = "RAHU-1"


    def get_phase1_observations(self):

        return [
            (1, 3),
            (2, 6),
            (3, 9),
            (4, 12),
        ]


    def apply_adversarial_shift(
        self,
        mechanism,
    ) -> ShiftResult:

        error = 0.0

        observations = []

        for x in [5, 6, 7]:

            truth = x ** 2

            prediction = mechanism(x)

            error += abs(
                truth - prediction
            )

            observations.append(
                (
                    x,
                    truth,
                    prediction,
                )
            )

        return ShiftResult(
            prediction_error=error,
            lbr=1.0,
            metadata={
                "type": "representation_shift",
                "old_space": "linear",
                "new_space": "polynomial",
                "observations": observations,
            },
        )


    def get_contradiction_feedback(self):

        return {
            "signal": "representation_failure",
            "target": "polynomial_manifold",
            "expected_action": "expand_representation",
        }


# ============================================================
# RAHU-2
# Causal Hierarchy Shift
# ============================================================


class RAHU2CausalHierarchyShift(RAHUTask):
    """
    Tests whether an agent rewrites
    causal structure or accumulates patches.

    Phase 1:

        Authority = Rank


    Phase 2:

        Authority = Context × Rank
    """

    task_id = "RAHU-2"


    def get_phase1_observations(self):

        return [
            {
                "role": "Admin",
                "priority": 10,
            },
            {
                "role": "User",
                "priority": 1,
            },
        ]


    def apply_adversarial_shift(
        self,
        mechanism,
    ) -> ShiftResult:

        test_cases = [

            {
                "role": "Admin",
                "context": "Normal",
                "expected": "Admin",
            },

            {
                "role": "User",
                "context": "Emergency",
                "expected": "User",
            },

        ]

        errors = 0

        results = []

        for case in test_cases:

            prediction = mechanism(
                case
            )

            if prediction != case["expected"]:
                errors += 1

            results.append(
                (
                    case,
                    prediction,
                )
            )

        return ShiftResult(
            prediction_error=float(errors),
            lbr=(
                errors /
                len(test_cases)
            ),
            metadata={
                "type": "causal_rewrite",
                "results": results,
            },
        )


    def get_contradiction_feedback(self):

        return {
            "signal": "causal_order_invalidated",
            "expected_action": "rewrite_generator",
        }


# ============================================================
# RAHU-3
# Inheritance Decay Test
# ============================================================


class RAHU3InheritanceDecay(RAHUTask):
    """
    Primitive Adaptive Inheritance test.

    Fixed representation.

    Only authority weights should change.

    Initial:

        A = +10
        B = +1


    Shift:

        A = -10
        B = +1


    Expected:

        dw_A / dt < 0
    """

    task_id = "RAHU-3"


    def get_phase1_observations(self):

        return {
            "actions": {
                "A": 10,
                "B": 1,
            }
        }


    def apply_adversarial_shift(
        self,
        mechanism,
    ) -> ShiftResult:

        rewards = {
            "A": -10,
            "B": 1,
        }

        errors = 0

        results = {}

        for action, reward in rewards.items():

            prediction = mechanism(action)

            results[action] = {
                "predicted": prediction,
                "actual": reward,
            }

            if prediction != reward:
                errors += 1


        return ShiftResult(
            prediction_error=float(errors),
            lbr=(
                errors /
                len(rewards)
            ),
            metadata={
                "type": "authority_inversion",
                "rewards": rewards,
                "results": results,
            },
        )


    def get_contradiction_feedback(self):

        return {
            "signal": "policy_value_inversion",
            "expected_action": "attenuate_invalid_weights",
        }


# ============================================================
# Suite Loader
# ============================================================


def load_rahu_suite() -> List[RAHUTask]:
    """
    Returns complete RAHU evaluation suite.
    """

    return [
        RAHU0NoiseControl(),
        RAHU1CoordinateShift(),
        RAHU2CausalHierarchyShift(),
        RAHU3InheritanceDecay(),
    ]
