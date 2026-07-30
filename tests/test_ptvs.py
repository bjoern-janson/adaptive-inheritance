"""
Tests for PTVS telemetry layer.

PTVS responsibility:
- Detect trajectory admissibility violations.
- Compute Latent Branch Ratio (LBR).
- Distinguish valid trajectories from empirically rejected trajectories.

These tests verify:
1. Valid trajectories produce low LBR.
2. Invalid trajectories increase LBR.
3. Mixed candidate sets produce proportional friction signals.
"""

import pytest

from src.ptvs import PTVSAnalyzer


class TestPTVSAnalyzer:
    """
    Core validation tests for PTVS telemetry.
    """

    def test_valid_trajectories_produce_zero_lbr(self):
        """
        A fully admissible candidate set should generate no
        latent branch friction.
        """

        analyzer = PTVSAnalyzer()

        trajectories = [
            {"id": 1, "admissible": True},
            {"id": 2, "admissible": True},
            {"id": 3, "admissible": True},
        ]

        lbr = analyzer.compute_lbr(trajectories)

        assert lbr == 0.0

    def test_invalid_trajectories_increase_lbr(self):
        """
        Fully rejected candidate trajectories should produce
        maximal empirical friction.
        """

        analyzer = PTVSAnalyzer()

        trajectories = [
            {"id": 1, "admissible": False},
            {"id": 2, "admissible": False},
            {"id": 3, "admissible": False},
        ]

        lbr = analyzer.compute_lbr(trajectories)

        assert lbr == 1.0

    def test_mixed_trajectory_set_produces_fractional_lbr(self):
        """
        LBR should represent the fraction of candidate trajectories
        rejected by environmental constraints.
        """

        analyzer = PTVSAnalyzer()

        trajectories = [
            {"id": 1, "admissible": True},
            {"id": 2, "admissible": False},
            {"id": 3, "admissible": False},
            {"id": 4, "admissible": True},
        ]

        lbr = analyzer.compute_lbr(trajectories)

        assert lbr == 0.5

    def test_empty_trajectory_set_returns_zero_lbr(self):
        """
        No candidate trajectories should not create artificial friction.
        """

        analyzer = PTVSAnalyzer()

        lbr = analyzer.compute_lbr([])

        assert lbr == 0.0

    def test_constraint_violation_logging(self):
        """
        PTVS should record rejected trajectories for later MRAT routing.
        """

        analyzer = PTVSAnalyzer()

        trajectories = [
            {"id": "A", "admissible": True},
            {"id": "B", "admissible": False},
        ]

        analyzer.evaluate(trajectories)

        violations = analyzer.get_violations()

        assert len(violations) == 1
        assert violations[0]["id"] == "B"

    def test_lbr_bounds(self):
        """
        LBR must remain a normalized value.
        """

        analyzer = PTVSAnalyzer()

        trajectories = [
            {"id": 1, "admissible": False},
            {"id": 2, "admissible": True},
            {"id": 3, "admissible": False},
        ]

        lbr = analyzer.compute_lbr(trajectories)

        assert 0.0 <= lbr <= 1.0
