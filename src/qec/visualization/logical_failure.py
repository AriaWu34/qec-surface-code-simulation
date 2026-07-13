"""
Logical failure-rate visualisations.
"""

import matplotlib.pyplot as plt

from .common import save_figure


def plot_logical_failure_rate(
    physical_error_rates,
    logical_error_rates,
    distance,
    save_path=None,
):
    plt.figure(figsize=(7.5, 5.2))

    plt.plot(
        physical_error_rates,
        logical_error_rates,
        "o-",
        linewidth=2,
        label=f"d={distance}",
    )

    plt.xlabel(
        "Physical depolarizing probability",
    )

    plt.ylabel(
        "Logical failure rate",
    )

    plt.title(
        f"Logical Failure Rate (d={distance})",
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    save_figure(save_path)

    plt.show()


def plot_distance_scaling(
    physical_error_rates,
    logical_error_rates_by_distance,
    save_path=None,
):
    plt.figure(figsize=(7.5, 5.2))

    for distance, rates in (
        logical_error_rates_by_distance.items()
    ):

        plt.plot(
            physical_error_rates,
            rates,
            "o-",
            label=f"d={distance}",
        )

    plt.xlabel(
        "Physical depolarizing probability",
    )

    plt.ylabel(
        "Logical failure rate",
    )

    plt.title(
        "Distance Scaling",
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    save_figure(save_path)

    plt.show()