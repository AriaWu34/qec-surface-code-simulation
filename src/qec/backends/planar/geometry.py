"""
Geometry definitions for the unrotated planar surface code.

This module defines the stabilizer lattice used by the
Planar backend. The implementation will be extended with
boundary stabilizers and canonical planar geometry.
"""


from dataclasses import dataclass
from qec.backends.geometry import d_idx


def valid_data_coordinate(
    row: int,
    col: int,
    distance: int,
) -> bool:
    """
    Return whether a data-qubit coordinate
    lies inside the code.
    """

    return (
        0 <= row < distance
        and 0 <= col < distance
    )


def stabilizer_data_coordinates(
    row: int,
    col: int,
    distance: int,
) -> tuple[tuple[int, int], ...]:
    """
    Return all data qubits neighbouring an
    ancilla centred at (row+0.5, col+0.5).
    """

    neighbours = []

    candidates = [
        (row, col),
        (row, col + 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]

    for r, c in candidates:

        if valid_data_coordinate(
            r,
            c,
            distance,
        ):
            neighbours.append((r, c))

    return tuple(neighbours)


@dataclass(frozen=True)
class StabilizerGeometry:
    """
    Geometry describing a stabilizer in the
    planar surface-code lattice.
    """

    stabilizer_idx: int

    stabilizer_type: str

    ancilla_position: tuple[float, float]

    data_coordinates: tuple[
        tuple[int, int],
        ...
    ]

    data_qubits: tuple[int, ...]

    boundary: bool = False

    @property
    def weight(self) -> int:
        """
        Number of data qubits acted on by the stabilizer.
        """
        return len(self.data_qubits)
    

def generate_planar_stabilizers(
    distance: int,
) -> list[StabilizerGeometry]:
    """
    Generate the stabilizer geometry for the
    unrotated planar surface code.

    Returns
    -------
    list[StabilizerGeometry]
        Metadata describing every stabilizer,
        including its type, ancilla position,
        neighbouring data qubits, and index.
    """

    stabilizers: list[
        StabilizerGeometry
    ] = []

    idx = 0

    for r in range(distance - 1):

        for c in range(distance - 1):

            coordinates = stabilizer_data_coordinates(
                r,
                c,
                distance,
            )

            stabilizers.append(
                StabilizerGeometry(
                    stabilizer_idx=idx,

                    stabilizer_type=(
                        "X"
                        if (r + c) % 2 == 0
                        else "Z"
                    ),

                    ancilla_position=(
                        r + 0.5,
                        c + 0.5,
                    ),

                    data_coordinates=coordinates,

                    data_qubits=tuple(
                        d_idx(
                            rr,
                            cc,
                            distance,
                        )
                        for rr, cc in coordinates
                    ),

                    boundary=False,
                )
            )

            idx += 1

    return stabilizers