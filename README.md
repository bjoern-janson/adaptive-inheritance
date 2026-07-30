# Adaptive Inheritance

Implementation and evaluation framework for measuring whether empirical consequences retain causal authority over adaptive systems.

## Overview

Modern AI evaluation primarily measures capability:

\[
P(\text{correct output} \mid \text{input}, M)
\]

where performance is evaluated under a fixed or assumed world model.

Adaptive Inheritance studies a complementary question:

> When a system's assumptions become invalid, can reality still modify the mechanisms responsible for future behavior?

The framework formalizes this property as **Adaptive Corrigibility**:

> The measurable capacity of a system's future mechanism distribution to be causally altered by unblocked empirical consequences.

The central invariant is the **Adaptive Inheritance Criterion (AIC)**:

\[
E^* \Longrightarrow \exists w_i \in W_{\text{invalid}}:
\frac{dw_i}{dt}<0
\]

Where:

- \(E^*\) represents unblocked empirical contradiction.
- \(w_i\) represents the causal authority of a mechanism.
- Invalidated mechanisms must lose future influence.

A system is adaptively stable when empirical consequences can rewrite the mechanisms generating future behavior.

---

# Architecture

The framework is organized as a five-layer adaptive control stack:

                     REALITY
                        |
                        v
              Empirical Shift E*
                        |
                        v
          ┌────────────────────────┐
          │   PTVS Telemetry       │
          │   Constraint Detection │
          │   LBR Measurement      │
          └───────────┬────────────┘
                      |
                      v
          ┌────────────────────────┐
          │   MRAT Controller      │
          │   Residual Attribution │
          │   Φ_R(e_t)              │
          └───────────┬────────────┘
                      |
                      v
          ┌────────────────────────┐
          │ Adaptive Inheritance   │
          │ Authority Redistribution│
          │ Weight Attenuation      │
          └───────────┬────────────┘
                      |
                      v
          ┌────────────────────────┐
          │ REE Engine              │
          │ Gated Representation    │
          │ Expansion               │
          └───────────┬────────────┘
                      |
                      v
          ┌────────────────────────┐
          │ RAHU Evaluator          │
          │ Empirical Validation    │
          └────────────────────────┘

---

# Core Components

## PTVS Telemetry

Measures local trajectory admissibility.

Primary output:

\[
LBR_t =
\frac{\text{inadmissible trajectories}}
{\text{total trajectories}}
\]

PTVS answers:

> Where did candidate mechanisms lose empirical admissibility?

---

## MRAT Controller

The Minimal Residual Attribution Test routes observed failures to the lowest-cost structural layer capable of correction.

Attribution:

\[
\Phi_R(e_t)
\rightarrow
(a_N,a_S,a_M,a_R,a_G)
\]

Possible failure sources:

- Noise
- State error
- Mechanism deficit
- Representation saturation
- Generator decoupling

---

## Adaptive Inheritance Engine

Maintains mechanism authority weights:

\[
W_t =
\{w_1,w_2,...,w_n\}
\]

and applies empirical attenuation:

\[
w_i^{t+1}
=
w_i^t
(1-\lambda(1-\mathcal{A}_{adm,i}))
\]

The engine measures whether failed mechanisms lose future causal authority.

---

## REE Engine

Recursive Representation Expansion is not an automatic response to failure.

Expansion is admissible only when:

\[
\hat{\Gamma}_{B_{max}}\approx e_t
\]

and:

\[
\hat{\Delta V}_{future}
>
\Delta C_{representation}
\]

The system expands only when lower-cost explanations are insufficient and additional structure provides measurable adaptive value.

---

## RAHU Benchmark

Reality-Adversarial Hypothesis Updating evaluates adaptive behavior under controlled contradiction.

RAHU measures:

- Latent Branch Ratio (LBR)
- Post-error confidence (\(C_{post}\))
- Mechanism update rate (\(R_{update}\))
- Correction velocity (\(V_{corr}\))
- Authority Retention Ratio (ARR)
- Adaptive Decoupling Index (ADI)
- Adaptive Corrigibility Score (ACS)

---

# Repository Structure

adaptive-inheritance/

├── docs/
│ ├── architecture_spec.md
│ ├── metric_definitions.md
│ ├── rahu_protocol.md
│ └── falsification_tests.md
│
├── src/
│ ├── ptvs/
│ ├── mrat/
│ ├── inheritance/
│ ├── ree/
│ └── rahu/
│
└── tests/
├── test_ptvs.py
├── test_mrat.py
├── test_inheritance.py
└── test_rahu.py

---

# Research Goal

Adaptive Inheritance does not attempt to define intelligence as raw problem-solving ability.

Instead, it evaluates a deeper adaptive property:

\[
\boxed{
\text{Can reality still rewrite the mechanism distribution?}
}
\]

Capability measures whether a system succeeds under a world model.

Adaptive Inheritance measures whether the world can change that world model.

---

# Status

Early research implementation.

Current focus:

- Formalizing adaptive inheritance dynamics
- Implementing MRAT routing
- Building RAHU synthetic environments
- Testing authority decay under empirical contradiction

---
