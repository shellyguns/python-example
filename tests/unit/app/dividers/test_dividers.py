import pytest
from app.dividers.dividers import dividers


@pytest.mark.parametrize(
    "number, num_dividers", [(1, [1]),
                             (3, [1, 3]),
                             (-4, [-4, -2, -1, 1, 2, 4])]

)
def test_dividers(number: int, num_dividers: list):
    assert num_dividers == dividers(number)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, 2.2),
                                           (TypeError, "two")]
)
def test_dividers_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        dividers(improper_input)
