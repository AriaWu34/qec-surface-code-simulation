"""
Compare rotated and unrotated Stim surface codes.

Usage:
    python experiments/compare_lattices.py
"""

from pathlib import Path

import numpy as np

from qec.backends.stim import StimBackend
from qec.visualization import plot_comparison


OUTPUT_DIR = Path(
    "results/compare_lattices"
)


def main():
    """
    Compare logical failure rates for
    rotated and unrotated surface codes.
    """

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

    distances = [
        3,
        5,
        7,
    ]

    shots = 50_000

    for basis in ("Z", "X"):

        basis_output_dir = (
            OUTPUT_DIR / basis
        )

        for distance in distances:

            print(
                f"\n=== {basis} memory, d={distance} ==="
            )

            comparison = {}

            for lattice in (
                "rotated",
                "unrotated",
            ):

                backend = StimBackend(
                    lattice=lattice,
                )

                rounds = distance

                rates = []

                print(
                    f"\nRunning {lattice}"
                )

                for p in p_vals:

                    rate = backend.logical_failure_rate(
                        distance=distance,
                        rounds=rounds,
                        shots=shots,
                        depolarizing_error=p,
                        readout_error=p,
                        memory_basis=basis,
                    )

                    rates.append(rate)

                    print(
                        f"{lattice:<10}"
                        f"p={p:.4f} "
                        f"logical={rate:.6e}"
                    )

                comparison[lattice] = rates

            plot_comparison(
                x=p_vals,
                y=comparison,
                xlabel="Physical error rate",
                ylabel="Logical failure rate",
                title=f"{basis} memory (d={distance})",
                save_path=(
                    basis_output_dir
                    / f"compare_lattices_d{distance}.png"
                ),
            )


if __name__ == "__main__":
    main()