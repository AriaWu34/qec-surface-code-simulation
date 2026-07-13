"""
Compare logical memory performance of the Stim and
Reference backends.

Usage:
    python experiments/compare_stim_checkerboard.py
"""

from pathlib import Path

import numpy as np

from qec.reference.checkerboard import CheckerboardBackend
from qec.backends.stim import StimBackend

from qec.visualization import (
    plot_backend_comparison,
)

OUTPUT_DIR = Path(
    "results/reference/compare_stim_checkerboard"
)


def run_backend(
    backend,
    distance,
    basis,
    p_vals,
    shots,
):
    """
    Compute logical failure rates for one backend.
    """

    logical = []

    for p in p_vals:

        logical.append(

            backend.logical_failure_rate(
                distance=distance,
                rounds=distance,
                shots=shots,
                depolarizing_error=p,
                readout_error=p,
                memory_basis=basis,
            )

        )

    return np.asarray(logical)


def main():

    stim = StimBackend(lattice="unrotated")

    reference = CheckerboardBackend()

    p_vals = np.array([
        0.0005,
        0.0010,
        0.0015,
        0.0020,
        0.0025,
        0.0030,
        0.0035,
        0.0040,
        0.0045,
        0.0050,
    ])

    shots = 50_000

    for basis in ("Z", "X"):

        for distance in (3, 5, 7):

            print(
                f"\n{basis} distance={distance}"
            )

            stim_unrotated_rates = run_backend(
                stim,
                distance,
                basis,
                p_vals,
                shots,
            )

            checkerboard_rates = run_backend(
                reference,
                distance,
                basis,
                p_vals,
                shots,
            )

            plot_backend_comparison(
                physical_error_rates=p_vals,
                stim_unrotated_rates=stim_unrotated_rates,
                checkerboard_rates=checkerboard_rates,
                distance=distance,
                basis=basis,
                save_path=(
                    OUTPUT_DIR
                    / basis
                    / f"d{distance}.png"
                ),
            )


if __name__ == "__main__":
    main()