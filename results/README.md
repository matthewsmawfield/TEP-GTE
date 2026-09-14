# Results Traceability

This directory documents the traceability chain for the numerical results
cited in the TEP-GTE manuscript (Paper 5, "Global Time Echoes: Empirical
Synthesis"). The manuscript is a synthesis paper; it does not generate new
primary data. All numerical results originate from the source papers
(Papers 1–4 and the broader TEP research program) and are reproduced here by
reference and, where the source repositories are available locally, by
symlink to the original output files.

## Source Repositories

| Paper | Repository | Local Path | Role in this manuscript |
|-------|-----------|------------|-------------------------|
| Paper 1 | [TEP-GNSS](https://github.com/matthewsmawfield/TEP-GNSS) | `../TEP-GNSS` | Multi-center GNSS correlation (CODE/IGS/ESA) |
| Paper 2 | [TEP-GNSS-II](https://github.com/matthewsmawfield/TEP-GNSS-II) | `../TEP-GNSS-II` | 25-year longitudinal CODE analysis; nutation & planetary events |
| Paper 3 | [TEP-GNSS-RINEX](https://github.com/matthewsmawfield/TEP-GNSS-RINEX) | `../TEP-GNSS-RINEX` | Raw RINEX / SPP consistency test (72 metric combinations) |
| Paper 4 | [TEP-GL](https://github.com/matthewsmawfield/TEP-GL) | `../TEP-GL` | Gravitational lensing; Phantom Mass; Earth–Galaxy scaling |

## Key Results Referenced in this Manuscript

The following headline numbers appear in the manuscript and trace to the
output files symlinked under `results/paper_*_*/`:

### Correlation length (λ_T = 4,201 ± 1,967 km; R² = 0.92–0.97)

- **Paper 1** (`paper_1_TEP-GNSS/step_2_0_correlation_analysis_summary.json`):
  multi-center exponential-decorrelation fits across CODE, IGS, and ESA
  processing centers.
- **Paper 1** (`paper_1_TEP-GNSS/meta_analysis_comprehensive.json`):
  comprehensive meta-analysis combining the three centers.
- **Paper 2** (`paper_2_TEP-GNSS-II/step_2_0_correlation_analysis_summary.json`):
  25-year CODE long-span headline correlation length.

### Spatial anisotropy (EW/NS = 2.16, p < 10⁻¹⁵)

- **Paper 1** (`paper_1_TEP-GNSS/step_2_0_correlation_analysis_summary.json`):
  East–West vs North–South azimuth-sector comparison.

### Orbital velocity coupling (r = −0.888, 3.65σ autocorrelation-corrected)

- **Paper 1** (`paper_1_TEP-GNSS/meta_analysis_comprehensive.json`):
  orbital-velocity regression and surrogate-test significance.

### CMB frame alignment (18.2°; Solar Apex geometrically incompatible)

- **Paper 1** (`paper_1_TEP-GNSS/meta_analysis_comprehensive.json`):
  CMB-dipole angular alignment and frame discrimination analysis.

### Planetary event responses (56/156 significant at ≥2σ)

- **Paper 2** (`paper_2_TEP-GNSS-II/planetary_events_jpl.json`):
  JPL ephemeris planetary-event response catalog.

### 18.6-year and semiannual nutation coupling (R² = 0.641; R² = 0.904)

- **Paper 2** (`paper_2_TEP-GNSS-II/nutation_surrogate_validation.json`):
  nutation harmonic regression and surrogate validation.

### Raw RINEX consistency (all 72 metric combinations; t up to 112)

- **Paper 3** (`paper_3_TEP-GNSS-RINEX/step_2_1_control_tests_summary.json`):
  SPP/broadcast-ephemeris control-test summary across metric combinations.
- **Paper 3** (`paper_3_TEP-GNSS-RINEX/step_2_1_elevation_analysis_summary.json`):
  elevation-dependent consistency summary.

### Gravitational lensing / Phantom Mass / Earth–Galaxy scaling

- **Paper 4** (`paper_4_TEP-GL/`): the TEP-GL repository is primarily
  theoretical; figure outputs are in `../TEP-GL/results/figures/`. The
  Earth–Galaxy scaling argument and Phantom Mass mechanism are documented in
  the Paper 4 manuscript.

## How to Regenerate

Each source repository contains its own pipeline (see the `scripts/README.md`
in the respective repo). To regenerate the primary results from scratch:

```bash
# Paper 1
cd "/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GNSS"
# see scripts/README.md

# Paper 2
cd "/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GNSS-II"
# see scripts/README.md

# Paper 3
cd "/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GNSS-RINEX"
# see scripts/README.md

# Paper 4
cd "/Users/matthewsmawfield/www/Temporal Equivalence Principle/TEP-GL"
# see scripts/README.md
```

## Note on Symlinks

The files under `results/paper_*_*/` are symbolic links to the corresponding
output files in the local source repositories. If the source repositories are
moved or removed, these links will dangle; in that case, clone the relevant
repository from GitHub and re-create the links, or refer directly to the
`results/outputs/` directory in each source repository.
