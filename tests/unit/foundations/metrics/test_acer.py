import numpy as np
import pytest

from gradgpad.foundations.metrics.acer import acer


@pytest.mark.unit
def test_should_throw_an_exception_when_input_is_not_np_array():
    pytest.raises(
        TypeError, lambda: acer([0.0, 0.2, 0.2, 0.5, 0.6], [1, 2, 2, 0, 0], 0.25)
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "scores, labels, expected_acer, th_eer",
    [
        (np.array([0.5, 0.6, 0.2, 0.0, 0.0]), np.array([1, 2, 2, 0, 0]), 0.0, 0.15),
        (np.array([0.1, 0.6, 0.2, 0.0, 0.0]), np.array([1, 2, 2, 0, 0]), 0.5, 0.15),
    ],
)
def test_should_compute_acer_correctly(scores, labels, expected_acer, th_eer):
    acer_value = acer(scores, labels, th_eer)
    assert pytest.approx(expected_acer, 0.1) == acer_value
