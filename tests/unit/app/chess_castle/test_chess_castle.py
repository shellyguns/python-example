import pytest
from app.conditional_operator.chess_castle.chess_castle import chess_castle


@pytest.mark.parametrize("castle_coordinate_a, castle_coordinate_n, target_coordinate_a, target_coordinate_n, beatable",
                         [("a", 1, "a", 5, "Yes"),
                          ("a", 1, "g", 1, "Yes"),
                          ("b", 2, "c", 3, "No")]
                         )
def test_chess_castle(castle_coordinate_a: str, castle_coordinate_n: int, target_coordinate_a: str,
                      target_coordinate_n: int, beatable: str):
    assert beatable == chess_castle(castle_coordinate_a, castle_coordinate_n, target_coordinate_a, target_coordinate_n)


@pytest.mark.parametrize("expected_exception, c_coordinate_a, c_coordinate_n, t_coordinate_a, t_coordinate_n",
                         [(TypeError, 1, 1, "a", 2),
                          (TypeError, "a", "a", "a", 2),
                          (ValueError, "a", 11, "a", 2),
                          (ValueError, "t", 1, "a", 2),
                          (ValueError, "a", 1, "a", 1)])
def test_chess_castle_exception(expected_exception, c_coordinate_a, c_coordinate_n, t_coordinate_a, t_coordinate_n):
    with pytest.raises(expected_exception):
        chess_castle(c_coordinate_a, c_coordinate_n, t_coordinate_a, t_coordinate_n)
