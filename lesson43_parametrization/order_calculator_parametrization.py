# Adjust your solution to first lesson's exercises using parametrization.
# Write 2-3 more useful fixtures for the OrderCalculator used in this lesson which can then be used for tests. Implement those tests.

import pytest

class OrderCalculator:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
    
    def calculate_tax(self, tax_rate):
        return self.calculate_total() * tax_rate
    
    def calculate_shipping(self, shipping_rate):
        return self.quantity * shipping_rate
    
    def calculate_grand_total(self, tax_rate, shipping_rate):
        return self.calculate_total() + self.calculate_tax(tax_rate) + self.calculate_shipping(shipping_rate)
    

@pytest.fixture
def order():
    return OrderCalculator(10, 5)

@pytest.fixture
def tax_rate():
    return 0.1

@pytest.fixture
def shipping_rate():
    return 1

def test_calculate_total(order):
    assert order.calculate_total() == 50

def test_calculate_tax(order, tax_rate):
    assert order.calculate_tax(tax_rate) == 5

def test_calculate_shipping(order, shipping_rate):
    assert order.calculate_shipping(shipping_rate) == 5
    
@pytest.mark.parametrize("price, quantity, expected_total", [(10, 5, 50), (20, 5, 100)])

def test_calculate_total(price, quantity, expected_total):
    order = OrderCalculator(price, quantity)
    assert order.calculate_total() == expected_total

@pytest.mark.parametrize("price, quantity, tax_rate, expected_tax", [(10, 5, 0.1, 5), (20, 5, 0.1, 10)])

def test_calculate_tax(price, quantity, tax_rate, expected_tax):
    order = OrderCalculator(price, quantity)
    assert order.calculate_tax(tax_rate) == expected_tax

@pytest.mark.parametrize("price, quantity, shipping_rate, expected_shipping", [(10, 5, 1, 5), (20, 5, 1, 5)])

def test_calculate_shipping(price, quantity, shipping_rate, expected_shipping):
    order = OrderCalculator(price, quantity)
    assert order.calculate_shipping(shipping_rate) == expected_shipping

@pytest.mark.parametrize("price, quantity, tax_rate, shipping_rate, expected_grand_total", [(10, 5, 0.1, 1, 60), (20, 5, 0.1, 1, 115)])

def test_calculate_grand_total(price, quantity, tax_rate, shipping_rate, expected_grand_total):
    order = OrderCalculator(price, quantity)
    assert order.calculate_grand_total(tax_rate, shipping_rate) == expected_grand_total



