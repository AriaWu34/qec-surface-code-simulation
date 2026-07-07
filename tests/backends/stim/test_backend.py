from qec.backends.stim import StimBackend


def test_backend_name():
    backend = StimBackend()

    assert backend.name == "stim"


def test_backend_logical_failure_rate_runs():
    backend = StimBackend()

    rate = backend.logical_failure_rate(
        distance=3,
        rounds=3,
        shots=10,
    )

    assert 0.0 <= rate <= 1.0