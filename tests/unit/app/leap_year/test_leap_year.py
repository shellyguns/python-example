import pytest
from app.leap_year.leap_year import leap_year


@pytest.mark.parametrize(
    "year, is_leap", [(1999, "No"),
                      (2000, "Yes"),
                      (2001, "No")]
)
def test_leap_year(year: int, is_leap: str):
    assert is_leap == leap_year(year)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, 2000.2),
                                           (TypeError, "2k12")]
)
def test_leap_year_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        leap_year(improper_input)


