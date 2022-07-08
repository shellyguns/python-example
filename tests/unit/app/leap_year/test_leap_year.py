import pytest
from app.leap_year.leap_year import leap_year


@pytest.mark.parametrize(
    "year, is_leap", [(1999, "No"),
                      (2000, "Yes"),
                      (2001, "No")]
)
def test_leap_year(year: int, is_leap: str):
    assert is_leap == leap_year(year)


def test_leap_year_exception():
    with pytest.raises(TypeError):
        leap_year(2000.2)
    with pytest.raises(TypeError):
        leap_year("2k12")

