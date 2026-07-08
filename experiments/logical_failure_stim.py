"""
Logical failure-rate experiment using the
Stim backend.

Usage:
    python experiments/logical_failure_stim.py
"""

from pathlib import Path

import numpy as np

from qec.backends.stim import StimBackend
from qec.visualization import (
    plot_distance_scaling,
    plot_logical_failure_rate,
)


OUTPUT_DIR = Path(
    "results/logical_failure"
)


def main():
    """
    Run logical memory experiments for
    multiple code distances and physical
    error rates.
    """

    backend = StimBackend()

    # Focus on the low-error regime where
    # threshold behaviour is expected.
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

        print(
            f"\n=== {basis} memory ==="
        )

        results = {}

        basis_output_dir = (
            OUTPUT_DIR / basis
        )

        for distance in distances:

            print(
                f"\nRunning d={distance}"
            )

            rates = []

            rounds = distance

            for p in p_vals:

                rate = (
                    backend.logical_failure_rate(
                        distance=distance,
                        rounds=rounds,
                        shots=shots,
                        depolarizing_error=p,
                        readout_error=p,
                        memory_basis=basis,
                    )
                )

                rates.append(rate)

                print(
                    f"{basis} "
                    f"d={distance} "
                    f"r={rounds} "
                    f"p={p:.4f} "
                    f"logical={rate:.6e}"
                )

            results[distance] = rates

            plot_logical_failure_rate(
                physical_error_rates=p_vals,
                logical_error_rates=rates,
                distance=distance,
                save_path=(
                    basis_output_dir
                    / f"logical_failure_rate_d{distance}.png"
                ),
            )

        plot_distance_scaling(
            physical_error_rates=p_vals,
            logical_error_rates_by_distance=results,
            save_path=(
                basis_output_dir
                / "distance_scaling.png"
            ),
        )


if __name__ == "__main__":
    main()