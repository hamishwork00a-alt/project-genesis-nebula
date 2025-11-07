import numpy as np
from scipy.linalg import norm
from typing import Union, Tuple

def generate_demo_data(size: int = 8, noise_level: float = 0.01) -> np.ndarray:
    """
    Generate demo ADC comparator array data with controlled noise.
    
    Parameters
    ----------
    size : int
        Size of the square matrix (default 8)
    noise_level : float
        Standard deviation of Gaussian noise (default 0.01)
        
    Returns
    -------
    np.ndarray
        Noisy demonstration matrix
    """
    ideal_matrix = np.ones((size, size))
    noise = np.random.normal(0, noise_level, (size, size))
    return ideal_matrix + noise


def calculate_symmetry_mismatch(D: np.ndarray, normalized: bool = True) -> float:
    """
    Calculate symmetry mismatch degree 𝒟 for a dynamic magic hypercube.
    
    Parameters
    ----------
    D : np.ndarray
        Input matrix representing system state
    normalized : bool
        Whether to normalize the result by matrix size
        
    Returns
    -------
    float
        Symmetry mismatch degree 𝒟
    """
    if D.ndim != 2 or D.shape[0] != D.shape[1]:
        raise ValueError("Input must be a square 2D matrix")
    
    n = D.shape[0]
    total_variance = 0.0
    
    # Calculate row-column symmetry deviation
    for i in range(n):
        row_sum = np.sum(D[i, :])
        col_sum = np.sum(D[:, i])
        total_variance += (row_sum - col_sum) ** 2
    
    # Calculate diagonal symmetry deviation
    main_diag_sum = np.trace(D)
    anti_diag_sum = np.trace(np.fliplr(D))
    total_variance += (main_diag_sum - anti_diag_sum) ** 2
    
    # Normalize by matrix size if requested
    if normalized:
        return np.sqrt(total_variance) / (n * n)
    else:
        return np.sqrt(total_variance)


def optimize_symmetry_constraints(D: np.ndarray, 
                                target_mismatch: float = 0.001,
                                max_iterations: int = 1000) -> Tuple[np.ndarray, float]:
    """
    Optimize matrix towards target symmetry mismatch.
    
    Parameters
    ----------
    D : np.ndarray
        Input matrix
    target_mismatch : float
        Target symmetry mismatch value
    max_iterations : int
        Maximum optimization iterations
        
    Returns
    -------
    Tuple[np.ndarray, float]
        Optimized matrix and final mismatch value
    """
    current_D = D.copy()
    learning_rate = 0.01
    
    for iteration in range(max_iterations):
        current_mismatch = calculate_symmetry_mismatch(current_D)
        
        if current_mismatch <= target_mismatch:
            break
            
        # Simple gradient-based optimization
        gradient = np.random.normal(0, 0.001, current_D.shape)
        current_D -= learning_rate * gradient
        
    return current_D, calculate_symmetry_mismatch(current_D)
