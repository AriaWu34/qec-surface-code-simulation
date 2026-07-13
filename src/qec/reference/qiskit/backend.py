"""
High-level interface for the educational Qiskit backend.

This module provides the public API for running logical
failure-rate simulations using the original Qiskit-based
surface-code implementation.
"""

from qec.backends.base import Backend
from .engine import (
    logical_failure_rates_single,
    logical_failure_rates_spacetime,
)


class QiskitBackend(Backend):
    """
    High-level interface for the educational
    Qiskit surface-code implementation.
    """

    @property
    def name(self):
        return "qiskit"

    def logical_failure_rate(self, *args, **kwargs):
        return logical_failure_rates_single(
            *args,
            **kwargs,
        )

    def logical_failure_rate_spacetime(
        self,
        *args,
        **kwargs,
    ):
        return logical_failure_rates_spacetime(
            *args,
            **kwargs,
        )