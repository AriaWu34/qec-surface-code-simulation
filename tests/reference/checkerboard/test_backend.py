from qec.reference.checkerboard import CheckerboardBackend


def test_backend_name():
    backend = CheckerboardBackend()
    assert backend.name == "reference"


def test_logical_failure_rate_runs():
    backend = CheckerboardBackend()

    rate = backend.logical_failure_rate(
        distance=3,
        rounds=2,
        shots=10,
    )

    assert 0.0 <= rate <= 1.0