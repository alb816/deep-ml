import numpy as np


def cov(x: np.ndarray, y: np.ndarray) -> float:
    """Вычисляет ковариацию между двумя векторами."""
	
    # Центрируем векторы (вычитаем математическое ожидание)
    x_centered = x - np.mean(x)
    y_centered = y - np.mean(y)

    # Находим ковариацию через среднее произведение центрированных значений
    covariance = np.dot(x_centered, y_centered) / (len(x) - 1)

    return covariance


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    """Вычисляет ковариационную матрицу с использованием циклов (покомпонентно)."""
    n_feats = len(vectors)
    cov_matrix = np.zeros((n_feats, n_feats))

    for i in range(n_feats):
        for j in range(n_feats):
            cov_matrix[i, j] = cov(vectors[i], vectors[j])

    return cov_matrix