# Create a class BankAccount that uses encapsulation to securely handle account balance management. 
# The class should prevent direct access to the balance attribute and provide methods for safe deposit and withdrawal actions.
            # Requirements
# Private balance attribute (_balance).
# Public methods to deposit, withdraw, and check_balance that ensure secure transactions and balance checks without exposing direct modifications to the balance

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return self._balance
        else:
            return "Invalid withdrawal amount"

    def check_balance(self):
        return self._balance
    
account = BankAccount(100)
account.deposit(150)
account.withdraw(50)
print(account.check_balance())