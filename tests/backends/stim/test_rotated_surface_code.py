from qec.backends.stim.rotated_surface_code import RotatedSurfaceCode

code = RotatedSurfaceCode(
    distance=3,
    rounds=3,
    depolarizing_error=0.001,
    readout_error=0.001,
    memory_basis="Z",
)

print(code.build_circuit())
print(code.detector_error_model())