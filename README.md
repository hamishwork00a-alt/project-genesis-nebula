# Shenqu Algorithm: Calibrating Reality with Symmetry

A novel mathematical framework that redefines analog-to-digital converter (ADC) calibration by quantifying and correcting symmetry mismatches (𝒟) in the dynamic magic hypercube of comparator arrays.

## Installation
```bash
pip install -r requirements.txt
pip install -e .
```

## Quick Start

```python
from shenqu import core
D = core.generate_demo_data()
mismatch = core.calculate_symmetry_mismatch(D)
print(f"System Symmetry Mismatch: {mismatch:.6f}")
```

## Theory

See docs/theory_background.md for the mathematical foundation.

```
