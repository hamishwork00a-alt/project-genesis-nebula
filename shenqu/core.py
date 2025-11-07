import numpy as np
from scipy.linalg import norm

def generate_demo_data(size=8, noise_level=0.01):
    """生成带噪声的模拟ADC比较器阵列数据"""
    ideal_matrix = np.ones((size, size))
    noise = np.random.normal(0, noise_level, (size, size))
    return ideal_matrix + noise

def calculate_symmetry_mismatch(D):
    """计算动态幻方的对称性失配度 𝒟"""
    if D.shape[0] != D.shape[1]:
        raise ValueError("Input matrix must be square")
    
    n = D.shape[0]
    total_variance = 0.0
    
    # 计算行和列的对称性偏差
    for i in range(n):
        row_sum = np.sum(D[i, :])
        col_sum = np.sum(D[:, i])
        total_variance += (row_sum - col_sum)**2
    
    # 计算对角线对称性偏差  
    main_diag_sum = np.trace(D)
    anti_diag_sum = np.trace(np.fliplr(D))
    total_variance += (main_diag_sum - anti_diag_sum)**2
    
    return np.sqrt(total_variance) / (n * n)
