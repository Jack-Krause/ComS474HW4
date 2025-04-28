import numpy as np
import pandas as pd

def best_linkage_pair(mat, g1, g2, similarity_type='single'):
    sub   = mat.loc[g1, g2]
    pairs = sub.stack()
    same  = (pairs.index.get_level_values(0) ==
             pairs.index.get_level_values(1))
    pairs = pairs[~same]
    if similarity_type == 'single':
        return pairs.nsmallest(1)
    else:
        return pairs.nlargest(1)

def merge_clusters(mat, c1, c2, new_label, similarity_type='single'):
    remaining = [c for c in mat.index if c not in (c1, c2)]
    sims = [
        (min(mat.at[c1, c], mat.at[c2, c])
         if similarity_type=='single' else
         max(mat.at[c1, c], mat.at[c2, c]))
        for c in remaining
    ]

    new_mat = mat.drop(index=[c1, c2], columns=[c1, c2])

    new_mat[new_label] = np.nan

    new_mat.loc[remaining, new_label] = sims
    new_mat.loc[new_label, remaining] = sims

    new_mat.at[new_label, new_label] = 1.0

    new_mat = new_mat.reindex(
        index=remaining + [new_label],
        columns=remaining + [new_label]
    )
    return new_mat


def agglomerative_clustering(sim_mat, similarity_type='single', stop_at=1):
    """
    Agglomeratively merge until `sim_mat` has `stop_at` clusters left.
    Prints the matrix at each step.
    
    sim_mat : pd.DataFrame
    similarity_type    : 'single' or 'complete'
    stop_at : int, how many clusters you want to end up with
    """
    print(f"\n\nSTART: {similarity_type}")
    current = sim_mat.copy()
    step = 1
    
    while current.shape[0] > stop_at:
        labels = list(current.index)
        
        best = best_linkage_pair(current, labels, labels, similarity_type=similarity_type)
        (c1, c2), simval = best.index[0], best.iloc[0]
        
        new_label = f"{c1}_{c2}"
        current = merge_clusters(current, c1, c2, new_label, similarity_type=similarity_type)
        
        print(f"\nStep {step}: merge {c1} & {c2} (sim={simval:.2f})")
        print(current.to_string())
        
        step += 1
    
    return current



labels = ['p1','p2','p3','p4','p5']
similarity_vals = np.array([
    [1.00, 0.10, 0.41, 0.55, 0.35],
    [0.10, 1.00, 0.64, 0.47, 0.98],
    [0.41, 0.64, 1.00, 0.44, 0.85],
    [0.55, 0.47, 0.44, 1.00, 0.76],
    [0.35, 0.98, 0.85, 0.76, 1.00]
])

sim_mat = pd.DataFrame(similarity_vals, index=labels, columns=labels)
single_final = agglomerative_clustering(sim_mat, similarity_type='single', stop_at=3)
complete_final = agglomerative_clustering(sim_mat, similarity_type='complete', stop_at=3)
# single_final = agglomerative_clustering(sim_mat, similarity_type='single')
# complete_final = agglomerative_clustering(sim_mat, similarity_type='complete')
