import numpy as np

from qec.analysis.threshold import (
    ThresholdEstimate,
    estimate_crossing,
    estimate_threshold,
    summarize_threshold,
)


def test_threshold_estimate_to_dataframe():

    estimate = ThresholdEstimate(
        threshold=0.009,
        pairwise_crossings={
            (3, 5): 0.0085,
            (5, 7): 0.0095,
        },
        mean=0.009,
        std=0.0005,
    )

    df = estimate.to_dataframe()

    assert len(df) == 1

    assert df.loc[0, "threshold"] == 0.009
    assert df.loc[0, "mean"] == 0.009
    assert df.loc[0, "std"] == 0.0005
    assert df.loc[0, "3-5"] == 0.0085
    assert df.loc[0, "5-7"] == 0.0095


def test_estimate_crossing():

    p = np.array([
        0.005,
        0.007,
        0.009,
    ])

    curve1 = np.array([
        0.010,
        0.020,
        0.040,
    ])

    curve2 = np.array([
        0.040,
        0.020,
        0.010,
    ])

    crossing = estimate_crossing(
        p,
        curve1,
        curve2,
    )

    assert crossing is not None

    assert 0.006 <= crossing <= 0.008


def test_estimate_crossing_none():

    p = np.array([
        0.005,
        0.007,
        0.009,
    ])

    curve1 = np.array([
        0.01,
        0.02,
        0.03,
    ])

    curve2 = np.array([
        0.04,
        0.05,
        0.06,
    ])

    crossing = estimate_crossing(
        p,
        curve1,
        curve2,
    )

    assert crossing is None


def test_estimate_threshold():

    p = np.array([
        0.005,
        0.007,
        0.009,
    ])

    logical = {
        3: np.array([
            0.010,
            0.020,
            0.040,
        ]),
        5: np.array([
            0.040,
            0.020,
            0.010,
        ]),
        7: np.array([
            0.050,
            0.030,
            0.005,
        ]),
    }

    estimate = estimate_threshold(
        p,
        logical,
    )

    assert isinstance(
        estimate,
        ThresholdEstimate,
    )

    assert estimate.threshold is not None
    assert estimate.mean is not None
    assert estimate.std is not None

    assert (3, 5) in estimate.pairwise_crossings
    assert (5, 7) in estimate.pairwise_crossings


def test_summarize_threshold():

    estimate = ThresholdEstimate(
        threshold=0.009,
        pairwise_crossings={
            (3, 5): 0.0088,
            (5, 7): 0.0092,
        },
        mean=0.009,
        std=0.0002,
    )

    summary = summarize_threshold(
        estimate
    )

    assert "Threshold estimation" in summary
    assert "Estimated threshold" in summary
    assert "Pairwise crossings" in summary
    assert "d=3 ↔ d=5" in summary


def test_summarize_threshold_none():

    estimate = ThresholdEstimate(
        threshold=None,
        pairwise_crossings={},
        mean=None,
        std=None,
    )

    summary = summarize_threshold(
        estimate
    )

    assert "No threshold detected." in summary