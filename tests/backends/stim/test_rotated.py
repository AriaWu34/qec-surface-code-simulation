from qec.backends.stim.rotated import (
    RotatedSurfaceCode,
)


def test_generated_circuit_builds():
    code = RotatedSurfaceCode(
        distance=3,
        rounds=3,
    )

    circuit = code.build_circuit()

    assert circuit.num_qubits > 0


def test_detector_error_model_builds():
    code = RotatedSurfaceCode(
        distance=3,
        rounds=3,
    )

    dem = code.detector_error_model()

    assert dem.num_detectors > 0


def test_sampler_runs():
    code = RotatedSurfaceCode(
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