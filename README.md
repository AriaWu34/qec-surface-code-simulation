# Quantum Error Correction Surface Code Simulator

A modular quantum error correction (QEC) simulator for studying surface codes through interchangeable simulation backends. The project provides tools for constructing surface-code circuits, generating detector error models (DEMs), performing Minimum Weight Perfect Matching (MWPM) decoding, and evaluating logical failure rates through Monte Carlo simulation.

The simulator is designed as a research platform that separates backend implementations from decoding and analysis, enabling benchmarking between educational, research, and high-performance surface-code simulators.

---

## Features

- Configurable odd code distances (`d = 3, 5, 7, ...`)
- Multi-round syndrome extraction
- Stim-generated rotated surface-code circuits
- Detector Error Model (DEM) generation
- PyMatching Minimum Weight Perfect Matching (MWPM) decoder
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
│   │   ├── engine.py
│   │   ├── circuit.py
│   │   └── noise.py
│   ├── stim/
│   │   ├── backend.py
│   │   └── rotated_surface_code.py
│   └── planar/
│       ├── backend.py
│       └── unrotated_surface_code.py
├── decoders/
│   ├── base.py
│   ├── mwpm.py
│   ├── networkx.py
│   └── syndrome.py
├── simulation.py
└── visualization.py

experiments/
results/
tests/
notebooks/
```

---

## Simulation Backends

### Stim Backend

The primary simulation backend is built on Stim's canonical rotated surface-code generator and provides:

- Stim circuit generation
- Detector Error Model (DEM) construction
- PyMatching MWPM decoding
- Fast Monte Carlo logical-memory simulations

This backend is intended for performance benchmarking, logical error-rate estimation, and future threshold studies.

---

### Qiskit Backend

The Qiskit backend provides a reference implementation using explicit circuit construction and Aer simulation.

It includes:

- Explicit syndrome-extraction circuits
- Configurable depolarising noise
- Reference NetworkX MWPM decoder

Although significantly slower than the Stim backend, it serves as an educational implementation and regression-testing reference.

---

### Planar Backend *(In Development)*

The next development milestone is a first-principles implementation of the unrotated planar surface code.

Planned features include:

- Canonical planar lattice geometry
- Rough and smooth boundaries
- Boundary stabilizers
- Geometry-derived logical operators
- Benchmarking against the Stim backend

---

## Example Experiment

Run the logical-memory experiment:

```bash
python experiments/logical_failure_stim.py
```

The experiment estimates logical failure rates for X- and Z-memory experiments across multiple code distances and generates logical-error-rate and distance-scaling plots.

---

## Current Status

### Implemented

- Stim backend using Stim's generated rotated surface-code circuits
- Qiskit reference backend
- Backend abstraction layer
- Detector Error Model (DEM) generation
- PyMatching decoder
- Reference NetworkX decoder
- Logical-memory Monte Carlo simulations
- Automated unit test suite

### In Progress

- Unrotated planar surface-code backend
- Physically accurate planar geometry
- Boundary stabilizers
- Threshold analysis

---

## Roadmap

- Complete planar surface-code backend
- Threshold estimation
- Decoder benchmarking (e.g. Union-Find)
- Additional noise models
- GitHub Actions CI
- Expanded documentation and tutorials

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
