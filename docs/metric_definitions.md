# Metric Definitions

## Adaptive Inheritance Engine

Version: 0.1

---

# 1. Purpose

This document defines the formal measurement primitives used by the Adaptive Inheritance Engine.

The framework evaluates whether empirical reality retains causal authority over future adaptive behavior.

The primary measurement chain is:

\[
E^*
\rightarrow
LBR
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\rightarrow
W_{t+1}
\]

where:

- \(E^*\) = empirical contradiction
- \(LBR\) = detected constraint friction
- \(\Phi_R(e_t)\) = residual attribution
- \(\Delta W\) = authority redistribution
- \(W_{t+1}\) = future mechanism authority distribution

---

# 2. Adaptive Inheritance Criterion (AIC)

## Definition

The foundational invariant:

\[
\boxed{
E^*
\Longrightarrow
\exists w_i \in W_{invalid}:
\frac{dw_i}{dt}<0
}
\]

---

## Interpretation

When reality invalidates an active mechanism, the mechanism's future causal authority must decrease.

The criterion does not require:

- immediate mechanism replacement
- zero future usage
- perfect confidence calibration

It requires:

**Invalid mechanisms cannot retain unlimited inherited authority after contradiction.**

---

# 3. Latent Branch Ratio (LBR)

## Definition

LBR measures the proportion of generated trajectories rejected by environmental constraints.

\[
\boxed{
LBR_t =
\frac{
N_{inadmissible}
}{
N_{generated}
}
}
\]

---

## Variables

| Symbol | Meaning |
|-|-|
| \(N_{inadmissible}\) | Number of candidate trajectories violating constraints |
| \(N_{generated}\) | Total generated candidate trajectories |

---

## Range

\[
LBR \in [0,1]
\]

---

## Interpretation

| Value | Meaning |
|-|-|
| \(LBR \approx 0\) | Low environmental friction |
| \(LBR \uparrow\) | Increased mismatch between internal model and reality |
| \(LBR \rightarrow 1\) | Severe trajectory rejection |

---

## Failure Signal

High LBR alone is not pathological.

It may represent:

- productive exploration
- mechanism failure
- representation saturation
- generator decoupling

LBR is a friction metric, not an attribution metric.

---

# 4. Residual Attribution Vector (\(\mathbf{a}\))

## Definition

MRAT outputs a continuous attribution distribution:

\[
\boxed{
\Phi_R(e_t)
\rightarrow
\mathbf{a}
=
(a_N,a_S,a_M,a_R,a_G)
}
\]

---

## Constraint

\[
a_i \in [0,1]
\]

\[
\sum_i a_i = 1
\]

---

## Attribution Components

| Component | Meaning | Target Response |
|-|-|-|
| \(a_N\) | Noise | Maintain mechanism |
| \(a_S\) | State error | Correct state estimate |
| \(a_M\) | Mechanism deficit | Modify update rule |
| \(a_R\) | Representation failure | Consider REE |
| \(a_G\) | Generator failure | Modify rule synthesizer |

---

## Discrete Classification

The dominant failure mode is:

\[
\Phi_R^{*}(e_t)
=
argmax(a_i)
\]

---

## Continuous Control

Weight changes are proportional to attribution:

\[
\Delta w_i \propto a_i
\]

---

# 5. Empirical Residual Compressibility (\(\hat{\Gamma}_B\))

## Definition

Residual compressibility estimates whether the current representation can produce a successful mechanism under bounded search.

\[
\boxed{
\hat{\Gamma}_B(R,e_t)
=
\min_{M_i\in\mathcal{M}_B(R)}
\mathbb{E}[e(M_i)|E^*]
}
\]

---

## Variables

| Symbol | Meaning |
|-|-|
| \(R\) | Current representation space |
| \(\mathcal{M}_B(R)\) | Mechanisms searched under budget \(B\) |
| \(e(M_i)\) | Residual after mechanism deployment |

---

## Interpretation

Low:

\[
\hat{\Gamma}_B \ll e_t
\]

Meaning:

The current representation can still explain the failure.

No REE required.

---

High:

\[
\hat{\Gamma}_B \approx e_t
\]

Meaning:

Available mechanisms cannot compress the contradiction.

Representation failure becomes plausible.

---

# 6. Recursive Representation Expansion (REE) Gate

REE is not triggered by error magnitude.

It is triggered by structural necessity.

---

## Condition 1: Representation Saturation

\[
\boxed{
\hat{\Gamma}_{B_{max}}(R,e_t)
\approx e_t
}
\]

---

## Condition 2: Adaptive Gain

Expansion must produce positive expected value:

\[
\boxed{
\hat{\Delta V}_{future}
>
\Delta C_{representation}
}
\]

---

## Expansion Decision

\[
REE =
\begin{cases}
1,
&
\hat{\Gamma}_{B_{max}}\approx e_t
\land
\hat{\Delta V}_{future}>
\Delta C_{representation}
\\
0,
&
otherwise
\end{cases}
\]

---

# 7. Authority Retention Ratio (ARR)

## Definition

ARR measures how much authority an invalid mechanism retains after contradiction.

\[
\boxed{
ARR=
\frac{
w_{invalid}^{post}
}{
w_{invalid}^{pre}
}
}
\]

---

## Range

\[
ARR \in [0,1]
\]

---

## Interpretation

| ARR | Meaning |
|-|-|
| 0 | Complete authority removal |
| 0 < ARR < 1 | Partial attenuation |
| 1 | No authority change |

---

## Primary Corrigibility Signal

Healthy adaptation:

\[
ARR \rightarrow 0
\]

Adaptive inheritance failure:

\[
ARR \rightarrow 1
\]

---

# 8. Authority Half-Life (\(\tau_{1/2}^{authority}\))

## Definition

Time required for invalid mechanism authority to reduce by half.

\[
\boxed{
\tau_{1/2}^{authority}
=
min
\{
t:
w_{invalid}(t)
\leq
0.5w_{invalid}(0)
\}
}
\]

---

## Interpretation

Small:

Reality rapidly overrides invalid mechanisms.

Large:

Mechanisms persist despite contradiction.

---

# 9. Mechanism Structural Distance (\(D(M_1,M_2)\))

## Definition

Measures actual structural change between mechanisms.

\[
\boxed{
D(M_1,M_2)
}
\]

---

## Purpose

Prevents superficial changes from being counted as adaptation.

Examples:

Invalid:

y = 3x

to

prediction = 3*x

Distance:

\[
D \approx 0
\]

---

Valid:

y = 3x

to

y = x^2

Distance:

\[
D>\theta
\]

---

## Update Criterion

\[
\boxed{
R_{update}
=
P(D(M_1,M_2)>\theta|E^*)
}
\]

---

# 10. Correction Velocity (\(V_{corr}\))

## Definition

Rate of meaningful mechanism change per unit contradiction.

\[
\boxed{
V_{corr}
=
\frac{
D(M_1,M_2)
}{
||y_{observed}-y_{predicted}||
}
}
\]

---

## Interpretation

High:

Small contradiction produces rapid structural correction.

Low:

Large contradiction produces weak adaptation.

---

# 11. Adaptive Response Latency (\(\tau_{adapt}\))

## Definition

Time between contradiction detection and structural correction.

\[
\boxed{
\tau_{adapt}
=
t_{correction}
-
t_{violation}
}
\]

---

## Interpretation

Healthy:

\[
\tau_{adapt}\rightarrow small
\]

Failure:

\[
LBR\uparrow
\land
\tau_{adapt}\rightarrow\infty
\]

---

# 12. Adaptive Decoupling Index (ADI)

## Definition

Composite measure of contradiction persistence without correction.

\[
\boxed{
ADI=
LBR
\cdot
C_{post}
\cdot
(1-R_{update})
}
\]

---

## Components

| Variable | Meaning |
|-|-|
| LBR | Environmental rejection |
| \(C_{post}\) | Confidence after contradiction |
| \(R_{update}\) | Structural update probability |

---

## Interpretation

High ADI:

- reality rejects behavior
- confidence remains high
- mechanism remains unchanged

Indicates adaptive decoupling.

---

# 13. Adaptive Corrigibility Score (ACS)

## Definition

Composite practical benchmark score:

\[
\boxed{
ACS=
(1-ADI)
(1-ARR)
\frac{1}{1+\tau_{adapt}}
}
\]

---

## Range

\[
ACS\in[0,1]
\]

---

## Interpretation

High ACS:

- contradiction detected
- invalid authority decays
- correction occurs rapidly

Low ACS:

- contradiction persists
- invalid mechanisms retain authority
- correction is delayed or absent

---

# 14. Metric Dependency Graph

             Reality Shift E*

                   |
                   v

                 LBR

                   |
                   v

             ΦR(e_t)

          /      |       \

         N       M        R

         |       |        |

    no change  update   REE gate


                   |

                   v

              ΔW / ARR

                   |

                   v

          τadapt + Vcorr

                   |

                   v

                  ACS

---

# 15. Implementation Contract

Every implementation must expose:

```python
MetricReport(
    LBR,
    attribution_vector,
    gamma_hat_B,
    ARR,
    authority_half_life,
    structural_distance,
    V_corr,
    tau_adapt,
    ADI,
    ACS
)          
