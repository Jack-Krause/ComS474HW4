import numpy as np
import pandas as pd

def best_linkage_pair(mat, g1, g2, kind='single'):
    """
    Returns a length‑1 Series whose index is (i, j) and value is the best
    inter‑cluster distance, but ignores diagonal self‑similarities.

    kind : 'single'  → pick the *smallest* of the off‑diagonal values
           'complete' → pick the *largest* of the off‑diagonal values
    """
    sub   = mat.loc[g1, g2]      # DataFrame |g1|×|g2|
    pairs = sub.stack()          # Series indexed by (i, j)

    # drop all self‑pairs where i == j
    same = pairs.index.get_level_values(0) == pairs.index.get_level_values(1)
    pairs = pairs[~same]

    if kind == 'single':
        return pairs.nsmallest(1)
    else:
        return pairs.nlargest(1)


labels = ['p1','p2','p3','p4','p5']
similarity_vals = np.array([
    [1.00, 0.10, 0.41, 0.55, 0.35],
    [0.10, 1.00, 0.64, 0.47, 0.98],
    [0.41, 0.64, 1.00, 0.44, 0.85],
    [0.55, 0.47, 0.44, 1.00, 0.76],
    [0.35, 0.98, 0.85, 0.76, 1.00]
])
sim_mat = pd.DataFrame(similarity_vals, index=labels, columns=labels)

# Example calls:
print(best_linkage_pair(sim_mat, labels, labels, kind='single'))
# p1  p2    0.10
# dtype: float64

print(best_linkage_pair(sim_mat, labels, labels, kind='complete'))
# p2  p5    0.98
# dtype: float65
