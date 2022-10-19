from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    payment_processor = PaymentProcessor("1234564789aaa")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()
