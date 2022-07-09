import pytest
from app.bigger_of_two.bigger_of_two import bigger_of_two


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 2, 2),
        (10, 30, 30),
        (-10, 2, 2),
    ]
)
def test_bigger_of_two(first: int, second: int, answer: int):
    assert answer == bigger_of_two(first, second)


def test_bigger_of_two_exception():
    with pytest.raises(TypeError):
        bigger_of_two(10, 's')
    with pytest.raises(TypeError):
        bigger_of_two('asd', 2)
    with pytest.raises(TypeError):
        bigger_of_two(10.2, 2)
