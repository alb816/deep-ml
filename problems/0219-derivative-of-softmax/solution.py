import numpy as np

def softmax(x: list[float], i: int) -> float:
	s_i = np.exp(x[i]) / np.sum([np.exp(x[k]) for k in range(len(x))])
	return s_i
	
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	J = []
	d_ij = 0
	for i in range(len(x)):
		j_row = []
		for j in range(len(x)):
			if i == j:
				d_ij = 1
			else:
				d_ij = 0
			j_row.append(softmax(x, i) * (d_ij - softmax(x, j)))
		J.append(j_row)
	return J