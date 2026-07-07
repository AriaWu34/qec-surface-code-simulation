from qec.backends.qiskit import QiskitBackend


def test_backend_name():
    backend = QiskitBackend()
    assert backend.name == "qiskit"