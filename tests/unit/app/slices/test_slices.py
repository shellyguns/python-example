import pytest
from app.strings.slices.slices import slices


@pytest.mark.parametrize(
    "input_str, third_char, pre_last_char, first_five_chars, all_expt_last_two, even_inx, odd_inx, str_rev, str_len",
    [("Hello, world!", "l", "d", "Hell", "Hello, worl", "lo ol!", "el,wrd", "!dlrow ,olleH", 13),
     ("0123456789", "2", "8", "0123", "01234567", "2468", "13579", "9876543210", 10)]
)
def test_slices(input_str: str, third_char: str, pre_last_char: str, first_five_chars: str, all_expt_last_two: str,
                even_inx: str, odd_inx: str, str_rev: str, str_len: int):
    assert (third_char, pre_last_char, first_five_chars, all_expt_last_two, even_inx, odd_inx, str_rev, str_len) \
           == slices(input_str)


@pytest.mark.parametrize(
    "expected_exception, improper_input", [(TypeError, [1, 2, 3]),
                                           (TypeError, 1),
                                           (TypeError, 1.1),
                                           (TypeError, (1, 2, 3))]
)
def test_slices_exception(expected_exception, improper_input):
    with pytest.raises(expected_exception):
        slices(improper_input)
