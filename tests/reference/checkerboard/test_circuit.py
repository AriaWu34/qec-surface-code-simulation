import stim

from qec.reference.checkerboard import CheckerboardSurfaceCode


def test_prepare_z_state():

    code = CheckerboardSurfaceCode(
        memory_basis="Z",
    )

    circuit = stim.Circuit()

    code.prepare_logical_state(circuit)

    assert len(str(circuit)) == 0


def test_prepare_x_state():

    code = CheckerboardSurfaceCode(
        memory_basis="X",
    )

    circuit = stim.Circuit()

    code.prepare_logical_state(circuit)

    assert "H" in str(circuit)


def test_build_circuit_contains_detectors():

    code = CheckerboardSurfaceCode(
        rounds=2,
    )

    circuit = code.build_circuit()

    text = str(circuit)

    assert "DETECTOR" in text
    assert "OBSERVABLE_INCLUDE" in text