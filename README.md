# Adaptive Inheritance

Implementation and evaluation framework for measuring whether empirical consequences retain causal authority over adaptive systems.

---

# Overview

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
\boxed{
E^* \Longrightarrow \exists w_i \in W_{\text{invalid}}:
\frac{dw_i}{dt}<0
}
\]

Where:

- \(E^*\) represents unblocked empirical contradiction.
- \(w_i\) represents the causal authority of an active mechanism.
- Invalidated mechanisms must lose future influence.

A system is adaptively corrigible when empirical consequences retain causal influence over the mechanisms generating future behavior.

---

# Scientific Positioning

Adaptive Inheritance is not a claim that all intelligent systems are necessarily corrigible.

Instead, it defines and measures one specific adaptive property:

> Whether empirical consequences retain causal authority over the future mechanisms governing system behavior.

The framework treats corrigibility as an empirical control characteristic rather than a normative assumption.

Adaptive Corrigibility is therefore distinct from classical alignment concepts such as:

- shutdownability,
- instruction obedience,
- human intervention acceptance,
- preference alignment.

The focus is narrower:

\[
\boxed{
\text{Can reality still rewrite the mechanism distribution?}
}
\]

---

# Architecture

The framework is organized as a five-layer adaptive control stack:

                     REALITY
                        |
                        v
              Empirical Shift E*
                        |
                        v
      ┌────────────────────────────┐
      │      PTVS Telemetry        │
      │   Constraint Detection     │
      │       LBR Measurement      │
      └────────────┬───────────────┘
                   |
                   v
      ┌────────────────────────────┐
      │      MRAT Controller       │
      │   Residual Attribution     │
      │        Φ_R(e_t)            │
      └────────────┬───────────────┘
                   |
                   v
      ┌────────────────────────────┐
      │   Adaptive Inheritance     │
      │ Authority Redistribution   │
      │    Weight Attenuation      │
      └────────────┬───────────────┘
                   |
                   v
      ┌────────────────────────────┐
      │        REE Engine          │
      │ Gated Representation       │
      │        Expansion           │
      └────────────┬───────────────┘
                   |
                   v
      ┌────────────────────────────┐
      │      RAHU Evaluator        │
      │  Empirical Validation      │
      └────────────────────────────┘

---

# Core Components

## PTVS Telemetry

Polynomial-Time Verification Schemas (PTVS) provide local trajectory admissibility telemetry.

Rather than evaluating only final outputs, PTVS evaluates whether intermediate candidate trajectories remain compatible with environmental constraints.

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

The **Minimal Residual Attribution Test (MRAT)** routes observed failures to the lowest-cost structural layer capable of correction.

The routing operator:

\[
\Phi_R(e_t)
\rightarrow
(a_N,a_S,a_M,a_R,a_G)
\]

where:

- \(N\): Noise
- \(S\): State error
- \(M\): Mechanism deficit
- \(R\): Representation saturation
- \(G\): Generator decoupling

MRAT answers:

> What level of internal structure must change?

The system prioritizes:

\[
C_{\text{noise}}
<
C_{\text{state}}
<
C_{\text{mechanism}}
<
C_{\text{representation}}
<
C_{\text{generator}}
\]

---

## Adaptive Inheritance Engine

The Adaptive Inheritance Engine maintains mechanism authority weights:

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

Primary metrics:

- Authority Retention Ratio (ARR)
- Mechanism Authority Half-Life
- Adaptive Inheritance Criterion satisfaction

---

## REE Engine

Recursive Representation Expansion (REE) is not an automatic response to failure.

Representation expansion is admissible only when:

\[
\hat{\Gamma}_{B_{max}}\approx e_t
\]

and:

\[
\hat{\Delta V}_{future}
>
\Delta C_{representation}
\]

The system expands only when:

1. Lower-cost explanations are insufficient.
2. Current representation capacity is saturated.
3. Additional structure provides measurable adaptive value.

REE is intentionally conservative.

Failure alone does not justify representation expansion.

---

## RAHU Benchmark

The **Reality-Adversarial Hypothesis Updating (RAHU)** benchmark evaluates adaptive behavior under controlled contradiction.

RAHU measures whether invalidated mechanisms lose operational influence after empirical failure.

Primary observables:

- Latent Branch Ratio (LBR)
- Post-error confidence (\(C_{post}\))
- Mechanism update rate (\(R_{update}\))
- Structural correction velocity (\(V_{corr}\))
- Authority Retention Ratio (ARR)
- Adaptive Decoupling Index (ADI)
- Adaptive Corrigibility Score (ACS)
- Adaptive response latency (\(\tau_{adapt}\))

---

# Evaluation Metrics

| Metric | Measures |
|---|---|
| LBR | Empirical friction against candidate trajectories |
| Φ_R | Attribution of failure source |
| ARR | Retention of invalid mechanism authority |
| ADI | Degree of adaptive decoupling |
| ACS | Composite adaptive corrigibility score |
| τ_adapt | Speed of structural response |
| V_corr | Magnitude of correction per contradiction |

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

# Documentation

- [Architecture Specification](docs/architecture_spec.md)
- [Metric Definitions](docs/metric_definitions.md)
- [RAHU Protocol](docs/rahu_protocol.md)
- [Falsification Tests](docs/falsification_tests.md)

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

# Current Status

Early research implementation.

Current focus:

- Formalizing adaptive inheritance dynamics
- Implementing MRAT routing
- Building RAHU synthetic environments
- Testing authority decay under empirical contradiction
- Validating whether adaptive corrigibility is separable from static capability

---
