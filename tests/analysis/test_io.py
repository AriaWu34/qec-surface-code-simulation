import pandas as pd

from qec.analysis.io import (
    file_exists,
    load_dataframe,
    save_dataframe,
    save_text,
    should_rerun,
)


def test_save_and_load_dataframe(tmp_path):

    df = pd.DataFrame(
        {
            "a": [1, 2],
            "b": [3, 4],
        }
    )

    path = tmp_path / "data.csv"

    save_dataframe(df, path)

    loaded = load_dataframe(path)

    pd.testing.assert_frame_equal(
        df,
        loaded,
    )


def test_save_text(tmp_path):

    path = tmp_path / "summary.txt"

    save_text(
        "hello world",
        path,
    )

    assert path.read_text() == "hello world"


def test_file_exists_false(tmp_path):

    assert not file_exists(
        tmp_path / "missing.csv"
    )


def test_file_exists_true(tmp_path):

    path = tmp_path / "file.txt"

    path.write_text("abc")

    assert file_exists(path)


def test_should_rerun_missing_file(tmp_path):

    assert should_rerun(
        tmp_path / "missing.csv"
    )


def test_should_rerun_use_cache(tmp_path):

    path = tmp_path / "data.csv"

    path.write_text("x")

    assert not should_rerun(
        path,
        use_cache=True,
    )


def test_should_rerun_ignore_cache(tmp_path):

    path = tmp_path / "data.csv"

    path.write_text("x")

    assert should_rerun(
        path,
        use_cache=False,
    )