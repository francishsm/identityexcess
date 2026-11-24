# identityexcess
Python toolkit for identity‑excess analysis of fibroblast matrix remodelling under mechanical load.
Companion code for manuscript: *Identity Programme vs Intra‑program Remodelling in load‑bearing fibrotic tissues*.

> Pre‑release version: API may be subject to breaking changes before formal publication.

## Overview
This package implements the identity‑excess metric and permutation‑based TOST equivalence test, alongside rank‑first signature scoring fully consistent with the frozen scRNA‑seq pipeline described in the manuscript.

- `compute_identity_excess()`: Compute excess between identity programme and intra‑program remodelling programme scores
- `tost_equivalence_test()`: Permutation two one‑sided test for equivalence
- `ucell_rank_score()`: Rank‑first signature scoring (match stage4 pipeline)

## Dependencies
- numpy
- scipy
- pandas

## Installation
```bash
pip install .
