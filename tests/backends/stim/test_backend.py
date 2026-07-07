from qec.backends.stim import StimBackend


def test_backend_name():
    backend = StimBackend()
    assert backend.name == "stim"