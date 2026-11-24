"""
core.py: identity excess calculation + null model / equivalence testing
"""
import numpy as np
import pandas as pd
from scipy.stats import permutation_test

def compute_identity_excess(score_identity: np.ndarray, score_program: np.ndarray) -> float:
    """
    Identity Programme vs Intra-program Remodelling excess metric.
    excess = median(score_identity) - median(score_program)
    """
    return np.median(score_identity) - np.median(score_program)

def tost_equivalence_test(x, y, eq_margin: float, n_perm=2000):
    """
    Two one-sided test (TOST) for equivalence, permutation null model.
    """
    def stat_fn(a,b):
        return np.median(a) - np.median(b)
    res = permutation_test((x,y), stat_fn, n_resamples=n_perm, alternative="two-sided")
    return {
        "delta": stat_fn(x,y),
        "pvalue": res.pvalue,
        "eq_margin": eq_margin
    }
