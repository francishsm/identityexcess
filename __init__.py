"""
identityexcess
Pre‑release Python toolkit (under manuscript review).
API subject to breaking changes.
Manuscript: Identity‑excess law separates constitutive fibroblast identity ...
Zenodo frozen archive for paper reproducibility: https://doi.org/10.5281/zenodo.24487895
"""

__version__ = "0.0.1-pre"
EXPERIMENTAL_API = True

from .core import compute_identity_excess, tost_equivalence_test
from .scoring import ucell_rank_score

__all__ = [
    "compute_identity_excess",
    "tost_equivalence_test",
    "ucell_rank_score",
    "__version__",
    "EXPERIMENTAL_API",
]
