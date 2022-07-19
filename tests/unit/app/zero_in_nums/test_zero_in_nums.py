import pytest
from app.cycles.zero_in_nums.zero_in_nums import zero_in_nums


@pytest.mark.parametrize(
    "input_nums, zero_presence", [([1, 2, 3], "No"),
                                  ([-1, -2, -3], "No"),
                                  ([-2, 0, 2], "Yes"),
                                  ([1], "No")]
)
def test_zero_in_nums( input_nums: list, zero_presence: str):
    assert zero_presence == zero_in_nums(input_nums)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [2.2, 3, 4]),
                                           (TypeError, ["two", 3]),
                                           (TypeError, "")]
)
def test_zero_in_nums_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        zero_in_nums(improper_input)
