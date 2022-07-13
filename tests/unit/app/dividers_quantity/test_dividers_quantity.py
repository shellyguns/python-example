import pytest
from app.cycles.dividers_quantity.dividers_quantity import dividers_quantity


@pytest.mark.parametrize(
    "number, dividers_quant", [(1, 1),
                               (3, 2),
                               (-4, 6)]
)
def test_dividers(number: int, dividers_quant: list):
    assert dividers_quant == dividers_quantity(number)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, 2.2),
                                           (TypeError, "two")]
)
def test_dividers_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        dividers_quantity(improper_input)
