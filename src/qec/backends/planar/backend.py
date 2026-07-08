"""
High-level interface for the planar surface-code backend.

This module provides the public API for constructing
and simulating the unrotated planar surface code.
"""

from qec.backends.base import Backend

from .unrotated_surface_code import PlanarSurfaceCode


class PlanarBackend(Backend):
    """
    High-level interface for the planar
    surface-code backend.
    """

    @property
    def name(self) -> str:
        return "planar"

    def logical_failure_rate(
        self,
        distance: int = 3,
        rounds: int = 3,
        shots: int = 1000,
        depolarizing_error: float = 0.01,
        readout_error: float = 0.01,
        memory_basis: str = "Z",
    ) -> float:
        """
        Estimate the logical failure rate for
        the planar surface code.

        Notes
        -----
        This backend is currently under
        development.
        """

        code = PlanarSurfaceCode(
            distance=distance,
            rounds=rounds,
            depolarizing_error=depolarizing_error,
            readout_error=readout_error,
            memory_basis=memory_basis,
        )

        return code.logical_failure_rate(
            shots=shots,
        )