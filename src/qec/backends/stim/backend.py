"""
High-level interface for the Stim backend.

This module provides the public API for running
surface-code simulations using Stim for circuit
generation and detector sampling together with
PyMatching for Minimum Weight Perfect Matching
(MWPM) decoding.
"""

from qec.backends.base import Backend
from qec.backends.stim.surface_code import StimSurfaceCode
from qec.decoders import MWPMDecoder


class StimBackend(Backend):
    """
    High-level interface for Stim-based
    surface-code simulations.
    """

    @property
    def name(self) -> str:
        return "stim"

    def logical_failure_rate(
        self,
        distance: int = 3,
        rounds: int = 5,
        shots: int = 1000,
        depolarizing_error: float = 0.01,
        readout_error: float = 0.01,
        memory_basis: str = "Z",
    ) -> float:

        code = StimSurfaceCode(
            distance=distance,
            rounds=rounds,
            depolarizing_error=depolarizing_error,
            readout_error=readout_error,
            memory_basis=memory_basis,
        )

        decoder = MWPMDecoder(
            backend="pymatching",
            dem=code.detector_error_model(),
        )

        dets, obs = code.sample_detectors_and_observables(
            shots=shots,
        )

        failures = 0

        for det, actual in zip(dets, obs):

            predicted = decoder.decode_detection_events(det)

            if not (predicted == actual).all():
                failures += 1

        return failures / shots