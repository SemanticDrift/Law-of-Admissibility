# Law of Admissibility
### Structural Invariants in Recursive Dynamics (R = 4)
**Author:** Carolina Johnson (CJ)  
**Date:** November 2026  
**DOI:** [10.5281/zenodo.18223592](https://doi.org/10.5281/zenodo.18223592)  
**ORCID:** [0009-0002-8819-3347
](https://orcid.org/0009-0002-8819-3347)


---

## What This Is

The Law of Admissibility locates the step at which a recursive system of memory depth k completes four full turns of its slowest damped mode. For the unweighted k-nacci recurrences (Fibonacci, Tribonacci, Tetranacci and the higher families), the characteristic roots fix the period P and the damping rate γ of that mode, and the law states where those roots complete a cycle of four quarters.

---

## The Law

The admissibility cycle has length 4k and consists of four quarters of k steps each. The slowest damped mode has period P, and for every k ≥ 2:

```
k − 1 < P ≤ k
```

with equality only for Fibonacci (Theorem 1). It follows that:

```
3k < 4P ≤ 4k
```

so the fourth full turn is not complete at n = 3k and is complete by n = 4k (Corollary 1). The step n = 4k is the **admissibility boundary**: the first window boundary at which the slowest mode has completed four full turns. Exactly four full turns are complete there in every family.

The boundary repeats at 4k, 8k, 12k and every multiple of 4k. At each one, the envelope of the residual of the initial conditions has fallen by the same factor, e^(−4kγ). For integer initial values the residual approaches zero and never reaches it.

---

## Harmonic Friction

Harmonic Friction (F) measures the position of the system within the current admissibility cycle, as the fraction of the cycle that remains before the next boundary:

```
F(n) = (⌈n / 4k⌉ − n / 4k) × 100%
```

F = 0 at every admissibility boundary and begins again after each one. In the first cycle it equals |n/4k − 1| × 100%.

| Recursive Family | k | Boundary (n = 4k) | F at n = 4k − 1 |
|-----------------|---|-------------------|-----------------|
| Fibonacci | 2 | 8 | 12.50% |
| Tribonacci | 3 | 12 | 8.33% |
| Tetranacci | 4 | 16 | 6.25% |
| Pentanacci | 5 | 20 | 5.00% |
| Hexanacci | 6 | 24 | 4.17% |
| Heptanacci | 7 | 28 | 3.57% |
| Octanacci | 8 | 32 | 3.13% |
| Nonanacci | 9 | 36 | 2.78% |
| Decanacci | 10 | 40 | 2.50% |

---

## What the Roots Set and What the Initial Values Set

The period P and the damping rate γ are properties of the recurrence. Harmonic Friction F is a property of the cycle. The admissibility boundary 4k is where the two meet. None of these depends on the initial values.

The initial values set only the coefficients of the modes, so they affect the measured numbers and not the law. Two runs of the same test with different starting values or a different indexing give different measured residuals, and both are correct.

---

## Repository Contents

- `README.md`: this file
- `Law_of_Admissibility_CC_BY_4.0.pdf`: the full paper with the proof, tables and Annex A

---

## Dependencies

| Paper | DOI |
|-------|-----|
| The Fibonacci Principle | [10.5281/zenodo.18227844](https://doi.org/10.5281/zenodo.18227844) |

---

Full publication list: https://www.SemanticDrift.net

---

## Citation

Johnson, C. (2026). Law of Admissibility: Structural Invariants in Recursive Dynamics (R = 4). SemanticDrift. DOI: [10.5281/zenodo.18223592](https://doi.org/10.5281/zenodo.18223592). License: CC BY 4.0.

---

## License

© 2026 Carolina Johnson (CJ)  
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)  
Attribution required. https://creativecommons.org/licenses/by/4.0/
