from qec.reference.checkerboard import CheckerboardSurfaceCode


def test_logical_x_chain():

    code = CheckerboardSurfaceCode(
        distance=3,
    )

    chain = code.logical_x_chain()

    assert len(chain) == 3


def test_logical_z_chain():

    code = CheckerboardSurfaceCode(
        distance=3,
    )

    chain = code.logical_z_chain()

    assert len(chain) == 3