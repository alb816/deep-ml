import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
    """
    Compute the Jensen-Shannon Divergence between two probability distributions.
    
    Args:
        P: First probability distribution
        Q: Second probability distribution
    
    Returns:
        Jensen-Shannon Divergence value
    """
    P = np.asarray(P)
    Q = np.asarray(Q)

    M = 1/2 * (P + Q)

    jsd = 1/2 * (np.sum(np.where(P > 0, P * np.log(P / M), 0.0)) 
                 + 
                 np.sum(np.where(Q > 0, Q * np.log(Q / M), 0.0))
                )

    return np.clip(jsd, 0.0, np.log(2))