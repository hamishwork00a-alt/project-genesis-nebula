Shenqu Algorithm Documentation
==============================

Symmetry-Based Calibration for High-Precision Systems

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   theory

Introduction
------------

The Shenqu Algorithm provides a novel mathematical framework for quantifying
and correcting symmetry mismatches in multi-dimensional systems. It is
particularly useful for:

- ADC/DAC calibration and optimization
- Quantum system simulation
- High-precision measurement systems
- Multi-physics modeling

Quick Start
-----------

.. code-block:: python

   from shenqu import generate_demo_data, calculate_symmetry_mismatch

   # Analyze system symmetry
   system_data = generate_demo_data(size=8, noise_level=0.02)
   mismatch = calculate_symmetry_mismatch(system_data)

   print(f"System symmetry mismatch: {mismatch:.6f}")

API Reference
-------------

.. automodule:: shenqu.core
   :members:
   :undoc-members:

.. automodule:: shenqu.calibration
   :members:
   :undoc-members:
