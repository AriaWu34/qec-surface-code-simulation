"""
Stim unrotated surface-code circuit generator.
"""

from qec.backends.stim.base import (
    StimSurfaceCode,
)


class UnrotatedSurfaceCode(
    StimSurfaceCode,
):
    """
    Stim implementation using the built-in
    unrotated surface-code circuit generator.
    """

    def _task_name(self) -> str:
        if self.memory_basis == "X":
            return "surface_code:unrotated_memory_x"

        return "surface_code:unrotated_memory_z"