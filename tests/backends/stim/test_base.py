from qec.backends.stim.rotated import (
    RotatedSurfaceCode,
)
from qec.backends.stim.unrotated import (
    UnrotatedSurfaceCode,
)


def test_rotated_task_names():
    assert (
        RotatedSurfaceCode(
            memory_basis="Z",
        )._task_name()
        == "surface_code:rotated_memory_z"
    )

    assert (
        RotatedSurfaceCode(
            memory_basis="X",
        )._task_name()
        == "surface_code:rotated_memory_x"
    )


def test_unrotated_task_names():
    assert (
        UnrotatedSurfaceCode(
            memory_basis="Z",
        )._task_name()
        == "surface_code:unrotated_memory_z"
    )

    assert (
        UnrotatedSurfaceCode(
            memory_basis="X",
        )._task_name()
        == "surface_code:unrotated_memory_x"
    )