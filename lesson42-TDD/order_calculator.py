# Finish developing OrderCalculator by writing tests first that adhere to the requirements. Follow-up these tests with appropriate implementations.

import unittest

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
    
class TestOrderCalculator(unittest.TestCase):
    def test_calculate_total(self):
        order = OrderCalculator(10, 5)
        self.assertEqual(order.calculate_total(), 50)
    
    def test_calculate_tax(self):
        order = OrderCalculator(10, 5)
        self.assertEqual(order.calculate_tax(0.1), 5)
    
    def test_calculate_shipping(self):
        order = OrderCalculator(10, 5)
        self.assertEqual(order.calculate_shipping(2), 10)
    
    def test_calculate_grand_total(self):
        order = OrderCalculator(10, 5)
        self.assertEqual(order.calculate_grand_total(0.1, 2), 65)


unittest.main()

    
