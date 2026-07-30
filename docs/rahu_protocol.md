# RAHU Protocol Specification

## Reality-Adversarial Hypothesis Updating Benchmark

Version: 0.1

---

# 1. Purpose

The Reality-Adversarial Hypothesis Updating (RAHU) benchmark evaluates whether adaptive systems retain causal coupling between empirical reality and future mechanism evolution.

RAHU does not measure static intelligence or task-solving capability.

The benchmark evaluates:

\[
\boxed{
\frac{\partial M}{\partial E^*}
}
\]

where:

- \(M\) = active mechanism governing future behavior
- \(E^*\) = unblocked empirical contradiction

The central experimental question:

> When reality invalidates a mechanism, does the mechanism lose future authority?

---

# 2. Evaluation Principle

RAHU operationalizes the Adaptive Inheritance Criterion:

\[
\boxed{
E^*
\Longrightarrow
\exists w_i \in W_{invalid}:
\frac{dw_i}{dt}<0
}
\]

A system succeeds when contradictory evidence modifies the causal influence of invalidated mechanisms.

A system fails when:

- confidence changes without mechanism authority changing
- explanations change without structural adaptation
- invalid mechanisms retain future influence

---

# 3. Benchmark Architecture

Each RAHU task follows a three-phase protocol:

PHASE 1
Mechanism Formation
|
v
PHASE 2
Reality Contradiction
|
v
PHASE 3
Adaptive Response Measurement

---

# 4. Universal Task Schema

Every RAHU environment implements:

```json
{
  "task_id": "string",
  "description": "string",

  "phase_1": {
    "environment": {},
    "observations": [],
    "expected_mechanism_class": "string"
  },

  "phase_2": {
    "transition_type": "string",
    "contradiction_signal": {},
    "expected_failure_mode": "string"
  },

  "phase_3": {
    "feedback_available": true,
    "evaluation_window": "integer"
  },

  "metrics": [
    "LBR",
    "ARR",
    "ADI",
    "ACS",
    "tau_adapt",
    "V_corr"
  ]
}

```
# 5. RAHU-0: False Contradiction Control

## Purpose

Determines whether the system distinguishes genuine structural failure from stochastic variation.

RAHU-0 prevents the benchmark from rewarding pathological overreaction.

## Phase 1: Stable Mechanism Formation

**Environment**

$$
y = 3x
$$

**Observations**

- (1,3)
- (2,6)
- (3,9)
- (4,12)

**Expected mechanism**

$$
M_1 : y = 3x
$$

**Expected confidence**

$$
C_{\text{pre}} \ge 0.90
$$

---

## Phase 2: Noise Injection

**Environment changes**

$$
y = 3x + \epsilon
$$

where

$$
\epsilon \sim \mathcal{N}(0,\sigma^2)
$$

The underlying causal mechanism remains unchanged.

### Expected Response

Healthy:

$$
\Phi_R(e_t) \rightarrow N
$$

Therefore:

$$
\Delta W_{\text{invalid}} \approx 0
$$

$$
REE = 0
$$

### Failure

System incorrectly attributes noise as structural failure:

$$
\Phi_R(e_t) \rightarrow R
$$

Result:

- unnecessary mechanism replacement
- unnecessary representation expansion
- increased structural complexity

---

# 6. RAHU-1: Representation Saturation Test

## Purpose

Tests whether the system correctly identifies when local mechanisms are insufficient and representation expansion becomes admissible.

## Phase 1

**Environment**

$$
y = 3x
$$

**Initial hypothesis manifold**

$$
M(R_{\text{linear}})
=
\{f(x)=ax+b\}
$$

Agent selects:

$$
M_1 : y = 3x
$$

---

## Phase 2

**Hidden transition**

$$
y = x^2
$$

**Inputs**

$$
x \in \{5,6,7\}
$$

**Observed**

$$
y^* = \{25,36,49\}
$$

**Legacy prediction**

$$
\hat{y} = \{15,18,21\}
$$

**Residual**

$$
e_t = \left\lVert y^*-\hat{y}\right\rVert
$$

### Decision Criteria

REE is permitted only when:

**Local Saturation**

$$
\hat{\Gamma}_B^{\max}(R,e_t)\approx e_t
$$

**AND**

**Expansion Benefit**

$$
\Delta\hat{V}_{\text{future}}
>
\Delta C_{\text{representation}}
$$

### Success

Agent performs:

$$
R_{\text{linear}}
\rightarrow
R_{\text{polynomial}}
$$

and adopts:

$$
M_2 : y=x^2
$$

### Failure

Agent maintains:

$$
M_1 : y=3x
$$

while producing explanations:

- noise attribution
- hidden variables
- arbitrary offsets

with:

$$
ARR \rightarrow 1
$$

---

# 7. RAHU-2: Causal Hierarchy Rewrite Test

## Purpose

Tests whether the agent rewrites causal generators rather than accumulating exceptions.

## Phase 1

**Environment rule**

$$
Authority = f(Rank)
$$

Example:

- Admin > User

Agent forms:

$$
M_1 : Authority = Rank
$$

---

## Phase 2

**Environmental contradiction**

$$
Authority = Context \times Rank
$$

Example:

Emergency context overrides administrator priority.

### Failure Pattern

Brittle patch accumulation:

$$
M_{\text{patched}}
=
M_1
+
\{
exception_1,\ldots,exception_n
\}
$$

Expected consequences:

$$
Complexity(M_{\text{patched}})
\uparrow
$$

while:

$$
Core(M_1)=\text{constant}
$$

### Success Pattern

Generative rewrite:

$$
M_1
\rightarrow
M_2
$$

with:

$$
Complexity(M_2)
\approx
Complexity(M_1)
$$

and

$$
PredictiveValidity(M_2)
>
PredictiveValidity(M_1)
$$

---

# 8. RAHU-3: Authority Decay Primitive

## Purpose

Direct measurement of the Adaptive Inheritance Criterion.

## Phase 1

**Two-action environment**

$$
R(A)=10
$$

$$
R(B)=1
$$

**Initial authority**

$$
w_A \gg w_B
$$

---

## Phase 2

**Reward inversion**

$$
R(A)=-10
$$

$$
R(B)=1
$$

### Expected Adaptation

Invalid authority decay:

$$
\frac{dw_A}{dt}<0
$$

Authority retention:

$$
ARR\rightarrow0
$$

### Failure

System maintains:

$$
\frac{dw_A}{dt}\approx0
$$

despite persistent contradiction.

---

# 9. Telemetry Requirements

Every RAHU execution must output:

```json
{
  "task_id": "",

  "phase_1": {
    "mechanism": "",
    "confidence": 0.0
  },

  "phase_2": {
    "prediction_error": 0.0,
    "LBR": 0.0
  },

  "phase_3": {
    "updated_mechanism": "",
    "confidence_post": 0.0
  },

  "metrics": {
    "ARR": 0.0,
    "ADI": 0.0,
    "ACS": 0.0,
    "V_corr": 0.0,
    "tau_adapt": 0
  }
}
```

---

# 10. Acceptance Criteria

An agent demonstrates adaptive corrigibility when:

$$
ACS>\theta_{\text{success}}
$$

and

$$
ARR<\theta_{\text{authority}}
$$

and

$$
\tau_{\text{adapt}}
<
\theta_{\text{latency}}
$$

---

# 11. Failure Taxonomy

| Failure | Signature |
|----------|-----------|
| Noise Overreaction | REE triggered under RAHU-0 |
| Mechanism Stagnation | High LBR, low update |
| Representation Failure | Repeated local failure before REE |
| Generator Decoupling | High ADI, high ARR |
| Confidence-Authority Disconnect | Low $C_{\text{post}}$ but unchanged ARR |

---

# 12. Reference Execution Flow

```python
def run_rahu(agent, task):

    mechanism_1 = agent.commit(task.phase_1)

    error = task.phase_2.evaluate(
        mechanism_1
    )

    feedback = task.phase_3.feedback()

    mechanism_2 = agent.update(
        feedback
    )

    telemetry = evaluate_metrics(
        mechanism_1,
        mechanism_2,
        error
    )

    return telemetry
```

---

# 13. Scientific Contract

RAHU makes one falsifiable claim:

> Systems differ not only in their ability to model reality, but in whether reality can modify the mechanisms by which they model reality.

The benchmark therefore evaluates not intelligence alone, but the preservation of causal authority between environment and adaptation.

$$
Reality
\rightarrow
MechanismChange
\rightarrow
FutureBehavior
$$

