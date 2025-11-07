"""
Shenqu Algorithm - Symmetry-based Calibration Framework

A novel mathematical framework that redefines system calibration by quantifying
and correcting symmetry mismatches in dynamic multi-dimensional structures.
"""

__version__ = "1.0.0"
__author__ = "Project Genesis Team"

from .core import (
    generate_demo_data,
    calculate_symmetry_mismatch,
    optimize_symmetry_constraints
)

from .calibration import (
    AdaptiveCalibrator,
    SymmetryOptimizer
)

__all__ = [
    'generate_demo_data',
    'calculate_symmetry_mismatch', 
    'optimize_symmetry_constraints',
    'AdaptiveCalibrator',
    'SymmetryOptimizer',
]
