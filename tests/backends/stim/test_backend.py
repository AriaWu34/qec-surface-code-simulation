import pytest

from qec.backends.stim import StimBackend


@pytest.mark.parametrize(
    "lattice",
    [
        "rotated",
        "unrotated",
    ],
)
def test_backend_name(lattice):
    backend = StimBackend(
        lattice=lattice,
    )

    assert backend.name == f"stim-{lattice}"


@pytest.mark.parametrize(
    "lattice",
    [
        "rotated",
        "unrotated",
    ],
)
def test_logical_failure_rate_runs(lattice):
    backend = StimBackend(
        lattice=lattice,
    )

    rate = backend.logical_failure_rate(
        distance=3,
        rounds=3,
        shots=10,
    )

    assert 0.0 <= rate <= 1.0


def test_invalid_lattice():
    with pytest.raises(ValueError):
        StimBackend(
            lattice="foobar",
        )