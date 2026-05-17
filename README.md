# Global Time Echoes: Empirical Synthesis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18004832.svg)](https://doi.org/10.5281/zenodo.18004832)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

![Global Time Echoes](site/public/image.webp)

**Author:** Matthew Lukin Smawfield  
**Version:** v0.4 (Singapore)  
**Date:** 29 April 2026  
**Status:** Preprint  
**DOI:** [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832)  
**Website:** [https://matthewsmawfield.github.io/TEP-GTE/](https://matthewsmawfield.github.io/TEP-GTE/)

## Abstract

Analysis of 25.3 years of GNSS timing data (2000–2025) reveals a persistent, distance-structured correlation in global atomic clock networks that tests an empirically untested assumption of general relativity: the global integrability of proper time. Examination of 165.2 million station pairs from 474 unique receivers demonstrates a spatial correlation signal decaying exponentially with distance (λ<sub>T</sub> = 4,201 ± 1,967 km, R² = 0.92–0.97 across three independent analysis centers). These findings emerge from a systematic five-paper research program: theoretical framework development with pre-specified expectations and theoretical search ranges (Paper 0), multi-center validation across independent processing pipelines (Paper 1), 25-year longitudinal analysis enabling long-period geophysical detection (Paper 2), raw data confirmation strongly constraining precise-product processing artifacts (Paper 3), and speculative cosmological extension exploring whether temporal covariance or gradient effects contribute to dark-sector phenomenology (Paper 4).

Seven convergent signatures emerge with joint probability p ≈ 2×10⁻²⁷ (>10σ): exponential spatial decay; East-West/North-South anisotropy (ratio 2.16, p < 10⁻¹⁵); orbital velocity coupling (r = −0.888, 5.1σ); alignment with the Cosmic Microwave Background dipole (18.2° separation, 5,570× variance ratio over galactic motion); planetary event responses (56/156 significant at ≥2σ); 18.6-year lunar nutation coupling (R² = 0.641); and semiannual nutation coupling (R² = 0.904). Raw RINEX validation using Single Point Positioning with broadcast ephemerides achieves consistent signal detection across all 72 metric combinations (t-statistics up to 112, Cohen's d up to 0.304), strongly constraining precise-product processing artifacts as the origin. Broadcast ephemerides still contain control-segment information, so Satellite Laser Ranging and non-GNSS optical checks remain necessary for definitive confirmation. The network's selectivity profile—sensitive to velocity-dependent dynamics while blind to GM/r² scaling and solar rotation—characterizes it as an inertial interferometer measuring correlation geometry rather than a gravimeter measuring Newtonian force.

These observations match pre-specified expectations of the Temporal Equivalence Principle, a bi-metric scalar-tensor framework in which proper time is a dynamical field governed by a conformal factor A(φ) = exp(βφ/M_Pl). Fifth-force suppression operates through the continuous spatial profile of the φ field (Temporal Topology), with suppression arising from the non-linear superposition of field gradients (Temporal Shear), replacing discrete thin-shell approximations with a geometrically continuous mechanism. The observed correlation length corresponds to a scalar field mass m_φ ≈ (4.34–5.93)×10⁻¹⁴ eV/c², consistent with Vainshtein screening at the dark energy scale Λ ~ 10⁻¹³ eV. The framework preserves local Lorentz invariance while predicting global path-dependent synchronization through spatial correlations in the φ field. Critically, the conformal sector responsible for clock-rate modulation is not directly constrained by photon–graviton differential-propagation tests such as GW170817, although local conformal-gradient/source-charge sectors remain constrained by PPN, clock, and equivalence-principle tests.

If validated through independent replication, TEP predicts that part of the phenomenology attributed to dark matter may include temporal-field gradient or covariance contributions (active Temporal Shear) alongside particulate matter—the projection of differential proper-time accumulation onto observations that assume the Isochrony Axiom. The 4,000 km correlation on Earth and the 50 kpc dark matter halo in galaxies represent the same scalar field at different density scales, connected by the M^1/3 scaling realized in some candidate derivative-screened completions and the continuous relaxation of Temporal Topology from deep potential wells to the weak-field regime. Explicit falsification criteria include: failure of independent groups to replicate the raw carrier-phase signal; correlation length falling outside the 500–20,000 km range; confirmation that the signal arises from ephemeris artifacts rather than physical clock correlations (via Satellite Laser Ranging validation); and null synchronization holonomy in closed-loop triangular time-transfer experiments.

## Key Findings

This synthesis integrates Papers 1–4 and shows seven convergent signatures with joint probability p ≈ 2×10⁻²⁷ (>10σ): exponential spatial decay (λ<sub>T</sub> = 4,201 ± 1,967 km), EW/NS anisotropy (ratio 2.16), orbital velocity coupling (r = −0.888), CMB frame alignment (18.2° from the dipole; 5,570× variance ratio), planetary event responses (56/156 significant), 18.6-year lunar nutation (R² = 0.641), and semiannual nutation (R² = 0.904). Raw RINEX validation detects the signal across all 72 metric combinations (mean R² = 0.93), strongly constraining processing artifacts. The inferred scalar field mass (m_φ ≈ (4.34–5.93)×10⁻¹⁴ eV/c²) is consistent with Vainshtein screening near the dark-energy scale, linking terrestrial timing networks to lensing-scale phenomenology through the continuous relaxation of Temporal Topology.

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
| **Paper 5** | **TEP-GTE** (This repo) | Global Time Echoes: Empirical Synthesis | [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832) |
| **Paper 6** | [TEP-UCD](https://github.com/matthewsmawfield/TEP-UCD) | Universal Critical Density: Cross-Scale Consistency of ρ_T | [10.5281/zenodo.18064365](https://doi.org/10.5281/zenodo.18064365) |
| **Paper 7** | [TEP-RBH](https://github.com/matthewsmawfield/TEP-RBH) | The Soliton Wake: Exploring RBH-1 as a Temporal Topology Candidate | [10.5281/zenodo.18059250](https://doi.org/10.5281/zenodo.18059250) |
| **Paper 8** | [TEP-SLR](https://github.com/matthewsmawfield/TEP-SLR) | Global Time Echoes: Optical-Domain Consistency Test via Satellite Laser Ranging | [10.5281/zenodo.18064581](https://doi.org/10.5281/zenodo.18064581) |
| **Paper 9** | [TEP-EXP](https://github.com/matthewsmawfield/TEP-EXP) | What Do Precision Tests of General Relativity Actually Measure? | [10.5281/zenodo.18109760](https://doi.org/10.5281/zenodo.18109760) |
| **Paper 10** | [TEP-COS](https://github.com/matthewsmawfield/TEP-COS) | Temporal Equivalence Principle: Suppressed Density Scaling in Globular Cluster Pulsars | [10.5281/zenodo.18165798](https://doi.org/10.5281/zenodo.18165798) |
| **Paper 11** | [TEP-H0](https://github.com/matthewsmawfield/TEP-H0) | The Cepheid Bias: Resolving the Hubble Tension | [10.5281/zenodo.18209702](https://doi.org/10.5281/zenodo.18209702) |
| **Paper 12** | [TEP-JWST](https://github.com/matthewsmawfield/TEP-JWST) | Temporal Equivalence Principle: A Unified Resolution to the JWST High-Redshift Anomalies | [10.5281/zenodo.19000827](https://doi.org/10.5281/zenodo.19000827) |
| **Paper 13** | [TEP-WB](https://github.com/matthewsmawfield/TEP-WB) | Temporal Equivalence Principle: Temporal Shear Recovery in Gaia DR3 Wide Binaries | [10.5281/zenodo.19102061](https://doi.org/10.5281/zenodo.19102061) |
| **Paper 15** | [TEP-EFA](https://github.com/matthewsmawfield/TEP-EFA) | Temporal Equivalence Principle: Temporal Shear in the Earth Flyby Anomaly | [10.5281/zenodo.19454863](https://doi.org/10.5281/zenodo.19454863) |
| **Paper 16** | [TEP-J0437](https://github.com/matthewsmawfield/TEP-J0437) | Synchronization Holonomy in Pulsar Scintillation | [10.5281/zenodo.19454620](https://doi.org/10.5281/zenodo.19454620) |
| **Paper 17** | [TEP-LLR](https://github.com/matthewsmawfield/TEP-LLR) | Lunar Laser Ranging and the Nordtvedt Effect | [10.5281/zenodo.19446029](https://doi.org/10.5281/zenodo.19446029) |

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
  title={Global Time Echoes: Empirical Synthesis},
  author={Smawfield, Matthew Lukin},
  journal={Zenodo},
  year={2025},
  doi={10.5281/zenodo.18004832},
  note={Preprint v0.4 (Singapore)}
}
```

---

## Open Science Statement

These are working preprints shared in the spirit of open science—all manuscripts, analysis code, and data products are openly available under Creative Commons and MIT licenses to encourage and facilitate replication. Feedback and collaboration are warmly invited and welcome.

---

**Contact:** matthew@mlsmawfield.com  
**ORCID:** [0009-0003-8219-3159](https://orcid.org/0009-0003-8219-3159)

