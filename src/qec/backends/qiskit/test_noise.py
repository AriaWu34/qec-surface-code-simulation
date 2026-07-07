from qec.backends.qiskit.noise import depol_noise_model


def test_noise_model_creation():

    noise = depol_noise_model()

    assert noise is not None