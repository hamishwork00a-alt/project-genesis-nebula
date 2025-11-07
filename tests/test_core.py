import pytest
import numpy as np
from shenqu.core import generate_demo_data, calculate_symmetry_mismatch

class TestCoreFunctionality:
    """Test core algorithm functionality."""
    
    def test_demo_data_generation(self):
        """Test demo data generation produces correct shapes."""
        data = generate_demo_data(size=8, noise_level=0.01)
        assert data.shape == (8, 8)
        assert isinstance(data, np.ndarray)
        
    def test_symmetry_mismatch_ideal(self):
        """Test symmetry mismatch calculation on ideal matrix."""
        ideal_matrix = np.ones((4, 4))
        mismatch = calculate_symmetry_mismatch(ideal_matrix)
        assert mismatch == 0.0  # Perfect symmetry
        
    def test_symmetry_mismatch_noisy(self):
        """Test symmetry mismatch on noisy matrix."""
        noisy_matrix = generate_demo_data(size=4, noise_level=0.1)
        mismatch = calculate_symmetry_mismatch(noisy_matrix)
        assert mismatch > 0.0  # Should have some mismatch
        
    def test_invalid_input(self):
        """Test error handling for invalid inputs."""
        with pytest.raises(ValueError):
            calculate_symmetry_mismatch(np.ones((3, 4)))  # Non-square matrix
