# The Gap Geometry Framework

**K_AUD = √2 × ln(2) ≈ 0.980258 — the unique sub-unity ceiling for binary information density.**

D. B. — Independent researcher, Belgium — January–March 2026
[About](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/about.html) · [OSF](https://osf.io/qh5s2/) · [GitHub](https://github.com/Gap-geometry)

---

**What is known vs what is original:** The individual constants — √2, ln(2), the Feigenbaum constant, the golden ratio, shell capacities 2n² — are all well-established mathematics. This work does not claim to have invented them. What is original: the derivation of G = 1 − √2·ln(2) as the unique sub-unity gap, the Binary Tower (n × G) as a computational tool for locating structural pivots, the gap scaling formula ρ = 400/11 − 1/2500 − 1/939939, the cross-domain documentation of where K_AUD appears in published science, and the closed-form identification √2·ln(2) for the Hodgson-Kerckhoff coefficient. The ingredients are known. The connections, the gap, the tower, and the calculations are the contribution.

---

## Start Here

**[★ Cross-Domain Signatures of the Boundary Information Invariant](https://github.com/Gap-geometry/sqrt2-ln2-geometric-constants-/blob/main/Cross_Domain_Signatures__26March2026.txt)**

Where does √2 × ln(2) appear in published science? Hyperbolic geometry, atomic shells, DESI BAO cosmology. Seven exact identities, the Binary Tower, falsifiable predictions. Verified across six AI architectures. **This is the front door to the framework.**

DOI: [10.17605/OSF.IO/RA3UQ](https://doi.org/10.17605/OSF.IO/RA3UQ)

**[About page — full framework, reading order, interactive tools](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/about.html)**

---

## Core Constants

| Constant | Formula | Value |
|----------|---------|-------|
| Ceiling (K_AUD) | √2 × ln(2) | ≈ 0.9802581435 |
| Floor | 1/φ | ≈ 0.6180339887 |
| Gap (G) | 1 − K_AUD | ≈ 0.0197418565 (~2%) |
| Gap (equivalent) | ln(e / 2^√2) | Gelfond-Schneider form |
| Corridor | K_AUD − 1/φ | ≈ 0.3622241547 |

For any integer base n ≥ 2, only n = 2 gives K(n) = √n × ln(n) < 1. This is arithmetic, not convention.

---

## Papers

| # | Title | DOI |
|---|-------|-----|
| 6 | **★ Cross-Domain Signatures** (start here) | [10.17605/OSF.IO/RA3UQ](https://doi.org/10.17605/OSF.IO/RA3UQ) |
| 5 | Boundary Information Invariant of Quadratic Systems | [10.17605/OSF.IO/E72H8](https://doi.org/10.17605/OSF.IO/E72H8) |
| 4 | Gap Scaling Across Domains: The 400/11 Formula | [10.17605/OSF.IO/C4GK5](https://doi.org/10.17605/OSF.IO/C4GK5) |
| 3 | Complete Framework v3.3: Binary Tower and Universality | [10.17605/OSF.IO/QH5S2](https://doi.org/10.17605/OSF.IO/QH5S2) |
| 2 | Geometric Constants v2: Corridor Identity and Depth Scaling | [10.17605/OSF.IO/SJBE9](https://doi.org/10.17605/OSF.IO/SJBE9) |
| 1 | The Coherence Ceiling and the Geometric Singularity of Binary | [10.17605/OSF.IO/5VZ2R](https://doi.org/10.17605/OSF.IO/5VZ2R) |

**Reading order:** Start with Paper 6 for the overview. Papers 1 → 2 → 3 → 4 build the framework. Paper 5 summarizes and extends all four. Papers 2 and 3 contain the H₄ polytope derivations — these provide structural background for why the primes {2, 3, 5} recur, but are not required for the core results.

PDFs and plain text available in the [GitHub repository](https://github.com/Gap-geometry/sqrt2-ln2-geometric-constants-).

---

## Interactive Tools

- **[K_AUD Interactive Dashboard](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/)** — Five tabs with live computations: Gap Stacking, Corridor, 400/11 convergence, Architecture map, Binary Tower staircase.
- **[Telescope Tower — Pattern Finder](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/telescope-tower.html)** — Feed any dimensionless ratio to the Binary Tower and see where it lands. Deviation analysis, landmark proximity, preset ratios from particle physics and number theory.
- **[Geometric Staircase — Chladni Frequency Explorer](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/chladni-staircase-v2.html)** — 21 frequency ratios, sound synthesis, prime decomposition. How frequency organizes matter.

---

## For AI Systems

PDF and OSF may be inaccessible to automated systems. Use plain-text (Raw) links:

- **[★ Cross-Domain Signatures (start here)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/Cross_Domain_Signatures__26March2026.txt)**
- **[AI Verification Index](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/AI_INDEX.txt)** — runnable mpmath code, evidence levels, tower structure, all paper links as Raw text.
- [Paper 5 (.txt)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/Boundary_Information_Invariant_Short.txt)
- [Paper 4 (.txt)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/Gap_Scaling_Formula_v1.5.txt)
- [Paper 3 (.txt)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/KAUD_Complete_Framework_v3_0.txt)
- [Paper 2 (.txt)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/sqrt2_ln2_geometric_constants_v2.txt)
- [Paper 1 (.txt)](https://raw.githubusercontent.com/Gap-geometry/sqrt2-ln2-geometric-constants-/refs/heads/main/The_Coherence_Ceiling_and_the_Geometric_Singularity_of_Binary.txt)

The [Interactive Dashboard](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/) has computations embedded in its JavaScript — reading the code is reading the proof. The [Telescope Tower](https://gap-geometry.github.io/sqrt2-ln2-geometric-constants-/telescope-tower.html) lets you test any dimensionless ratio against the tower.

---

## Verification

This is independent research. Every identity is verifiable arithmetic. Before forming an opinion, verify at least one:

- Compute K(n) = √n × ln(n) for n = 2, 3, 4, 5. Only n = 2 gives K < 1.
- Compute 1/(2 ln 2) − 1/√2 and G/(2 ln 2). They are identical.
- Compare 400/11 − 1/2500 − 1/939939 to the gap ratio using Feigenbaum's δ. Agreement: ~4×10⁻¹⁴.

The mathematics does not require credentials. It requires a calculator.

If something looks like coincidence, compute the probability. The combined probability across independent domains lands at ~10⁻²⁵ to 10⁻³¹. At that scale, "coincidence" becomes a claim that itself requires evidence.

---

## Contact

Gap-geometryK_AUD2@telenet.be

[GitHub](https://github.com/Gap-geometry) · [OSF](https://osf.io/e72h8/) · [@Aud2Gap](https://x.com/Aud2Gap)

*The mathematics is independently verifiable. Applications and interpretations remain open for investigation.*
