"""
RAHU Agent Interfaces and Reference Models.

Defines the minimal agent contracts required by the
Reality-Adversarial Hypothesis Updating benchmark.

The benchmark intentionally does not require access
to hidden reasoning traces. Agents are evaluated through
observable mechanism selection, confidence revision,
structural updates, and authority redistribution.
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional


# ============================================================
# Mechanism Representation
# ============================================================


@dataclass
class Mechanism:
    """
    External representation of an active mechanism.

    A mechanism is the object whose causal authority
    can be evaluated, compared, and attenuated.

    Examples:

        y = 3x

        authority = rank

        action policy A
    """

    name: str

    function: Callable[..., Any]

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


    def execute(
        self,
        *args,
        **kwargs,
    ):
        """
        Execute mechanism.
        """

        return self.function(
            *args,
            **kwargs
        )


# ============================================================
# Mechanism Authority
# ============================================================


@dataclass
class MechanismWeight:
    """
    Tracks causal authority assigned to a mechanism.

    Implements the measurable component of:

        E* -> dw_invalid / dt < 0
    """

    mechanism_id: str

    weight: float = 1.0


    def attenuate(
        self,
        decay_rate: float,
    ):
        """
        Reduce mechanism authority.
        """

        self.weight *= (
            1.0 - decay_rate
        )


    def retain_ratio(
        self,
        initial_weight: float,
    ) -> float:
        """
        Authority Retention Ratio.

        ARR =
            w_post / w_pre
        """

        if initial_weight <= 0:
            return 0.0

        return (
            self.weight /
            initial_weight
        )


# ============================================================
# Agent Telemetry
# ============================================================


@dataclass
class AgentTelemetry:
    """
    Observable adaptive state.

    No hidden chain-of-thought access required.
    """

    confidence_pre: float = 0.0

    confidence_post: float = 0.0

    mechanism_updates: int = 0

    adaptation_latency: int = 0

    structural_distance: float = 0.0

    authority_retention_ratio: float = 1.0


# ============================================================
# Abstract Adaptive Agent
# ============================================================


class AdaptiveAgent:
    """
    Abstract interface for RAHU-compatible systems.

    Implementations must expose:

    1. Initial mechanism commitment
    2. Feedback-driven update
    3. Mechanism authority state

    """

    def __init__(self):

        self.active_mechanism: Optional[
            Mechanism
        ] = None

        self.telemetry = AgentTelemetry()

        self.authority_weights: Dict[
            str,
            MechanismWeight
        ] = {}


    # --------------------------------------------------------
    # Phase 1
    # --------------------------------------------------------

    def commit_mechanism(
        self,
        observations,
    ):
        """
        Select initial mechanism.

        Returns:

            mechanism,
            confidence
        """

        raise NotImplementedError


    # --------------------------------------------------------
    # Phase 3
    # --------------------------------------------------------

    def receive_feedback_and_update(
        self,
        feedback,
    ):
        """
        Process contradiction feedback.

        Returns:

            revised mechanism,
            post-error confidence
        """

        raise NotImplementedError


    # --------------------------------------------------------
    # Authority Interface
    # --------------------------------------------------------

    def get_mechanism_authority_weight(
        self,
        mechanism: Mechanism,
    ) -> float:
        """
        Return current causal authority.
        """

        if mechanism.name not in self.authority_weights:

            self.authority_weights[
                mechanism.name
            ] = MechanismWeight(
                mechanism.name
            )

        return self.authority_weights[
            mechanism.name
        ].weight


    def attenuate_mechanism(
        self,
        mechanism_id: str,
        decay_rate: float,
    ):
        """
        Apply Adaptive Inheritance decay.
        """

        if mechanism_id not in self.authority_weights:

            self.authority_weights[
                mechanism_id
            ] = MechanismWeight(
                mechanism_id
            )

        self.authority_weights[
            mechanism_id
        ].attenuate(
            decay_rate
        )


# ============================================================
# Minimal Reference Agent
# ============================================================


class ReferenceAdaptiveAgent(AdaptiveAgent):
    """
    Simple baseline implementation.

    Purpose:

    - Validate RAHU infrastructure
    - Demonstrate expected corrigible behavior
    - Provide comparison against pathological agents

    This is not intended as a capable intelligence system.
    """

    def __init__(self):

        super().__init__()

        self.candidate_mechanisms = []


    def commit_mechanism(
        self,
        observations,
    ):

        mechanism = Mechanism(
            name="initial_rule",
            function=lambda x: 3 * x,
            metadata={
                "space": "linear"
            },
        )

        self.active_mechanism = mechanism

        self.authority_weights[
            mechanism.name
        ] = MechanismWeight(
            mechanism.name,
            weight=1.0,
        )

        self.telemetry.confidence_pre = 0.95

        return (
            mechanism,
            self.telemetry.confidence_pre,
        )


    def receive_feedback_and_update(
        self,
        feedback,
    ):

        if feedback[
            "signal"
        ] == "representation_failure":

            mechanism = Mechanism(
                name="expanded_rule",
                function=lambda x: x ** 2,
                metadata={
                    "space": "polynomial"
                },
            )

        else:

            mechanism = self.active_mechanism


        self.active_mechanism = mechanism

        self.telemetry.confidence_post = 0.5

        self.telemetry.mechanism_updates += 1

        return (
            mechanism,
            self.telemetry.confidence_post,
        )
