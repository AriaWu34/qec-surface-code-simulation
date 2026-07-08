"""
Shared geometry and indexing utilities.

This module contains backend-independent helper
functions used throughout the project, including
distance validation, data-qubit indexing, and
decoder geometry utilities.
"""

def d_idx(r: int, c: int, distance: int) -> int:
    """
    Convert a 2D data-qubit coordinate into a linear index.
    """
    return distance * r + c


def code_sizes(distance: int):
    """
    Return the number of data, X-ancilla, and Z-ancilla qubits.
    """
    n_data = distance**2
    n_x = (distance - 1) ** 2
    n_z = (distance - 1) ** 2

    return n_data, n_x, n_z


def ancilla_offsets(distance: int):
    """
    Return the starting indices of X and Z ancillas.
    """
    n_data, n_x, _ = code_sizes(distance)

    x_start = n_data
    z_start = n_data + n_x

    return x_start, z_start


def generate_plaquettes(distance: int):
    """
    Generate all 2×2 plaquettes used by the
    legacy Qiskit circuit construction.

    This helper is retained for compatibility with
    the reference Qiskit backend.
    """
    plaqs = []

    for r in range(distance - 1):
        for c in range(distance - 1):
            plaqs.append(
                [
                    (r, c),
                    (r, c + 1),
                    (r + 1, c),
                    (r + 1, c + 1),
                ]
            )

    return plaqs


def manhattan(p: tuple, q: tuple) -> float:
    """
    Manhattan distance between two coordinates.
    """
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def code_boundaries(distance: int):
    """
    Return decoder boundary coordinates.
    """
    low = -0.5
    high = distance - 0.5

    return {
        "top": low,
        "bottom": high,
        "left": low,
        "right": high,
        "span": float(distance),
    }


def validate_distance(distance: int):
    """
    Validate that the code distance is an
    odd integer greater than or equal to 3.
    """
    if distance < 3 or distance % 2 == 0:
        raise ValueError(
            "Distance must be an odd integer >= 3."
        )