# Quantum Error Correction Surface Code Benchmarking Framework

A modular quantum error correction (QEC) simulator for studying surface codes through interchangeable simulation backends and decoding algorithms.

The project provides tools for generating surface-code circuits, constructing detector error models (DEMs), performing syndrome decoding, and evaluating logical failure rates through Monte Carlo simulation.

The simulator is designed as a research framework that separates circuit generation, decoding, and analysis, enabling benchmarking between different surface-code implementations and decoder algorithms.

---

## Features

- Configurable odd code distances (`d = 3, 5, 7, ...`)
- Multi-round syndrome extraction
- Stim-generated **rotated** and **unrotated** surface-code circuits
- Detector Error Model (DEM) generation
- Minimum Weight Perfect Matching (MWPM) decoding
- PyMatching implementation for Stim
- Reference NetworkX implementation for Qiskit
- Depolarising and readout noise models
- X- and Z-memory experiments
- Logical failure-rate simulations
- Lattice comparison experiments
- Modular backend and decoder architecture
- Comprehensive unit test suite

---

## Repository Structure

```text
src/qec/
├── backends/
│   ├── base.py
│   ├── qiskit/
│   │   ├── backend.py
│   │   ├── circuit.py
│   │   ├── engine.py
│   │   └── noise.py
│   └── stim/
│       ├── backend.py
│       ├── base.py
│       ├── rotated.py
│       └── unrotated.py
│
├── decoders/
│   ├── base.py
│   ├── mwpm/
│       ├── pymatching.py
│       └── networkx.py
│   └── syndrome.py
│
├── geometry.py
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

The primary backend uses Stim's built-in surface-code circuit generators and supports both:

- Rotated surface code
- Unrotated surface code

Features include:

- Stim circuit generation
- Detector Error Model (DEM) construction
- PyMatching MWPM decoding
- Fast Monte Carlo logical-memory simulations

This backend is intended for logical error-rate estimation, decoder benchmarking, and threshold studies.

---

### Qiskit Backend

The Qiskit backend provides a reference implementation using explicit circuit construction and Aer simulation.

It includes:

- Explicit syndrome-extraction circuits
- Configurable depolarising noise
- Reference NetworkX MWPM decoder

Although significantly slower than the Stim backend, it serves as an educational implementation and reference for comparison.

---

## Experiments

Current experiments include:

- Logical failure-rate scaling
- Rotated vs. unrotated lattice comparison

Additional experiments can be added by combining different backends and decoders.

---

## Next Milestone

- Union-Find decoder
- Decoder benchmarking (MWPM vs. Union-Find)

---

## Roadmap

- Implement Union-Find decoder
- Decoder benchmarking
- Threshold estimation
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
