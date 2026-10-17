# Global Time Echoes: Empirical Synthesis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18004832.svg)](https://doi.org/10.5281/zenodo.18004832)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Global Time Echoes](site/public/image.webp)

**Author:** Matthew Lukin Smawfield  
**Version:** v0.8 (Singapore)  
**First published:** 21 December 2025 · **Last updated:** 17 October 2026  
**Status:** Preprint  
**DOI:** [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832)  
**Website:** [https://mlsmawfield.com/tep/gte/](https://mlsmawfield.com/tep/gte/)  
**Paper Series:** TEP Series · Group B (II. Global Time Echoes: GNSS Atomic Clock Networks) · Paper 5 (`B5`)

## Abstract

<!-- Generated from site/components/abstract.html; update the manuscript source, then run tools/sync_current_corpus_readmes.py. -->

Analysis of 25.3 years of GNSS timing data (2000–2025) reveals a persistent, distance-structured correlation in global atomic clock networks that tests whether corrected distributed GNSS timing residuals contain a coherent spatial covariance beyond the standard relativistic and geodetic measurement model. Examination of 165.2 million station-pair observations from 474 unique receivers (814 station codes) over a 25.3-year baseline demonstrates a spatial correlation signal decaying with distance over a finite scale (Gaussian-family kernels preferred in the 25-year dataset, exponential ΔAIC = 12.8; power law excluded at ΔAIC > 30; azimuth-averaged exponential scale λ = 3,210 ± 389 km, with cross-sector directional dispersion λ_T = 4,201 ± 1,967 km across eight azimuthal sectors, a measurement of order thousands of kilometres rather than a single fixed scale), following cross-centre validation yielding R² = 0.92–0.97 across three distinct analysis-centre software architectures on a 62.7 million observation baseline. These findings emerge from a systematic multi-paper research program: theoretical framework development with pre-specified expectations and theoretical search ranges (Paper 0), multi-center consistency across software-diverse product families within the shared IGS tracking ecosystem (Paper 1), 25-year longitudinal analysis enabling long-period geophysical detection (Paper 2), raw-data consistency test strongly constraining precise-product processing artifacts (Paper 3), and cosmological extension testing whether temporal covariance or gradient effects contribute to dark-sector phenomenology (Paper 4).

The evidence programme combines timing-network signatures, environmental tests, and an optical sensitivity bound: distance-structured spatial decay over a finite scale; East-West/North-South anisotropy (ratio 2.16 ± 0.23 across the 25.3-year aggregate; nominal pair-count p $\lt$ 10⁻¹⁵); orbital velocity coupling (r = −0.888, 3.65σ autocorrelation-corrected; surrogate p $\lt$ 2×10⁻⁷ resolution bound); a recovered annual-phase direction near Earth's aphelion velocity tangent (RA = 6°, Dec = +4°; directional-rank permutation p $\lt$ 10⁻⁵, with the directed CMB-apex template anti-phase, the Solar Apex geometrically incompatible, and MGEX projection-degenerate); outer-planet opposition coupling (40-event opposition subset null-validated at 5.5× over matched random dates, p $\lt$ 10⁻¹⁷, alongside a continuous planetary-potential correlation r = +0.116, p = 0.012, whereas the broader 156-event free-centre pulse scan reflects calendar-position sampling on the seasonal series); 18.6-year lunar nutation coupling (R² = 0.641 ± 0.10 over 1.36 cycles); an optical-domain sensitivity bound from passive Satellite Laser Ranging (sampling-matched controls reproduce the apparent spectral concentration; inter-station candidates remain exploratory); pulsar spin-down excess (exploratory channel); and host-potential H_0 correlation. On the held-out MGEX product the distance-structured coherence replicates (λ ≈ 1,862 km), while the anisotropy and primary orbital-velocity metrics do not replicate robustly. Raw RINEX Single Point Positioning with broadcast ephemerides achieves consistent signal detection across all 72 metric combinations (t-statistics up to 112, Cohen's d up to 0.304), strongly constraining precise-product processing artifacts as the sole origin. Because broadcast ephemerides still carry control-segment orbit information, terrestrial closure is structured in three tiers: the GNSS analyses characterize the macroscopic microwave clock-network covariance; Satellite Laser Ranging supplies a hardware- and orbit-independent optical sensitivity bound ($\delta A \lesssim 2\times 10^{-8}$); and physical-confound forward models together with orbit-free optical-fiber and two-way time-transfer links adjudicate the residual orbit-projection channel at atomic-clock precision. The network's selectivity profile—sensitive to velocity-dependent dynamics while blind to GM/r² scaling and solar rotation—characterizes it as an inertial interferometer measuring correlation geometry rather than a gravimeter measuring Newtonian force.

Table 5 scores these observations against the pre-specified expectations of the Temporal Equivalence Principle: the orbital-velocity sign, EW > NS ordering, band localization, and GM/r² null are met, while the 2,000–3,000 km screening-parameterized forecast, the $\lt$ 5% cross-centre criterion, and—in the 25-year data—the exponential-kernel preference are not met. TEP is a bi-metric scalar-tensor framework in which proper time is a dynamical field governed by a conformal factor A(ϕ) = exp(β_Aϕ/M_Pl). Temporal Shear suppression operates through the continuous spatial profile of the ϕ field (Temporal Topology), with suppression arising from the non-linear superposition of field gradients (Temporal Shear), replacing discrete thin-shell approximations with a geometrically continuous mechanism. The observed correlation length λ_T represents the characteristic scale of Temporal Topology. Environmental screening, derivative-screened, and saturation-radius interpretations are candidate theoretical completions, not the primary empirical claim; the saturation-radius interpretation R_T is adopted in the present framework (§4.4.2). The framework preserves local Lorentz invariance while predicting spatially correlated clock-network residuals in the conformal sector and closed-loop synchronization holonomy in the disformal/non-exact sector. The measured GNSS covariance is interpreted primarily as a conformal-sector \(A(\phi)\) observable; it should not be identified with the non-zero closed-loop holonomy predicted only by the non-exact/disformal sector. The empirical evidence presented here therefore supports the conformal sector alone; the disformal-sector holonomy — the framework's definitive discriminating test — remains unmeasured at the canonical amplitude (the J0437 phase-closure detection attests non-exact transport but sits roughly two orders of magnitude above the canonical connection's ceiling on that sightline).

Evidence Tiers: A (Paper 0/EXP): Foundational theory with pre-specified search ranges; B (GNSS I–III): Primary timing-network evidence; C (SLR): Optical-domain bound and exploratory correlation test; D (H₀, COS, WB): Environmental response tests; E (JWST, GL, UCD, RBH): Conditional astrophysical/cosmological extensions. These evidence channels are not statistically independent: the exponential decay, anisotropy, orbital coupling, preferred-axis recovery, nutation, and planetary-catalogue signatures share the same GNSS data and phase-alignment method, while the SLR check, pulsar spin-down, and host-potential H_0 correlation use distinct data — the effective number of independent tests is smaller than the number of listed results, and smaller still at channel level: the SLR check reads the same conformal clock sector through different hardware, the CMB axis is product-unstable, and the pulsar channel is exploratory (its standalone evidence uninformative — mildly GR-favouring — in the J0337 adjudication, where the kinetic impedance solved in Paper 0 suppresses the differential acceleration ratio to $\eta \simeq 2.5 \times 10^{-7}$, well within the experimental bound $2.6 \times 10^{-6}$). Critically, the conformal sector responsible for clock-rate modulation is not directly constrained by photon–graviton differential-propagation tests such as GW170817, although local conformal-gradient/source-charge sectors remain constrained by PPN, clock, and equivalence-principle tests.

If validated through independent replication, TEP predicts that the dynamical and optical phenomenology attributed to dark matter is the observational projection of Temporal Topology and Temporal Shear across unstretched space, not evidence for a new particulate matter component. In this interpretation, GNSS-scale covariance, dynamical phantom mass, and unstretched-space optical refraction (Papers 4, 18, 19; where intermediate clock rates $A_{\rm loc}(u_{\rm grav}(\mathbf x))$ along the shared ADM lapse $N_{\rm TEP}=A_{\rm loc}N_{\rm GR}$ at fixed spatial 3-metric $\gamma_{ij}$ refract light via $n(x)\simeq 1-2\Phi_N/c²-\beta_A u_{\rm grav}(x)$, whereas isotropic conformal rescaling $\tilde g_{\mu\nu}=A² g_{\mu\nu}$ cancels out of null rays) are different observational projections of the same time-field topology, with Papers 4, 6, 13, and 19 testing distinct optical and dynamical projections of the environmental-response architecture on the selected two-branch action $P_{,X}=k\sqrt\xi+2\xi$ ($k=16.03$ fixed by $a_0$, zero per-system free parameters), not a derived Earth-to-galaxy covariance-to-shear transfer kernel. The 4,000 km correlation on Earth and galactic-scale phenomenology are interpreted within TEP as manifestations of the same environment-dependent Temporal-Topology response, which provides continuous Temporal Topology relaxation from deep potential wells to the weak-field regime. The saturation-density scale ρ_T ≈ 20 g/cm³, and the diagnostic radius R_T = (3M/4πρ_T)¹/3 it defines for each body, remain testable through interplanetary missions. Explicit falsification criteria include: failure of independent groups to replicate the raw carrier-phase signal; Temporal Topology correlation length falling outside the 500–20,000 km range; adjudication of the ephemeris-artifact question — GNSS-product provenance via the Satellite Laser Ranging check, and the wider orbit-projection confound via the physical-confound forward model or an orbit-free clock channel; and null synchronization holonomy in closed-loop triangular time-transfer experiments.

Keywords: Temporal Equivalence Principle, GNSS, atomic clocks, preferred direction, dark matter, gravitational lensing, scalar-tensor gravity, synchronization holonomy, Temporal Topology, Temporal Shear, nonlinear screening mechanisms

Current manuscript source: [abstract.html](site/components/abstract.html).

## Key Findings

The current findings, numerical results and comparison assumptions are reported in [7. Conclusions](site/components/section_7_conclusions.html). The abstract above is synchronized from the current manuscript.

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
| **Paper 16** | [TEP-J0437](https://github.com/matthewsmawfield/TEP-J0437) | Synchronization Holonomy in Pulsar Scintillation | [10.5281/zenodo.19454619](https://doi.org/10.5281/zenodo.19454619) |
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
  note={Preprint v0.8 (Singapore)}
}
```

---

## Open Science Statement

These are working preprints shared in the spirit of open science—all manuscripts, analysis code, and data products are openly available under Creative Commons and MIT licenses to encourage and facilitate replication. Feedback and collaboration are warmly invited and welcome.

---

**Contact:** matthew@mlsmawfield.com  
**ORCID:** [0009-0003-8219-3159](https://orcid.org/0009-0003-8219-3159)
