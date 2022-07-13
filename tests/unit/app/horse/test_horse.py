import pytest
from app.conditional_operator.horse.horse import horse


@pytest.mark.parametrize ("horse_coordinate_a, horse_coordinate_n, target_coordinate_a, target_coordinate_n, beatable",
                         [("a", 1, "b", 3, "Yes"),
                          ("c", 2, "a", 1, "Yes"),
                          ("b", 2, "c", 3, "No")]
                         )
def test_horse(horse_coordinate_a: str, horse_coordinate_n: int, target_coordinate_a: str, target_coordinate_n: int, beatable: str):
    assert beatable == horse(horse_coordinate_a, horse_coordinate_n, target_coordinate_a, target_coordinate_n)


@pytest.mark.parametrize("expected_exception, h_coordinate_a, h_coordinate_n, t_coordinate_a, t_coordinate_n",
                         [(TypeError, 1, 1, "a", 2),
                          (TypeError,"a", "a", "a", 2),
                          (ValueError,"a", 0, "a", 2),
                          (ValueError,"t", 1, "a", 2),
                          (ValueError,"a", 1, "a", 1)])
def test_horse_exception(expected_exception, h_coordinate_a, h_coordinate_n, t_coordinate_a, t_coordinate_n):
    with pytest.raises(expected_exception):
        horse(h_coordinate_a, h_coordinate_n, t_coordinate_a, t_coordinate_n)
