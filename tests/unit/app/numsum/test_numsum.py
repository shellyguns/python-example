import pytest
from app.cycles.numsum.numsum import numsum


@pytest.mark.parametrize(
    "input_nums, expected_sum", [([1, 2, 3], 6),
                                 ([-1, -2, -3], -6),
                                 ([-2, 0, 2], 0),
                                 ([1], 1)]
)
def test_numsum(input_nums: list, expected_sum: int):
    assert expected_sum == numsum(input_nums)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [2.2, 3, 4]),
                                           (TypeError, ["two", 3]),
                                           (TypeError, "")]
)
def test_numsum_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        numsum(improper_input)
