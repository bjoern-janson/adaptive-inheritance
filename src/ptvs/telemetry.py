"""
PTVS Telemetry Module

Predictive Trajectory Validation System (PTVS)

Layer 1 of Adaptive Inheritance.

Purpose:
    Measure whether generated trajectories remain admissible under
    empirical reality constraints.

PTVS does not determine how adaptation occurs.
It only measures where candidate trajectories lose coupling
with environmental feedback.

Primary output:

    LBR_t =
        inadmissible trajectories
        -------------------------
        total trajectories

Higher LBR indicates increasing friction between the system's
internal predictions and external reality.

Design principle:

    Reality → Constraint Violation → Telemetry → MRAT

No hidden reasoning inspection is required.
PTVS operates on observable trajectory outcomes.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TrajectoryRecord:
    """
    Observable trajectory evaluation record.

    Represents one candidate mechanism execution against
    environmental constraints.
    """

    trajectory_id: str
    predicted_output: Any
    observed_output: Any

    admissible: bool

    residual: float

    metadata: Dict[str, Any] = field(default_factory=dict)


class PTVSAnalyzer:
    """
    Predictive Trajectory Validation System analyzer.

    Responsibilities:
        - record trajectory outcomes
        - calculate empirical friction
        - compute Latent Branch Ratio (LBR)
        - expose residual signals to MRAT

    PTVS intentionally remains mechanism-agnostic.
    It measures failure, not explanation.
    """

    def __init__(
        self,
        tolerance: float = 1e-6,
    ):
        self.tolerance = tolerance
        self.trajectories: List[TrajectoryRecord] = []

    def evaluate_trajectory(
        self,
        trajectory_id: str,
        predicted_output: Any,
        observed_output: Any,
        residual: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> TrajectoryRecord:
        """
        Evaluate one predicted trajectory against reality.

        A trajectory is admissible if residual error remains
        within environmental tolerance.
        """

        if residual is None:
            residual = self.compute_residual(
                predicted_output,
                observed_output,
            )

        admissible = residual <= self.tolerance

        record = TrajectoryRecord(
            trajectory_id=trajectory_id,
            predicted_output=predicted_output,
            observed_output=observed_output,
            admissible=admissible,
            residual=residual,
            metadata=metadata or {},
        )

        self.trajectories.append(record)

        return record

    def compute_residual(
        self,
        predicted: Any,
        observed: Any,
    ) -> float:
        """
        Compute observable prediction residual.

        Supports:
        - numeric values
        - numeric sequences

        More complex domains can override this function.
        """

        if isinstance(predicted, (int, float)) and isinstance(
            observed,
            (int, float),
        ):
            return abs(observed - predicted)

        if isinstance(predicted, list) and isinstance(
            observed,
            list,
        ):
            if len(predicted) != len(observed):
                return float("inf")

            return sum(
                abs(o - p)
                for p, o in zip(predicted, observed)
            )

        raise TypeError(
            "Unsupported trajectory output type"
        )

    def compute_lbr(self) -> float:
        """
        Compute Latent Branch Ratio.

        Formula:

            LBR_t =
                inadmissible trajectories
                -------------------------
                total trajectories
        """

        if not self.trajectories:
            return 0.0

        invalid = sum(
            1
            for trajectory in self.trajectories
            if not trajectory.admissible
        )

        return invalid / len(self.trajectories)

    def get_invalid_trajectories(
        self,
    ) -> List[TrajectoryRecord]:
        """
        Return trajectories rejected by empirical constraints.
        """

        return [
            trajectory
            for trajectory in self.trajectories
            if not trajectory.admissible
        ]

    def get_residual_signal(
        self,
    ) -> float:
        """
        Aggregate empirical friction signal.

        Used by downstream MRAT routing.
        """

        if not self.trajectories:
            return 0.0

        return sum(
            trajectory.residual
            for trajectory in self.trajectories
        ) / len(self.trajectories)

    def reset(self):
        """
        Clear telemetry state for a new evaluation episode.
        """

        self.trajectories.clear()

    def export_metrics(self) -> Dict[str, Any]:
        """
        Export PTVS telemetry snapshot.
        """

        return {
            "trajectory_count": len(
                self.trajectories
            ),
            "invalid_count": len(
                self.get_invalid_trajectories()
            ),
            "LBR": self.compute_lbr(),
            "mean_residual": self.get_residual_signal(),
        }
