import pytest
from pay.processor import PaymentProcessor

API_KEY = "1234564789aaa"


def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor("")
        payment_processor.charge("5459755678641246", 12, 2024, 100)


def test_card_number_valid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.validate_card("5459755678641246", 12, 2024)


def test_card_number_invalid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.validate_card("5459755678641246", 12, 1900)


def test_card_number_invalid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.luhn_checksum("1234567890123456")


def test_card_number_valid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.luhn_checksum("5459755678641246")


def test_charge_card_valid():
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge("5459755678641246", 12, 2024, 100)


def test_charge_card_invalid():
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("1234567890123456", 12, 2024, 100)
