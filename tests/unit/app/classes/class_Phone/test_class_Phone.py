import pytest
from app.classes.class_Phone.class_Phone import Phone
phone = Phone("0675553535", "Phone", "100")


@pytest.mark.parametrize(
    "caller_name, maybe_number, screen_message", [("Someone", "0123", "Someone is calling on Phone with number 0123"),
                                                  ("No_name", None, "No_name is calling on Phone")]
)
def test_receive_call(caller_name: str, maybe_number: str, screen_message: str):
    assert screen_message == phone.receive_call(caller_name, maybe_number)


@pytest.mark.parametrize(
    "expected_exception, improper_name, improper_number", [(TypeError, 1010, 1.2),
                                                           (TypeError, 1.2, None)]
)
def test_receive_call_exception(expected_exception, improper_name, improper_number):
    with pytest.raises(expected_exception):
        phone.receive_call(improper_name, improper_number)


@pytest.mark.parametrize(
    "recipient_number, message_of_numbers", [(("01324",), "Phone sends message on the following number(s): ('01324',)"),
                                             (("111", "222"),
                                              "Phone sends message on the following number(s): ('111', '222')")]
)
def test_send_message(recipient_number: str, message_of_numbers: str):
    assert message_of_numbers == phone.send_message(*recipient_number)


@pytest.mark.parametrize(
    "expected_exception, improper_numbers", [(TypeError, (1010, )),
                                             (TypeError, (1.2, 1010))]
)
def test_send_message_exception(expected_exception, improper_numbers):
    with pytest.raises(expected_exception):
        phone.send_message(*improper_numbers)
