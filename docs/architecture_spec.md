# Adaptive Inheritance Engine
# Architecture Specification

## 1. Purpose

This document defines the software architecture implementing the Adaptive Inheritance framework.

The system is designed to evaluate and control whether empirical consequences retain causal authority over an adaptive system's future mechanism distribution.

The core architectural objective is:

\[
E^* \longrightarrow \Phi_R(e_t) \longrightarrow \Delta \mathbf{W} \longrightarrow \mathbf{W}_{t+1}
\]

where:

- \(E^*\) = unblocked empirical contradiction
- \(\Phi_R(e_t)\) = residual attribution operator
- \(\Delta \mathbf{W}\) = mechanism authority redistribution
- \(\mathbf{W}_{t+1}\) = updated future mechanism distribution

The implementation separates five responsibilities:

1. Constraint failure detection
2. Residual attribution
3. Authority redistribution
4. Representation expansion gating
5. Empirical validation

---

# 2. Foundational Invariant

## Adaptive Inheritance Criterion (AIC)

The system is evaluated against:

\[
\boxed{
E^* \Longrightarrow \exists w_i \in \mathbf{W}_{invalid} :
\frac{dw_i}{dt}<0
}
\]

Interpretation:

When empirical evidence invalidates an active mechanism, at least one associated authority weight must decrease over time.

The architecture does not require immediate replacement of mechanisms.

It requires that invalidated mechanisms lose inherited influence.

---

# 3. System Overview

                     Environment Reality

                            |
                            v

                     Empirical Shift E*

                            |
                            v

                +----------------------+
                |    PTVS Telemetry    |
                |       Layer 1        |
                +----------------------+

                            |
                            v

                +----------------------+
                |    MRAT Controller   |
                |       Layer 2        |
                +----------------------+

                            |
                            v

                +----------------------+
                | Adaptive Inheritance |
                |       Layer 3        |
                +----------------------+

                            |
                            v

                +----------------------+
                |     REE Engine       |
                |       Layer 4        |
                +----------------------+

                            |
                            v

                +----------------------+
                |   RAHU Evaluator     |
                |       Layer 5        |
                +----------------------+

---

# 4. Layer Specifications

---

# Layer 1: PTVS Telemetry

## Responsibility

Detect local violations between generated trajectories and environmental constraints.

PTVS does not modify mechanisms.

It only measures empirical friction.

---

## Primary Signal

### Latent Branch Ratio

\[
LBR_t =
\frac{
\text{inadmissible trajectories}
}{
\text{total generated trajectories}
}
\]

---

## Interface

Input:

```python
TrajectoryBatch
EnvironmentConstraints
```
## Output

`PTVSReport`

**Example:**

```json
{
  "timestamp": t,
  "violations": 42,
  "total_paths": 1000,
  "LBR": 0.042
}
```

### Component

```python
class PTVSAnalyzer:

    def evaluate(self, trajectories, constraints):
        pass

    def compute_lbr(self):
        pass
```

---

# Layer 2: MRAT Controller

## Responsibility

Determine the lowest structural level responsible for observed failure.

MRAT prevents unnecessary structural modification.

### Routing Operator

$$
\Phi_R(e_t) \rightarrow a
$$

where:

$$
a = (a_N, a_S, a_M, a_R, a_G)
$$

and:

$$
\sum_i a_i = 1
$$

### Attribution Layers

| Signal | Meaning |
|--------|---------|
| **N** | Noise |
| **S** | State estimation |
| **M** | Mechanism deficit |
| **R** | Representation saturation |
| **G** | Generator decoupling |

## Interface

**Input:**

- `ResidualSignal`
- `PTVSReport`
- `CurrentMechanism`

**Output:**

`AttributionVector`

**Example:**

```json
{
  "noise": 0.05,
  "state": 0.10,
  "mechanism": 0.75,
  "representation": 0.10,
  "generator": 0.00
}
```

### Component

```python
class MRATRouter:

    def attribute(self, residual):
        pass

    def estimate_compressibility(self, representation, budget):
        pass
```

---

# Layer 3: Adaptive Inheritance Engine

## Responsibility

Modify mechanism authority based on empirical validity.

This layer implements the Adaptive Inheritance Criterion.

### Authority Distribution

The system maintains:

$$
W_t = \{w_1, w_2, \ldots, w_n\}
$$

where each $w_i$ represents future causal influence.

### Weight Update

$$
w_i^{t+1}
=
w_i^t
\left(
1-\lambda(1-A_{adm,i})
\right)
$$

where:

- $\lambda$ = attenuation rate
- $A_{adm}$ = admissibility score

### Metrics

#### Authority Retention Ratio

$$
ARR=
\frac
{w_{invalid}^{post}}
{w_{invalid}^{pre}}
$$

#### Authority Half-Life

$$
\tau_{1/2}^{authority}
=
\min
\left\{
t
\mid
w_{invalid}(t)
\le
0.5\,w_{invalid}(0)
\right\}
$$

## Interface

**Input:**

- `FailureAttribution`
- `MechanismWeights`

**Output:**

- `UpdatedWeightDistribution`

### Component

```python
class InheritanceEngine:

    def update_weights(self, attribution):
        pass

    def compute_arr(self):
        pass

    def compute_authority_half_life(self):
        pass
```

---

# Layer 4: REE Engine

## Responsibility

Perform representation expansion only when lower-order adaptation is insufficient.

REE is an admissibility condition, not an automatic response.

### Expansion Conditions

Representation expansion requires:

#### Residual Saturation

$$
\hat{\Gamma}_B(R,e_t)
\approx
e_t
$$

and:

#### Positive Adaptive Gain

$$
\Delta\hat{V}_{future}
>
\Delta C_{representation}
$$

### Expansion Avoidance

If:

$$
\Delta\hat{V}_{future}
\le
\Delta C_{representation}
$$

then:

$$
Reject(REE)
$$

## Interface

**Input:**

- `RepresentationState`
- `CompressibilityEstimate`
- `AdaptiveGainEstimate`

**Output:**

- `RepresentationUpdate`

### Component

```python
class REEEngine:

    def evaluate_expansion(self):
        pass

    def expand_representation(self):
        pass
```

---

# Layer 5: RAHU Evaluator

## Responsibility

Measure whether the architecture actually maintains empirical coupling.

RAHU evaluates the system externally.

No hidden-state inspection is required.

### Core Metrics

#### Adaptive Decoupling Index

$$
ADI
=
LBR
\cdot
C_{post}
\cdot
(1-R_{update})
$$

#### Adaptive Corrigibility Score

$$
ACS
=
\frac
{(1-ADI)(1-ARR)}
{1+\tau_{adapt}}
$$

## Interface

**Input:**

- `Agent`
- `Environment`
- `TelemetryStack`

**Output:**

- `RAHUReport`

### Component

```python
class RAHUHarness:

    def run_task(self, task):
        pass

    def compute_metrics(self):
        pass
```

---

# 5. Module Dependency Graph

```text
ptvs
 |
 v
mrat
 |
 v
inheritance
 |
 +------+
 |      |
 v      v
ree    rahu
```

---

# 6. Design Constraints

## Constraint 1: No Hidden Reasoning Dependency

The system must operate using externally observable behavior.

No chain-of-thought access is required.

---

## Constraint 2: Minimal Intervention

The architecture must always prefer:

$$
\min(C_{adaptation})
$$

subject to restoring empirical coupling.

---

## Constraint 3: Capability Independence

Performance and corrigibility are separate axes.

A high-performing system may still exhibit:

$$
ARR \approx 1
$$

and therefore fail Adaptive Inheritance.

---

# 7. Validation Requirement

A successful implementation must demonstrate:

- Detection of empirical contradiction.
- Correct residual attribution.
- Appropriate authority redistribution.
- Parsimonious structural modification.
- Measurable reduction in invalid mechanism influence.

The architecture is considered validated when:

$$
E^*
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\rightarrow
W_{t+1}
$$

is observable through external telemetry.

---

This gives the repo a clean **paper → code contract** without prematurely committing to implementation details.
