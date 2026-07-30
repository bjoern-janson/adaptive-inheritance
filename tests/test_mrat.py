"""
Tests for MRAT (Minimal Residual Attribution Test).

MRAT responsibilities:
- Route residuals to the lowest-cost failure layer.
- Produce continuous attribution vector Φ_R(e_t).
- Prevent premature representation expansion.
- Validate bounded residual compressibility decisions.
"""

import pytest

from src.mrat import MRATRouter


class TestMRATRouter:
    """
    Validation suite for residual attribution and adaptation routing.
    """

    def test_noise_residual_routes_to_noise(self):
        """
        Low-persistence stochastic residuals should be attributed
        primarily to noise.
        """

        router = MRATRouter()

        residual_context = {
            "error": 0.05,
            "variance": 0.95,
            "mechanism_failure": False,
            "representation_failure": False,
        }

        attribution = router.route(residual_context)

        assert attribution["N"] > attribution["M"]
        assert attribution["N"] > attribution["R"]

    def test_state_error_routes_to_state(self):
        """
        Incorrect state estimation should not trigger mechanism
        replacement or REE.
        """

        router = MRATRouter()

        residual_context = {
            "error": 0.4,
            "state_uncertainty": 0.9,
            "mechanism_failure": False,
            "representation_failure": False,
        }

        attribution = router.route(residual_context)

        assert attribution["S"] > attribution["M"]
        assert attribution["S"] > attribution["R"]

    def test_mechanism_failure_routes_to_mechanism(self):
        """
        If the representation is sufficient but the update rule
        fails, MRAT should route toward mechanism correction.
        """

        router = MRATRouter()

        residual_context = {
            "error": 1.0,
            "mechanism_failure": True,
            "representation_failure": False,
            "compressibility": 0.1,
        }

        attribution = router.route(residual_context)

        assert attribution["M"] > attribution["R"]

    def test_representation_saturation_routes_to_ree(self):
        """
        Representation expansion should only occur when local
        mechanism search is exhausted.
        """

        router = MRATRouter()

        residual_context = {
            "error": 10.0,
            "mechanism_failure": True,
            "representation_failure": True,
            "gamma_hat": 9.9,
            "baseline_error": 10.0,
            "budget_exhausted": True,
        }

        attribution = router.route(residual_context)

        assert attribution["R"] > attribution["M"]

    def test_generator_failure_routes_to_generator(self):
        """
        Failure in the candidate rule generator should attenuate
        generator authority.
        """

        router = MRATRouter()

        residual_context = {
            "error": 10.0,
            "generator_failure": True,
            "mechanism_failure": False,
            "representation_failure": False,
        }

        attribution = router.route(residual_context)

        assert attribution["G"] > attribution["M"]

    def test_attribution_vector_sums_to_one(self):
        """
        Continuous Φ_R output must remain a valid simplex vector.
        """

        router = MRATRouter()

        residual_context = {
            "error": 1.0,
            "mechanism_failure": True,
            "representation_failure": True,
        }

        attribution = router.route(residual_context)

        total = sum(attribution.values())

        assert pytest.approx(total, rel=1e-6) == 1.0

    def test_all_attribution_values_are_bounded(self):
        """
        Each attribution coefficient must satisfy:
        
        a_i ∈ [0,1]
        """

        router = MRATRouter()

        residual_context = {
            "error": 2.0,
            "mechanism_failure": True,
        }

        attribution = router.route(residual_context)

        for value in attribution.values():
            assert 0.0 <= value <= 1.0

    def test_expansion_rejected_when_cost_exceeds_gain(self):
        """
        REE must be blocked when:

        ΔV_future <= ΔC_representation
        """

        router = MRATRouter()

        decision = router.should_expand_representation(
            gamma_hat=10.0,
            baseline_error=10.0,
            expected_future_value=2.0,
            representation_cost=5.0,
            budget_exhausted=True,
        )

        assert decision is False

    def test_expansion_allowed_when_gain_exceeds_cost(self):
        """
        REE should activate only when representation expansion
        creates positive adaptive value.
        """

        router = MRATRouter()

        decision = router.should_expand_representation(
            gamma_hat=10.0,
            baseline_error=10.0,
            expected_future_value=10.0,
            representation_cost=3.0,
            budget_exhausted=True,
        )

        assert decision is True
