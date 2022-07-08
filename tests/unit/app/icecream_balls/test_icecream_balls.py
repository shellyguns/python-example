import pytest
from app.icecream_balls.icecream_balls import icecream_balls


@pytest.mark.parametrize(
    "quantity, available", [(1, "No"),
                            (3, "Yes"),
                            (4, "No"),
                            (5, "Yes")]
)
def test_icecream_balls(quantity: int, available: str):
    assert available == icecream_balls(quantity)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, 2.2),
                                           (TypeError, "two"),
                                           (ValueError, -1)]
)
def test_icecream_balls_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        icecream_balls(improper_input)
