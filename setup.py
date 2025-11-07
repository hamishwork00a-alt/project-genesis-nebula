from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shenqu-algorithm",
    version="1.0.0",
    author="Project Genesis Team",
    author_email="contact@project-genesis.dev",
    description="Symmetry-based calibration algorithm for analog and quantum systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/project-genesis-nebula/Shenqu-Algorithm",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Electronics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0", 
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "jupyter>=1.0.0",
            "ipykernel>=6.0",
        ],
    },
)
