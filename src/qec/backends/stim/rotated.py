"""
Stim rotated surface-code circuit generator.
"""

from qec.backends.stim.base import (
    StimSurfaceCode,
)


class RotatedSurfaceCode(
    StimSurfaceCode,
):
    """
    Stim implementation using the built-in
    rotated surface-code circuit generator.
    """

    def _task_name(self) -> str:
        if self.memory_basis == "X":
            return "surface_code:rotated_memory_x"

        return "surface_code:rotated_memory_z"