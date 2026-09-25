import numpy as np

def fn(seed, mean, std, n, bins):
    if isinstance(bins, (list, tuple, np.ndarray)):
        bins = np.asarray(bins).astype(float)
    np.random.seed(seed)
    samples = np.random.normal(mean, std, n)
    counts, edges = np.histogram(samples, bins=bins)
    return counts.tolist(), edges.tolist()