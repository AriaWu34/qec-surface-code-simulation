"""
Stim backend based on Stim's built-in rotated
surface-code circuit generator.
"""

import stim

from qec.backends.geometry import validate_distance


class RotatedSurfaceCode:
    """
    Stim implementation using Stim's built-in
    rotated surface-code circuit generator.
    """

    def __init__(
        self,
        distance: int = 3,
        rounds: int = 1,
        depolarizing_error: float = 0.0,
        readout_error: float = 0.0,
        memory_basis: str = "Z",
    ):
        validate_distance(distance)

        if rounds < 1:
            raise ValueError(
                "Rounds must be >= 1."
            )

        if memory_basis not in {"X", "Z"}:
            raise ValueError(
                "memory_basis must be 'X' or 'Z'."
            )

        for p in (
            depolarizing_error,
            readout_error,
        ):
            if not 0.0 <= p <= 1.0:
                raise ValueError(
                    "Error probabilities must be in [0, 1]."
                )

        self.distance = distance
        self.rounds = rounds
        self.depolarizing_error = depolarizing_error
        self.readout_error = readout_error
        self.memory_basis = memory_basis

    def _task_name(self) -> str:
        """
        Return the Stim generated-circuit task.
        """

        if self.memory_basis == "X":
            return "surface_code:rotated_memory_x"

        return "surface_code:rotated_memory_z"

    def build_circuit(self) -> stim.Circuit:
        """
        Build a rotated surface-code memory circuit.
        """

        return stim.Circuit.generated(
            self._task_name(),
            distance=self.distance,
            rounds=self.rounds,
            after_clifford_depolarization=self.depolarizing_error,
            before_round_data_depolarization=0.0,
            before_measure_flip_probability=self.readout_error,
            after_reset_flip_probability=0.0,
        )

    def detector_error_model(
        self,
    ) -> stim.DetectorErrorModel:
        """
        Generate the detector error model.
        """

        return (
            self.build_circuit()
            .detector_error_model()
        )

    def compile_detector_sampler(
        self,
    ) -> stim.CompiledDetectorSampler:
        """
        Compile a detector sampler.
        """

        return (
            self.build_circuit()
            .compile_detector_sampler()
        )

    def sample_detectors(
        self,
        shots: int,
    ):
        """
        Sample detector outcomes.
        """

        return (
            self.compile_detector_sampler()
            .sample(shots)
        )

    def sample_detectors_and_observables(
        self,
        shots: int,
    ):
        """
        Sample detector outcomes together with
        logical observables.
        """

        return (
            self.compile_detector_sampler()
            .sample(
                shots,
                separate_observables=True,
            )
        )