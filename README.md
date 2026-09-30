# Global Time Echoes: Empirical Synthesis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18004832.svg)](https://doi.org/10.5281/zenodo.18004832)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

![Global Time Echoes](site/public/image.webp)

**Author:** Matthew Lukin Smawfield  
**Version:** v0.7 (Singapore)  
**First published:** 21 December 2025 · **Last updated:** 30 September 2026
**Status:** Preprint  
**DOI:** [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832)  
**Website:** [https://mlsmawfield.com/tep/gte/](https://mlsmawfield.com/tep/gte/)

## Abstract





Analysis of 25.3 years of GNSS timing data (2000–2025) reveals a persistent, distance-structured correlation in global atomic clock networks that tests whether corrected distributed GNSS timing residuals contain a coherent spatial covariance beyond the standard relativistic and geodetic measurement model. Examination of 165.2 million station-pair observations from 474 unique receivers (814 station codes) over a 25.3-year baseline demonstrates a spatial correlation signal decaying with distance over a finite scale (Gaussian-family kernels preferred in the 25-year dataset, exponential ΔAIC = 12.8; power law excluded at ΔAIC > 30; azimuth-averaged exponential scale λ = 3,210 ± 389 km, with cross-sector directional dispersion λ T = 4,201 ± 1,967 km across eight azimuthal sectors, a measurement of order thousands of kilometres rather than a single fixed scale), following cross-centre validation yielding R² = 0.92–0.97 across three distinct analysis-centre software architectures on a 62.7 million observation baseline. These findings emerge from a systematic multi-paper research program: theoretical framework development with pre-specified expectations and theoretical search ranges (Paper 0), multi-center consistency across software-diverse product families within the shared IGS tracking ecosystem (Paper 1), 25-year longitudinal analysis enabling long-period geophysical detection (Paper 2), raw-data consistency test strongly constraining precise-product processing artifacts (Paper 3), and cosmological extension testing whether temporal covariance or gradient effects contribute to dark-sector phenomenology (Paper 4). The evidence programme combines timing-network signatures, environmental tests and an optical sensitivity bound: distance-structured spatial decay over a finite scale; East-West/North-South anisotropy (ratio 2.16 ± 0.23, aggregate across the 25.3-year dataset; nominal pair-count p < 10 −15 ); orbital velocity coupling (r = −0.888, 3.65σ autocorrelation-corrected; surrogate p < 2 × 10⁻⁷ as a resolution bound); a recovered annual-phase direction near Earth's aphelion velocity tangent (RA = 6°, Dec = +4°; directional-rank permutation p < 10⁻⁵; the directed CMB-apex template is anti-phase and the Solar Apex is geometrically incompatible, predicting N-S anisotropy against the observed E-W dominance; no global full-sky-search surrogate p-value has been computed; on the MGEX product the scan is projection-degenerate); an optical-domain sensitivity bound (SLR sampling-matched controls reproduce the apparent spectral concentration; inter-station candidates remain exploratory); a planetary event catalogue (56/156 significant at ≥ 2σ under the free-centre pulse statistic — repeatable estimator behaviour whose excess is attributable to calendar-position sampling in the season-preserving RINEX controls; the 40-event opposition subset is null-validated at 5.5 ×  and a continuous planetary-potential correlation survives at r = +0.116, p = 0.012); 18.6-year lunar nutation coupling (R² = 0.641 ± 0.10 over 1.36 cycles); pulsar spin-down excess (exploratory channel); and host-potential H 0 correlation. On the held-out MGEX product the distance-structured coherence replicates (λ ≈ 1,862 km), while the anisotropy and primary orbital-velocity metrics do not replicate robustly. Raw RINEX consistency test using Single Point Positioning with broadcast ephemerides achieves consistent signal detection across all 72 metric combinations (t-statistics up to 112, Cohen's d up to 0.304), strongly constraining precise-product processing artifacts as the sole origin. Broadcast ephemerides still contain control-segment information; Satellite Laser Ranging supplies a GNSS-product-independent test pathway, whose present sensitivity and exploratory correlations do not yet adjudicate the origin of the GNSS signal, while the generic orbit-projection confound is reserved for the physical-confound forward model and orbit-free clock channels. The network's selectivity profile—sensitive to velocity-dependent dynamics while blind to GM/r² scaling and solar rotation—characterizes it as an inertial interferometer measuring correlation geometry rather than a gravimeter measuring Newtonian force. Table 5 scores these observations against the pre-specified expectations of the Temporal Equivalence Principle: the orbital-velocity sign, EW > NS ordering, band localization, and GM/r² null are met, while the 2,000–3,000 km screening-parameterized forecast, the < 5% cross-centre criterion, and—in the 25-year data—the exponential-kernel preference are not met. TEP is a bi-metric scalar-tensor framework in which proper time is a dynamical field governed by a conformal factor A(ϕ) = exp(β A ϕ/M Pl ). Temporal Shear suppression operates through the continuous spatial profile of the ϕ field (Temporal Topology), with suppression arising from the non-linear superposition of field gradients (Temporal Shear), replacing discrete thin-shell approximations with a geometrically continuous mechanism. The observed correlation length λ T represents the characteristic scale of Temporal Topology. Environmental screening, derivative-screened, and saturation-radius interpretations are candidate theoretical completions, not the primary empirical claim; the saturation-radius interpretation R T is adopted in the present framework (§4.4.2). The framework preserves local Lorentz invariance while predicting spatially correlated clock-network residuals in the conformal sector and closed-loop synchronization holonomy in the disformal/non-exact sector. The measured GNSS covariance is interpreted primarily as a conformal-sector A(ϕ) observable; it should not be identified with the non-zero closed-loop holonomy predicted only by the non-exact/disformal sector. The empirical evidence presented here therefore supports the conformal sector alone; the disformal-sector holonomy — the framework's definitive discriminating test — remains unmeasured at the canonical amplitude (the J0437 phase-closure detection attests non-exact transport but sits roughly two orders of magnitude above the canonical connection's ceiling on that sightline). Evidence Tiers: A (Paper 0/EXP): Foundational theory with pre-specified search ranges; B (GNSS I–III): Primary timing-network evidence; C (SLR): Optical-domain bound and exploratory correlation test; D (H₀, COS, WB): Environmental response tests; E (JWST, GL, UCD, RBH): Conditional astrophysical/cosmological extensions. These evidence channels are not statistically independent: the exponential decay, anisotropy, orbital coupling, preferred-axis recovery, nutation, and planetary-catalogue signatures share the same GNSS data and phase-alignment method, while the SLR check, pulsar spin-down, and host-potential H 0 correlation use distinct data — the effective number of independent tests is smaller than the number of listed results, and smaller still at channel level: the SLR check reads the same conformal clock sector through different hardware, the CMB axis is product-unstable, and the pulsar channel is exploratory (its standalone evidence uninformative — mildly GR-favouring — in the J0337 adjudication, where the kinetic impedance solved in Paper 0 suppresses the differential acceleration ratio to η ≈ 2.5 × 10⁻⁷, well within the experimental bound 2.6 × 10⁻⁶). Critically, the conformal sector responsible for clock-rate modulation is not directly constrained by photon–graviton differential-propagation tests such as GW170817, although local conformal-gradient/source-charge sectors remain constrained by PPN, clock, and equivalence-principle tests. If validated through independent replication, TEP predicts that the dynamical phenomenology attributed to dark matter is the observational projection of Temporal Topology and Temporal Shear, not evidence for a new particulate matter component. In this interpretation, GNSS-scale covariance, dynamical phantom mass — with lensing tracking the gravitating matter (Papers 4, 19) — and galactic mass discrepancies are different observational projections of the same time-field topology, with Papers 4 and 13 testing distinct optical and dynamical projections of the environmental-response architecture (Paper 4: the dynamical–lensing mass difference as a phantom-mass test; Paper 13: the SPARC-anchored wide-binary transition), not a derived Earth-to-galaxy covariance-to-shear transfer kernel. The phantom-mass prediction is conditional on the Temporal Shear surviving unscreened at galactic scales — an amplitude whose deep-regime derivation from the action is identified in Paper 0 as the decisive open calculation — and is presented as a conditional consequence, not an established result. The 4,000 km correlation on Earth and galactic-scale phenomenology are interpreted within TEP as manifestations of the same environment-dependent Temporal-Topology response, which provides continuous Temporal Topology relaxation from deep potential wells to the weak-field regime. The saturation-density scale ρ T ≈ 20 g/cm³, and the diagnostic radius R T = (3M/4πρ T ) 1/3 it defines for each body, remain testable through interplanetary missions. Explicit falsification criteria include: failure of independent groups to replicate the raw carrier-phase signal; Temporal Topology correlation length falling outside the 500–20,000 km range; adjudication of the ephemeris-artifact question — GNSS-product provenance via the Satellite Laser Ranging check, and the wider orbit-projection confound via the physical-confound forward model or an orbit-free clock channel; and null synchronization holonomy in closed-loop triangular time-transfer experiments.


## Key Findings

This synthesis integrates Papers 1–4 and documents nine convergent signatures: exponential spatial decay (λ<sub>T</sub> = 4,201 ± 1,967 km; 95% CL ≈ 2,300–8,100 km), EW/NS anisotropy (ratio 2.16), orbital velocity coupling (r = −0.888; 3.65σ autocorrelation-corrected, surrogate p < 2 × 10⁻⁷ as a resolution bound), annual-phase direction recovery near Earth's aphelion velocity tangent (CMB apex anti-phase; Solar Apex null), instrument-level universality (SLR optical chain consuming no GNSS products), planetary event responses (56/156 significant; 13/29 non-overlapping windows vs ~1.3 expected), 18.6-year lunar nutation (R² = 0.641 ± 0.10), exploratory pulsar spin-down excess, and host-potential H₀ correlation. The signatures share data and method, so the effective number of independent tests is smaller than nine — a joint ~10σ claim is not asserted. Raw RINEX validation detects the signal across all 72 metric combinations (mean R² = 0.93), strongly constraining processing artifacts. The observed correlation length is identified with the geometric saturation radius R<sub>T</sub> = (3M/4πρ<sub>T</sub>)<sup>1/3</sup> ≈ 4,150 km (Paper 6, UCD), linking terrestrial timing networks to lensing-scale phenomenology through the continuous relaxation of Temporal Topology.

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
| **Paper 15** | [TEP-EFA](https://github.com/matthewsmawfield/TEP-EFA) | Temporal Equivalence Principle: Temporal Shear in the Earth Flyby Anomaly | [10.5281/zenodo.19454862](https://doi.org/10.5281/zenodo.19454862) |
| **Paper 16** | [TEP-J0437](https://github.com/matthewsmawfield/TEP-J0437) | Synchronization Holonomy in Pulsar Scintillation | [10.5281/zenodo.19454620](https://doi.org/10.5281/zenodo.19454620) |
| **Paper 17** | [TEP-LLR](https://github.com/matthewsmawfield/TEP-LLR) | Lunar Laser Ranging and the Nordtvedt Effect | [10.5281/zenodo.19446028](https://doi.org/10.5281/zenodo.19446028) |

## Paper Structure

1. **Introduction** — The synchronization residual problem, historical context, theoretical motivation
2. **Phenomenology** — Spatial correlation structure, nine signatures, annual-phase direction, selectivity profile
3. **Validation** — Processing artifacts, ionospheric/geomagnetic/tropospheric hypotheses, long-period stability
4. **Theoretical Framework** — Two-metric geometry, Temporal Topology and Temporal Shear, geometric saturation-radius screening (R_T), synchronization holonomy
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
  note={Preprint v0.7 (Singapore)}
}
```

---

## Open Science Statement

These are working preprints shared in the spirit of open science—all manuscripts, analysis code, and data products are openly available under Creative Commons and MIT licenses to encourage and facilitate replication. Feedback and collaboration are warmly invited and welcome.

---

**Contact:** matthew@mlsmawfield.com  
**ORCID:** [0009-0003-8219-3159](https://orcid.org/0009-0003-8219-3159)
