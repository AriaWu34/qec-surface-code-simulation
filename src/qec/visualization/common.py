"""
Shared plotting utilities.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def save_figure(
    save_path: str | Path | None = None,
):
    """
    Save the current matplotlib figure.
    """

    if save_path is None:
        return

    path = Path(save_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight",
    )

    print(f"Saved figure to {path}")