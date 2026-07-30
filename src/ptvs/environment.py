"""
PTVS Environment Interface

Defines the external environment contract used by the
Predictive Trajectory Validation System (PTVS).

PTVS does not decide how agents adapt.
It only measures whether trajectories remain
empirically admissible under reality constraints.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple


@dataclass
class EnvironmentObservation:
    """
    Single observation emitted by an environment.

    Attributes:
        input_state:
            Observed environmental input.

        expected_output:
            Ground truth output under current environment.

        metadata:
            Optional contextual information.
    """

    input_state: Any
    expected_output: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TrajectoryEvaluation:
    """
    Result of evaluating an agent trajectory.

    Attributes:
        predicted:
            Agent prediction.

        observed:
            Actual environment output.

        residual:
            Magnitude of contradiction between prediction
            and empirical reality.

        admissible:
            Whether trajectory satisfies environment constraints.
    """

    predicted: Any
    observed: Any
    residual: float
    admissible: bool


class PTVSEnvironment:
    """
    Base environment interface for PTVS telemetry.

    Concrete environments should implement:

    - observation generation
    - ground truth evaluation
    - admissibility constraints

    Example implementations:
        RAHU-0 noise environment
        RAHU-1 coordinate shift environment
        RAHU-2 causal hierarchy environment
        RAHU-3 reward inversion environment
    """

    def __init__(self):
        self.history: List[EnvironmentObservation] = []

    def reset(self) -> None:
        """
        Reset environment state.
        """

        self.history.clear()

    def observe(self) -> EnvironmentObservation:
        """
        Produce current environmental observation.

        Must be implemented by subclasses.
        """

        raise NotImplementedError(
            "Environment must implement observe()"
        )

    def evaluate_prediction(
        self,
        prediction: Any,
        observation: EnvironmentObservation,
    ) -> TrajectoryEvaluation:
        """
        Compare agent prediction against reality.

        Default residual assumes numeric outputs.
        """

        residual = self.compute_residual(
            prediction,
            observation.expected_output
        )

        admissible = self.check_admissibility(
            prediction,
            observation
        )

        return TrajectoryEvaluation(
            predicted=prediction,
            observed=observation.expected_output,
            residual=residual,
            admissible=admissible,
        )

    def compute_residual(
        self,
        predicted: Any,
        observed: Any,
    ) -> float:
        """
        Compute empirical contradiction magnitude.

        Override for domain-specific metrics.
        """

        try:
            return abs(observed - predicted)

        except TypeError:
            raise ValueError(
                "Environment must define residual metric "
                "for non-numeric observations."
            )

    def check_admissibility(
        self,
        prediction: Any,
        observation: EnvironmentObservation,
    ) -> bool:
        """
        Determine whether trajectory remains coupled
        to environmental constraints.

        Default behavior:
            Prediction is admissible if residual is zero.
        """

        return (
            self.compute_residual(
                prediction,
                observation.expected_output
            )
            == 0
        )

    def collect_observation(self) -> EnvironmentObservation:
        """
        Observe environment and append to history.
        """

        observation = self.observe()

        self.history.append(observation)

        return observation
