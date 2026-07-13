from qec.reference.checkerboard import CheckerboardSurfaceCode


def test_data_idx():

    code = CheckerboardSurfaceCode(distance=3)

    assert code.data_idx(0, 0) == 0
    assert code.data_idx(2, 2) == 8


def test_record_measurement():

    code = CheckerboardSurfaceCode()

    code.record_measurement(
        round_idx=0,
        stabilizer_idx=1,
        record_idx=5,
    )

    measurement = code.get_measurement(
        0,
        1,
    )

    assert measurement.record_idx == 5


def test_reset_measurements():

    code = CheckerboardSurfaceCode()

    code.record_measurement(
        0,
        0,
        0,
    )

    code.reset_measurements()

    assert len(code.measurements) == 0
    assert len(code.data_measurement_records) == 0