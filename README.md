# Global Time Echoes: Empirical Validation of the Temporal Equivalence Principle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18004832.svg)](https://doi.org/10.5281/zenodo.18004832)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

![Global Time Echoes](site/public/image.webp)

**Author:** Matthew Lukin Smawfield  
**Version:** v0.3 (Singapore)  
**Date:** 21 December 2025  
**Status:** Preprint  
**DOI:** [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832)  
**Website:** [https://matthewsmawfield.github.io/TEP-GTE/](https://matthewsmawfield.github.io/TEP-GTE/)

## Abstract

Analysis of 25.3 years of GNSS timing data (2000–2025) reveals a persistent, distance-structured correlation in global atomic clock networks that tests an empirically untested assumption of general relativity: the global integrability of proper time. Examination of 165.2 million station pairs from 474 unique receivers demonstrates a spatial correlation signal decaying exponentially with distance (λ = 4,201 ± 1,967 km, R² = 0.92–0.97 across three independent analysis centers). These findings emerge from a systematic five-paper research program: theoretical framework development with quantitative predictions (Paper 0), multi-center validation across independent processing pipelines (Paper 1), 25-year longitudinal analysis enabling long-period geophysical detection (Paper 2), raw data confirmation eliminating processing artifacts (Paper 3), and cosmological extension connecting terrestrial correlations to dark matter phenomenology through gravitational lensing (Paper 4).

Seven statistically independent signatures emerge with joint probability p ≈ 2×10⁻²⁷ (>10σ): exponential spatial decay; East-West/North-South anisotropy (ratio 2.16, p < 10⁻¹⁵); orbital velocity coupling (r = −0.888, 5.1σ); alignment with the Cosmic Microwave Background dipole (18.2° separation, 5,570× variance ratio over galactic motion); planetary event responses (56/156 significant at ≥2σ); 18.6-year lunar nutation coupling (R² = 0.641); and semiannual nutation coupling (R² = 0.904). Raw RINEX validation using Single Point Positioning with broadcast ephemerides achieves 100% detection rate across 72 metric combinations (t-statistics up to 112, Cohen's d up to 0.304), excluding processing artifacts as the origin. The network's selectivity profile—sensitive to velocity-dependent dynamics while blind to GM/r² scaling and solar rotation—characterizes it as an inertial interferometer measuring correlation geometry rather than a gravimeter measuring Newtonian force.

These observations match a priori predictions of the Temporal Equivalence Principle, a bi-metric scalar-tensor framework in which proper time is a dynamical field governed by a conformal factor A(φ) = exp(2βφ/M_Pl). Fifth-force suppression operates through the continuous spatial profile of the φ field (Temporal Topology), with suppression arising from the non-linear superposition of field gradients (Temporal Shear), replacing discrete thin-shell approximations with a geometrically continuous mechanism. The observed correlation length corresponds to a scalar field mass m_φ ≈ (4.34–5.93)×10⁻¹⁴ eV/c², consistent with Vainshtein screening at the dark energy scale Λ ~ 10⁻¹³ eV. The framework preserves local Lorentz invariance while predicting global path-dependent synchronization through spatial correlations in the φ field. Critically, the conformal sector responsible for clock-rate modulation remains unconstrained by GW170817, which bounds only disformal (cone-tilting) effects.

If validated through independent replication, TEP implies that dark matter phenomenology in gravitational lensing arises from temporal-field gradients (active Temporal Shear) rather than particulate matter—the projection of differential proper-time accumulation onto observations that assume the Isochrony Axiom. The 4,000 km correlation on Earth and the 50 kpc dark matter halo in galaxies represent the same scalar field at different density scales, connected by the universal M^1/3 Vainshtein scaling law and the continuous relaxation of Temporal Topology from deep potential wells to the weak-field regime. Explicit falsification criteria include: failure of independent groups to replicate the raw carrier-phase signal; correlation length falling outside the 500–20,000 km range; confirmation that the signal arises from ephemeris artifacts rather than physical clock correlations (via Satellite Laser Ranging validation); and null synchronization holonomy in closed-loop triangular time-transfer experiments.

## Key Findings

This synthesis integrates Papers 1–4 and shows seven statistically independent signatures with joint probability p ≈ 2×10⁻²⁷ (>10σ): exponential spatial decay (λ = 4,201 ± 1,967 km), EW/NS anisotropy (ratio 2.16), orbital velocity coupling (r = −0.888), CMB frame alignment (18.2° from the dipole; 5,570× variance ratio), planetary event responses (56/156 significant), 18.6-year lunar nutation (R² = 0.641), and semiannual nutation (R² = 0.904). Raw RINEX validation detects the signal in 72/72 metric combinations (mean R² = 0.93), ruling out processing artifacts. The inferred scalar field mass (m_φ ≈ (4.34–5.93)×10⁻¹⁴ eV/c²) is consistent with Vainshtein screening near the dark-energy scale, linking terrestrial timing networks to lensing-scale phenomenology through the continuous relaxation of Temporal Topology.

---

## The TEP Research Program

This integrated manuscript synthesizes results from a systematic research program:

| Paper | Repository | Title | DOI |
|-------|-----------|-------|-----|
| **Paper 0** | [TEP](https://github.com/matthewsmawfield/TEP) | Temporal Equivalence Principle: Dynamic Time & Emergent Light Speed | [10.5281/zenodo.16921911](https://doi.org/10.5281/zenodo.16921911) |
| **Paper 1** | [TEP-GNSS](https://github.com/matthewsmawfield/TEP-GNSS) | Global Time Echoes: Distance-Structured Correlations in GNSS Clocks | [10.5281/zenodo.17127229](https://doi.org/10.5281/zenodo.17127229) |
| **Paper 2** | [TEP-GNSS-II](https://github.com/matthewsmawfield/TEP-GNSS-II) | Global Time Echoes: 25-Year Temporal Evolution of Distance-Structured Correlations in GNSS Clocks | [10.5281/zenodo.17517141](https://doi.org/10.5281/zenodo.17517141) |
| **Paper 3** | [TEP-GNSS-RINEX](https://github.com/matthewsmawfield/TEP-GNSS-RINEX) | Global Time Echoes: Raw RINEX Validation of Distance-Structured Correlations in GNSS Clocks | [10.5281/zenodo.17860166](https://doi.org/10.5281/zenodo.17860166) |
| **Paper 4** | [TEP-GL](https://github.com/matthewsmawfield/TEP-GL) | Temporal-Spatial Coupling in Gravitational Lensing: A Reinterpretation of Dark Matter Observations | [10.5281/zenodo.17982540](https://doi.org/10.5281/zenodo.17982540) |
| **Paper 5** | **TEP-GTE** (This repo) | Global Time Echoes: Empirical Validation of the Temporal Equivalence Principle | [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832) |
| **Paper 6** | [TEP-UCD](https://github.com/matthewsmawfield/TEP-UCD) | Universal Critical Density: Unifying Atomic, Galactic, and Compact Object Scales | [10.5281/zenodo.18064366](https://doi.org/10.5281/zenodo.18064366) |
| **Paper 7** | [TEP-RBH](https://github.com/matthewsmawfield/TEP-RBH) | The Soliton Wake: A Runaway Black Hole as a Gravitational Soliton | [10.5281/zenodo.18059251](https://doi.org/10.5281/zenodo.18059251) |
| **Paper 8** | [TEP-SLR](https://github.com/matthewsmawfield/TEP-SLR) | Global Time Echoes: Optical Validation of the Temporal Equivalence Principle via Satellite Laser Ranging | [10.5281/zenodo.18064582](https://doi.org/10.5281/zenodo.18064582) |
| **Paper 9** | [TEP-EXP](https://github.com/matthewsmawfield/TEP-EXP) | What Do Precision Tests of General Relativity Actually Measure? | [10.5281/zenodo.18109761](https://doi.org/10.5281/zenodo.18109761) |
| **Paper 10** | [TEP-COS](https://github.com/matthewsmawfield/TEP-COS) | The Temporal Equivalence Principle: Suppressed Density Scaling in Globular Cluster Pulsars | [10.5281/zenodo.18165798](https://doi.org/10.5281/zenodo.18165798) |
| **Paper 11** | [TEP-H0](https://github.com/matthewsmawfield/TEP-H0) | The Cepheid Bias: Resolving the Hubble Tension | [10.5281/zenodo.18209702](https://doi.org/10.5281/zenodo.18209702) |
| **Paper 12** | [TEP-JWST](https://github.com/matthewsmawfield/TEP-JWST) | The Temporal Equivalence Principle: A Unified Resolution to the JWST High-Redshift Anomalies | [10.5281/zenodo.19000827](https://doi.org/10.5281/zenodo.19000827) |
| **Paper 13** | [TEP-WB](https://github.com/matthewsmawfield/TEP-WB) | The Temporal Equivalence Principle: Density-Dependent Screening in Gaia DR3 Wide Binaries | [10.5281/zenodo.19102062](https://doi.org/10.5281/zenodo.19102062) |

## Paper Structure

1. **Introduction** — The synchronization residual problem, historical context, theoretical motivation
2. **Phenomenology** — Spatial correlation structure, seven signatures, CMB alignment, selectivity profile
3. **Validation** — Processing artifacts, ionospheric/geomagnetic/tropospheric hypotheses, long-period stability
4. **Theoretical Framework** — Two-metric geometry, Temporal Topology and Temporal Shear, Vainshtein screening, synchronization holonomy
5. **Cosmological Implications** — GW170817 constraints, Phantom Mass mechanism, Earth-Galaxy scaling
6. **Falsification** — Explicit criteria, three-tier experimental program
7. **Conclusions** — Summary and path forward


## License

This project is licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0). See [LICENSE](LICENSE) for details.

## Citation

```bibtex
@article{smawfield2025tepgte,
  title={Global Time Echoes: Empirical Validation of the Temporal Equivalence Principle},
  author={Smawfield, Matthew Lukin},
  journal={Zenodo},
  year={2025},
  doi={10.5281/zenodo.18004832},
  note={Preprint v0.3 (Singapore)}
}
```

---

## Open Science Statement

These are working preprints shared in the spirit of open science—all manuscripts, analysis code, and data products are openly available under Creative Commons and MIT licenses to encourage and facilitate replication. Feedback and collaboration are warmly invited and welcome.

---

**Contact:** matthewsmawfield@gmail.com  
**ORCID:** [0009-0003-8219-3159](https://orcid.org/0009-0003-8219-3159)

