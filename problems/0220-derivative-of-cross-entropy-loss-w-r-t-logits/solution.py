import numpy as np


def softmax(x, i):
	s_i = np.exp(x[i]) / np.sum([np.exp(x[k]) for k in range(len(x))])
	return s_i


def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	logits = np.array(logits)
	y = np.zeros(len(logits))
	y[target] = 1
	g = []
	
	for k in range(y.size):
		g.append(softmax(logits, k)  - y[k])
			
	return g
