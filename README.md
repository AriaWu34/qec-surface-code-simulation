# Quantum Error Correction Surface Code Simulator

A modular quantum error correction (QEC) simulator for studying surface codes through multiple simulation backends. The project provides tools for constructing surface-code circuits, generating detector error models (DEMs), performing Minimum Weight Perfect Matching (MWPM) decoding, and evaluating logical failure rates through Monte Carlo simulation.

The simulator is designed as a research platform with interchangeable simulation backends, enabling comparison between educational Qiskit implementations, high-performance Stim simulations, and future physically accurate planar surface-code implementations.

---

## Features

- Configurable odd code distances (`d = 3, 5, 7, ...`)
- Multi-round syndrome extraction
- Stim-based detector error model generation
- PyMatching MWPM decoding
- Reference NetworkX decoder
- Depolarising and readout noise models
- X- and Z-memory experiments
- Logical failure-rate simulations
- Modular backend architecture
- Comprehensive unit test suite

---

## Repository Structure

```text
src/qec/
├── backends/
│   ├── base.py
│   ├── geometry.py
│   ├── qiskit/
│   │   ├── backend.py
│   │   ├── circuit.py
│   │   ├── engine.py
│   │   ├── noise.py
│   │   └── syndrome.py
│   ├── stim/
│   │   ├── backend.py
│   │   ├── simulation.py
│   │   └── surface_code.py
│   └── planar/
├── decoders/
│   ├── mwpm.py
│   └── networkx.py
└── visualization.py

experiments/
results/
tests/
notebooks/
```

---

## Backends

### Stim Backend

The Stim backend provides a high-performance simulation pipeline based on:

- Stim circuit generation
- Detector Error Model (DEM) construction
- PyMatching MWPM decoding
- Monte Carlo logical-memory simulations

This backend is intended for large-scale simulation and threshold experiments.

### Qiskit Backend

The Qiskit backend provides an educational reference implementation based on:

- Explicit syndrome-extraction circuits
- Aer simulation
- Reference NetworkX MWPM decoder

Although slower than the Stim implementation, it provides a transparent implementation useful for learning and algorithmic comparison.

### Planar Backend (In Development)

The next major milestone is implementing a physically accurate unrotated planar surface-code backend with:

- Rough and smooth boundaries
- Boundary stabilizers
- Geometry-derived logical operators
- Canonical planar lattice construction

---

## Example Experiment

Run the Stim logical-memory experiment:

```bash
python experiments/logical_failure_stim.py
```

The experiment estimates logical failure rates for X- and Z-memory experiments over multiple code distances.

---

## Current Status

Implemented:

- Qiskit backend
- Stim backend
- Backend abstraction layer
- PyMatching decoder
- NetworkX reference decoder
- Detector Error Model generation
- Monte Carlo logical-memory simulations
- Comprehensive automated tests

Currently under development:

- Canonical planar surface-code geometry
- Boundary stabilizers
- Threshold analysis

---

## Future Work

- Complete planar surface-code backend
- Threshold estimation
- Decoder benchmarking
- Additional noise models
- GitHub Actions CI/CD
- Documentation improvements

---

## Testing

Run the complete test suite:

```bash
pytest
```

---

## Requirements

- Python 3.12+
- Stim
- PyMatching
- NumPy
- NetworkX
- Matplotlib
- Pytest
- Qiskit

Install dependencies:

```bash
pip install qiskit stim pymatching numpy networkx matplotlib pytest
```
