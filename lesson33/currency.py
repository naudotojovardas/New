# Design a Currency class in Python that encapsulates the attributes and behaviors associated with monetary values, offering functionalities for setting currency properties,
# performing currency conversion, and displaying currency information.
# Currency class requirements
# Attributes:
# code: The 3-letter ISO currency code (e.g., "USD", "EUR", "GBP") representing the type of currency.
# amount: A floating-point number representing the monetary value.
# exchange_rate: A floating-point number representing the currency's exchange rate relative to a base currency.
# Methods:
# set_code(self, code): Sets the currency's 3-letter code. Returns the Currency instance to support method chaining.
# set_amount(self, amount): Sets the currency's amount. The input should be a positive float. Returns the Currency instance for method chaining.
# set_exchange_rate(self, exchange_rate): Sets the exchange rate of the currency. 
# The input should be a positive float representing how much of the currency equals one unit of the base currency. Returns the Currency instance for method chaining.
# convert(self, new_code, new_exchange_rate): Converts the currency to a new currency using the specified new exchange rate.
# Updates the amount based on this rate and changes the currency code. Returns the modified Currency instance for method chaining.
# __str__(self): Provides a string representation of the currency in the format "code: amount", where amount is formatted to two decimal places.

# MY MODS: PRACTICE DECORATORS
# Use decorators to print a separator before and after the currency information when calling the print_currency method.


import functools

def print_separator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\\\\\\\\\\\\\\\\\\\\\\\\")
        func(*args, **kwargs)
        print("////////////////////////")
    return wrapper

class Currency:
    def __init__(self, code, amount, exchange_rate):
        self.code = code
        self.amount = amount
        self.exchange_rate = exchange_rate

    def set_code(self, code):
        self.code = code
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code, new_exchange_rate):
        self.amount /= self.exchange_rate
        self.exchange_rate = new_exchange_rate
        self.code = new_code
        self.amount *= self.exchange_rate
        return self

    def __str__(self):
        return f"{self.code}: {self.amount:.2f}"
    
    @print_separator
    def print_currency(self):
        print(self)

# Create a Currency instance
currency = Currency("USD", 1000, 1)
currency.print_currency()

# Set the currency code and amount
currency.set_code("EUR").set_amount(500).print_currency()

# Set the exchange rate
currency.set_exchange_rate(0.8).print_currency()

# Convert the currency to a new currency
currency.convert("GBP", 0.7).print_currency()
