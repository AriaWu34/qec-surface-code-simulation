# Quantum Error Correction Surface Code Benchmarking Framework

A modular quantum error correction (QEC) framework for studying surface codes through interchangeable simulation backends and decoding algorithms.

The framework provides tools for constructing surface-code circuits, generating detector error models (DEMs), performing syndrome decoding, and evaluating logical failure rates through Monte Carlo simulation.

Designed as a research-oriented software framework, it separates circuit generation, decoding, experimentation, and visualization, enabling reproducible benchmarking of different surface-code implementations.

---

## Features

- Configurable odd code distances (`d = 3, 5, 7, ...`)
- Multi-round syndrome extraction
- Stim-generated **rotated** and **unrotated** surface-code circuits
- Explicit checkerboard surface-code reference implementation
- Detector Error Model (DEM) generation
- Minimum Weight Perfect Matching (MWPM) decoding
- PyMatching decoder for Stim
- Reference NetworkX decoder
- Depolarising and readout noise models
- X- and Z-memory experiments
- Logical failure-rate simulations
- Rotated vs. unrotated lattice comparison
- Reference implementation validation
- Modular backend and decoder architecture
- Comprehensive unit test suite

---

## Repository Structure

```text
src/qec/
├── backends/
│   ├── base.py
│   └── stim/
│       ├── backend.py
│       ├── base.py
│       ├── rotated.py
│       └── unrotated.py
│
├── decoders/
│   ├── base.py
│   ├── mwpm/
│   │   ├── pymatching.py
│   │   └── networkx.py
│   └── syndrome.py
│
├── reference/
│   ├── checkerboard/
│   │   ├── backend.py
│   │   ├── checkerboard_surface_code.py
│   │   ├── circuit.py
│   │   ├── detectors.py
│   │   └── helpers.py
│   │
│   └── qiskit/
│       ├── backend.py
│       ├── circuit.py
│       ├── engine.py
│       └── noise.py
│
├── geometry.py
├── simulation.py
├── analysis/
└── visualization/

experiments/
results/
tests/
notebooks/
```

---

## Production Backend

### Stim Backend

The production backend is built on Stim's canonical surface-code circuit generators and supports both:

- Rotated surface code
- Unrotated surface code

Features include:

- Canonical circuit generation
- Detector Error Model (DEM) construction
- PyMatching MWPM decoding
- Fast Monte Carlo logical-memory simulations

This backend is used for all benchmarking experiments, including logical failure-rate estimation and future threshold studies.

---

## Reference Implementations

### Checkerboard Surface Code

The repository includes an explicit first-principles implementation of a checkerboard surface-code memory experiment.

Rather than relying on Stim's built-in generators, it constructs:

- explicit stabilizer circuits,
- repeated syndrome-extraction rounds,
- detector events,
- logical observables,
- Stim-compatible detector error models.

This implementation serves as an educational reference and validates the framework against Stim's canonical implementation.

### Qiskit Backend

The Qiskit reference backend demonstrates explicit circuit construction using Qiskit and Aer.

It includes:

- explicit syndrome-extraction circuits,
- configurable depolarising and readout noise,
- Aer simulation,
- reference NetworkX MWPM decoding.

Although considerably slower than the Stim backend and based on a simplified circuit model, it illustrates how surface-code circuits can be implemented and simulated using Qiskit.

---

## Experiments

Current experiments include:

- Logical failure-rate scaling
- Rotated vs. unrotated lattice comparison
- Stim vs. checkerboard reference comparison

The experiment framework is designed to support additional benchmarking studies with different decoders, noise models, and analysis methods.

---

## Next Milestone

- Threshold estimation
- Runtime benchmarking
- GitHub Actions continuous integration
- Expanded documentation

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
