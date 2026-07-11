from qec.geometry import (
    generate_qiskit_stabilizers,
    stabilizer_data_coordinates,
)  


def test_stabilizer_weight():

    layout = generate_qiskit_stabilizers(5)

    for stabilizer in layout:

        assert stabilizer.weight == len(
            stabilizer.data_qubits
        )


def test_planar_stabilizer_weight():

    layout = generate_qiskit_stabilizers(5)

    assert all(
        stabilizer.weight == 4
        for stabilizer in layout
    )


def test_weight_matches_coordinates():

    layout = generate_qiskit_stabilizers(7)

    for stabilizer in layout:

        assert (
            stabilizer.weight
            == len(stabilizer.data_coordinates)
        )


def test_planar_layout_d3():
    layout = generate_qiskit_stabilizers(3)

    types = [
        s.stabilizer_type
        for s in layout
    ]

    assert types == [
        "X",
        "Z",
        "Z",
        "X",
    ]


def test_stabilizer_has_data_qubits():

    layout = generate_qiskit_stabilizers(3)

    assert layout[0].data_qubits == (
        0,
        1,
        3,
        4,
    )


def test_stabilizer_has_data_coordinates():

    layout = generate_qiskit_stabilizers(3)

    assert (
        layout[0].data_coordinates
        ==
        (
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
        )
    )


def test_stabilizer_has_ancilla_position():

    layout = generate_qiskit_stabilizers(3)

    assert (
        layout[0].ancilla_position
        ==
        (0.5, 0.5)
    )


def test_stabilizer_not_boundary():

    layout = generate_qiskit_stabilizers(3)

    assert layout[0].boundary is False


def test_stabilizer_geometry_consistency():

    layout = generate_qiskit_stabilizers(5)

    for stabilizer in layout:

        assert len(stabilizer.data_qubits) == 4
        assert len(stabilizer.data_coordinates) == 4

        assert (
            len(set(stabilizer.data_qubits))
            == 4
        )

        assert (
            len(set(stabilizer.data_coordinates))
            == 4
        )


def test_neighbouring_data_coordinates_d3():

    coords = stabilizer_data_coordinates(
        0,
        0,
        3,
    )

    assert coords == (
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    )


def test_all_neighbours_are_valid():

    layout = generate_qiskit_stabilizers(7)

    for stabilizer in layout:

        for r, c in stabilizer.data_coordinates:

            assert 0 <= r < 7
            assert 0 <= c < 7