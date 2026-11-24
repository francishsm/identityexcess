# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0-pre] - 2026-11-24
> Pre-release for manuscript review & Zenodo archive. API is not stable.
### Added
- `ucell_rank_score()`: rank-first signature scoring (matches stage4 frozen pipeline)
- `compute_identity_excess()`: identity programme vs remodelling programme excess metric
- `tost_equivalence_test()`: permutation-based two one-sided equivalence test
- `pyproject.toml`: package definition for local pip install
- `CITATION.cff`: manuscript citation metadata
- `README.md`: overview, dependencies, installation and minimal code example
- `example.ipynb`: reproducible notebook with demo and visualization
- MIT LICENSE, .gitignore

### Notes
- This release corresponds to the v1.11 manuscript freeze of *Identity Programme vs Intra-program Remodelling in load-bearing fibrotic tissues*.
- No raw sequencing data is included; all raw datasets are available via GEO accession IDs listed in the manuscript.
