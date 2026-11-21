import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
    """
    Compute entropy of P and cross-entropy between P and Q.
    
    Args:
        P: True probability distribution
        Q: Predicted probability distribution
    
    Returns:
        Tuple of (entropy H(P), cross-entropy H(P,Q))
    """
    P = np.asarray(P)
    Q = np.asarray(Q)

    self_inf = -np.log(P)
    entropy = np.dot(P, -np.log(P)) if not np.any(P == 0) else 0.0
    cross_entropy = np.dot(P, -np.log(Q)) if not np.any((P > 0.0) & (Q == 0)) else float('inf')
    return (round(entropy, 6), round(cross_entropy, 6))