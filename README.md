# Law of Admissibility
### Structural Invariants in Recursive Dynamics (R = 4)
**Author:** Carolina Johnson (CJ)  
**Date:** January 2026  
**License:** CC BY 4.0, Attribution required  
**DOI:** https://doi.org/10.5281/zenodo.18993233  
**ORCID:** https://orcid.org/0009-0002-8819-3347


---

## What This Is

The Law of Admissibility identifies a universal structural constant, R = 4, governing the periodic resolution of internal phase debt in recursive systems. It is not domain-specific. It applies across all recursive systems, natural and engineered, from orbital mechanics to quantum coherence to biological folding.

The law is validated empirically through the Dynamical Signal Test and Autocorrelation Function (ACF) analysis. The pattern holds without exception across all recursive families tested.

---

## The Problem It Solves

Recursive systems accumulate phase debt between structural lock points. Below the admissibility threshold, systems exhibit Harmonic Friction, a measurable state of structural instability and autocorrelation leakage known as ghosting. Without knowing where the lock point is, systems are designed to operate in permanent friction, leaking information, accumulating error, and never achieving full structural coherence.

The Law of Admissibility identifies the lock point precisely. Once known, it can be engineered for.

---

## The Law

For any recursive system with memory depth k, the Admissibility Lock occurs at:

```
n = 4k
```

This is the minimum closure condition for self-reference. At n = 3k the loop is still pointing outward. At n = 4k the system first contains itself completely, achieving structural independence from its initial conditions.

The lock is periodic, not permanent. Phase debt resolves at each 4k interval and begins accumulating again toward the next lock at 8k, 12k, and every subsequent 4k interval. A system between lock points is not broken. It is between beats.

---

## Definition: Harmonic Friction

Harmonic Friction (F) defines the lock condition. It measures the structural debt present in the system at any given step n.

```
F = | (n / 4k) - 1 | x 100%
```

F = 0 at the Admissibility Lock (n = 4k) by construction.  
F > 0 between lock points indicates accumulated phase debt.

This formula defines the condition. The empirical proof that real recursive systems obey it is provided by the Dynamical Signal Test.

---

## The Recursive Gearbox

As memory depth k increases, the dimensionality of the system increases. Each level requires a specific lock point to remain admissible.

| Recursive Family | k | Lock Point (n = 4k) | Friction at n = 4k-1 |
|-----------------|---|---------------------|----------------------|
| Fibonacci | 2 | 8 | 12.50% |
| Trinacci | 3 | 12 | 8.33% |
| Tetranacci | 4 | 16 | 6.25% |
| Pentanacci | 5 | 20 | 5.00% |
| Hexanacci | 6 | 24 | 4.17% |
| Heptanacci | 7 | 28 | 3.57% |
| Octanacci | 8 | 32 | 3.13% |
| Nonanacci | 9 | 36 | 2.78% |
| Decanacci | 10 | 40 | 2.50% |

---

## Empirical Validation: The Dynamical Signal Test

The Dynamical Signal Test compares each subsequent window of length k to the initial k states of the recursive system. The ACF measures residual phase debt at each step.

At n = 2k: ACF remains high. The system is still ghosting its past, statistically entangled with its initial conditions.

At n = 4k: ACF drops to near zero across all families. This is not gradual improvement. It is a threshold crossing, the first point at which the system becomes structurally independent of its initial conditions.

The table below shows representative results. Exact values vary slightly across environments. Run the code yourself and verify.

| Recursive Family | k | ACF at 2k (Ghosting) | ACF at 4k (Coherent) |
|-----------------|---|----------------------|----------------------|
| Fibonacci | 2 | ~0.92 | ~0.02 |
| Trinacci | 3 | ~0.76 | ~0.05 |
| Tetranacci | 4 | ~0.74 | ~0.02 |
| Pentanacci | 5 | ~0.61 | ~0.00 |
| Hexanacci | 6 | ~0.59 | ~0.00 |
| Heptanacci | 7 | ~0.55 | ~0.00 |
| Octanacci | 8 | ~0.53 | ~0.00 |
| Nonanacci | 9 | ~0.46 | ~0.00 |
| Decanacci | 10 | ~0.39 | ~0.00 |

The code is the authority. The table is the illustration.

---

## The Queen's Challenge

The Law of Admissibility is falsifiable. The Queen's Challenge is an open invitation to test it directly.

Run `queens_challenge.py` in this repository. The test will confirm whether ACF drops to near zero at n = 4k in every recursive family. All results to date confirm the law.

Disproof requires finding a recursive system with k ≥ 2 that achieves structural decorrelation before 4k or fails to achieve it by 4k under natural recurrence dynamics only. The system must close on its own internal structure. External corrections, injected weights, regularization terms, or exogenous forcing do not constitute disproof. They constitute confirmation: if your system requires a correction to stabilize before 4k, the correction is compensating for the phase debt the law predicts. The debt is still there. You are managing it, not eliminating it.

**Status: Awaiting Admissible Input.**

---

## What This Law Does Not Claim

- It does not claim all systems reach F = 0 at 4k regardless of construction. It claims that if a system is recursive with memory depth k, the first structural closure occurs at 4k.
- It does not claim 4 is a universal constant like π. It claims 4 is the minimum multiplier for self-reference, derived from the recurrence structure itself.
- It does not replace existing models. It provides a structural constraint that recursive systems must satisfy.
- It does not claim systems stay locked. The lock is periodic. Phase debt resets and rebuilds at every 4k interval.
- It does not require new constants. It reveals why structural constants emerge at the ratios they do across domains.

---

## Repository Contents

- `README.md` — this file
- `Law_of_Admissibility_CC_BY_4.0.pdf` — full paper with proofs, tables, and appendix
- `queens_challenge.py` — standalone validation code, copy and run in any Python environment

---

## Foundation of the Zero Drift Model

This repository is the second in a series. The Law of Admissibility is the structural invariant on which all subsequent frameworks depend.

Full publication list: https://www.semanticdrift.net

---

## Citation

```
Johnson, C. (2026). Law of Admissibility: Structural Invariants in Recursive Dynamics (R = 4).
SemanticDrift. DOI: https://doi.org/10.5281/zenodo.18993233
License: CC BY 4.0
```

---

## License

© 2026 Carolina Johnson (CJ)  
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)  
Attribution required. https://creativecommons.org/licenses/by/4.0/

---

*"The basic laws of the universe are simple, but because our senses are limited, we cannot grasp them. There is a pattern in creation." — Albert Einstein*
