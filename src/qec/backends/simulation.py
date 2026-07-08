"""
Simulation utilities for Stim-based surface-code experiments.

This module provides backwards-compatible wrappers around
the Stim backend. New code should instantiate `StimBackend`
directly.
"""

from qec.backends.stim import StimBackend


def logical_failure_rate_stim(
    distance: int = 3,
    rounds: int = 5,
    shots: int = 1000,
    depolarizing_error: float = 0.01,
    readout_error: float = 0.01,
    memory_basis: str = "Z",
) -> float:
    """
    Estimate the logical failure rate using the Stim backend.

    Notes
    -----
    This function is retained for backwards compatibility.
    New code should use `StimBackend.logical_failure_rate()`.
    """

    return StimBackend().logical_failure_rate(
        distance=distance,
        rounds=rounds,
        shots=shots,
        depolarizing_error=depolarizing_error,
        readout_error=readout_error,
        memory_basis=memory_basis,
    )