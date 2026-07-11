from qec.backends.stim.unrotated import (
    UnrotatedSurfaceCode,
)


def test_generated_circuit_builds():
    code = UnrotatedSurfaceCode(
        distance=3,
        rounds=3,
    )

    circuit = code.build_circuit()

    assert circuit.num_qubits > 0


def test_detector_error_model_builds():
    code = UnrotatedSurfaceCode(
        distance=3,
        rounds=3,
    )

    dem = code.detector_error_model()

    assert dem.num_detectors > 0


def test_sampler_runs():
    code = UnrotatedSurfaceCode(
        distance=3,
        rounds=3,
    )

    dets, obs = (
        code.sample_detectors_and_observables(
            shots=5,
        )
    )

    assert len(dets) == 5
    assert len(obs) == 5