import pytest
from app.print_even_nums.print_even_nums import print_even_nums


@pytest.mark.parametrize(
    "num1, num2, even_between", [(1, 5, [2, 4]),
                                 (-3, 6, [-2, 2, 4])]
)
def test_print_even_nums(num1: int, num2: int, even_between: list):
    assert even_between == print_even_nums(num1, num2)


@pytest.mark.parametrize(
    "expected_exception, lesser_num, bigger_num", [(TypeError, 2.2, 6),
                                                   (TypeError, -3, "two"),
                                                   (ValueError, 4, -1)]
)
def test_print_even_nums_exception(expected_exception, lesser_num, bigger_num):
    with pytest.raises(expected_exception):
        print_even_nums(lesser_num, bigger_num)
