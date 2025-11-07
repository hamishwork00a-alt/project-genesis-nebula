#!/usr/bin/env python3
"""
Basic usage example for Shenqu Algorithm.
"""

import numpy as np
import matplotlib.pyplot as plt
from shenqu.core import generate_demo_data, calculate_symmetry_mismatch

def demonstrate_algorithm():
    """Demonstrate the core algorithm functionality."""
    print("🚀 Shenqu Algorithm Demonstration")
    print("=" * 50)
    
    # Generate demo data
    ideal_matrix = np.ones((8, 8))
    noisy_matrix = generate_demo_data(size=8, noise_level=0.03)
    
    # Calculate symmetry mismatches
    ideal_mismatch = calculate_symmetry_mismatch(ideal_matrix)
    noisy_mismatch = calculate_symmetry_mismatch(noisy_matrix)

    # 在打印校准潜力之前添加检查
if ideal_mismatch > 0:
    improvement_ratio = noisy_mismatch / ideal_mismatch
    print(f"Calibration potential: {improvement_ratio:.1f}x improvement")
else:
    print("Calibration potential: Perfect symmetry achieved (infinite improvement possible)")
    
    print(f"Ideal matrix symmetry mismatch: {ideal_mismatch:.6f}")
    print(f"Noisy matrix symmetry mismatch: {noisy_mismatch:.6f}")
    print(f"Calibration potential: {noisy_mismatch/ideal_mismatch:.1f}x improvement")
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot ideal matrix
    im1 = ax1.imshow(ideal_matrix, cmap='viridis', interpolation='nearest')
    ax1.set_title(f'Ideal System\nSymmetry Mismatch: {ideal_mismatch:.6f}')
    plt.colorbar(im1, ax=ax1)
    
    # Plot noisy matrix  
    im2 = ax2.imshow(noisy_matrix, cmap='viridis', interpolation='nearest')
    ax2.set_title(f'Real System with Noise\nSymmetry Mismatch: {noisy_mismatch:.6f}')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.savefig('symmetry_demonstration.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return ideal_mismatch, noisy_mismatch

if __name__ == "__main__":
    demonstrate_algorithm()
