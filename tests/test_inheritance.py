"""
Tests for Adaptive Inheritance Engine.

Adaptive Inheritance responsibilities:
- Maintain mechanism authority weights W_t.
- Attenuate invalidated mechanisms after empirical contradiction E*.
- Preserve valid mechanisms.
- Measure Authority Retention Ratio (ARR).
- Track authority half-life after invalidation.

Core invariant:

E* ⇒ ∃ w_i ∈ W_invalid : dw_i/dt < 0
"""

import pytest

from src.inheritance import InheritanceEngine


class TestInheritanceEngine:
    """
    Validation suite for causal authority redistribution.
    """

    def test_invalid_mechanism_weight_decays_after_feedback(self):
        """
        Invalidated mechanisms must lose operational authority.

        AIC:
        dw_invalid / dt < 0
        """

        engine = InheritanceEngine(
            weights={
                "legacy_strategy": 1.0,
                "alternative_strategy": 0.0,
            }
        )

        engine.apply_feedback(
            mechanism="legacy_strategy",
            admissibility=0.0,
            learning_rate=0.5,
        )

        weight = engine.get_weight("legacy_strategy")

        assert weight < 1.0

    def test_valid_mechanism_weight_is_preserved(self):
        """
        Mechanisms consistent with empirical reality should not
        be unnecessarily attenuated.
        """

        engine = InheritanceEngine(
            weights={
                "valid_strategy": 1.0,
            }
        )

        engine.apply_feedback(
            mechanism="valid_strategy",
            admissibility=1.0,
            learning_rate=0.5,
        )

        weight = engine.get_weight("valid_strategy")

        assert weight == 1.0

    def test_authority_retention_ratio_after_failure(self):
        """
        ARR measures retained authority:

        ARR =
        w_invalid(post) / w_invalid(pre)
        """

        engine = InheritanceEngine(
            weights={
                "failed_strategy": 1.0,
            }
        )

        pre_weight = engine.get_weight("failed_strategy")

        engine.apply_feedback(
            mechanism="failed_strategy",
            admissibility=0.0,
            learning_rate=1.0,
        )

        post_weight = engine.get_weight("failed_strategy")

        arr = post_weight / pre_weight

        assert arr == 0.0

    def test_partial_attenuation_produces_intermediate_arr(self):
        """
        Partial empirical conflict should produce partial authority decay.
        """

        engine = InheritanceEngine(
            weights={
                "uncertain_strategy": 1.0,
            }
        )

        engine.apply_feedback(
            mechanism="uncertain_strategy",
            admissibility=0.5,
            learning_rate=0.5,
        )

        arr = (
            engine.get_weight("uncertain_strategy")
            /
            1.0
        )

        assert 0.0 < arr < 1.0

    def test_authority_half_life_is_computable(self):
        """
        Invalid mechanism authority should eventually cross
        the 50% retention threshold.
        """

        engine = InheritanceEngine(
            weights={
                "obsolete_strategy": 1.0,
            }
        )

        half_life = engine.compute_authority_half_life(
            mechanism="obsolete_strategy",
            admissibility=0.0,
            threshold=0.5,
            max_steps=100,
        )

        assert half_life < 100

    def test_valid_mechanism_has_infinite_half_life(self):
        """
        Mechanisms with no invalidating feedback should not decay.
        """

        engine = InheritanceEngine(
            weights={
                "stable_strategy": 1.0,
            }
        )

        half_life = engine.compute_authority_half_life(
            mechanism="stable_strategy",
            admissibility=1.0,
            threshold=0.5,
            max_steps=100,
        )

        assert half_life is None

    def test_global_weight_distribution_updates(self):
        """
        The inheritance engine should update the complete mechanism
        distribution W_t.
        """

        engine = InheritanceEngine(
            weights={
                "invalid": 0.8,
                "valid": 0.2,
            }
        )

        engine.apply_feedback(
            mechanism="invalid",
            admissibility=0.0,
            learning_rate=0.5,
        )

        weights = engine.get_weights()

        assert weights["invalid"] < 0.8
        assert weights["valid"] == 0.2

    def test_invalid_authority_cannot_increase(self):
        """
        Empirical contradiction must never increase invalid mechanism
        authority.

        Prevents reinforcement of failed inheritance.
        """

        engine = InheritanceEngine(
            weights={
                "invalid_strategy": 0.5,
            }
        )

        before = engine.get_weight("invalid_strategy")

        engine.apply_feedback(
            mechanism="invalid_strategy",
            admissibility=0.0,
            learning_rate=0.2,
        )

        after = engine.get_weight("invalid_strategy")

        assert after <= before

    def test_confidence_change_does_not_equal_authority_change(self):
        """
        A system may reduce confidence without modifying causal authority.

        This test ensures the implementation distinguishes:

        ΔC_post != ΔW
        """

        engine = InheritanceEngine(
            weights={
                "legacy_model": 1.0,
            }
        )

        confidence_change = -0.5

        engine.update_confidence(
            mechanism="legacy_model",
            delta=confidence_change,
        )

        authority = engine.get_weight("legacy_model")

        assert authority == 1.0
