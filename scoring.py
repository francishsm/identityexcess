"""
scoring.py: rank-based UCell signature scoring (match your frozen pipeline)
"""
import numpy as np

def ucell_rank_score(mat, gene_list):
    """
    Fast rank-based UCell, consistent with your stage4 pipeline:
    rank all genes per cell first, then average rank of signature genes.
    mat: cell × gene matrix (AnnData.X or numpy array)
    """
    n_cell, n_gene = mat.shape
    ranks = np.argsort(np.argsort(mat, axis=1), axis=1)
    gene_idx = np.isin(np.arange(n_gene), gene_list)
    score = ranks[:, gene_idx].mean(axis=1) / n_gene
    return score
