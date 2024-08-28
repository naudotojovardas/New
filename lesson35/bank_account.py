# Create a simple bank account class, BankAccount, with the following specifications:
# The BankAccount class should have an attribute balance that starts at 0.
# It should have an instance method deposit that allows an amount to be added to the balance.
# It should have an instance method withdraw that allows an amount to be taken from the balance.
#  If the balance is less than the withdrawal amount, print a message that says "Insufficient funds".
# Add a class method from_balance that takes a starting balance as an argument and returns a new BankAccount instance with that starting balance.
# Add a static method transfer that takes two BankAccount instances and an amount as arguments.
#  It should withdraw the amount from the first account and deposit it into the second account.
# MY MODS:
# I added a print statement to the transfer method to show the new balances for both accounts after the transfer is made.
# I added time.sleep() to the transfer method to simulate a delay in the transfer process.

import time
import functools


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print('Depositing...')
        time.sleep(2)
        return (f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Withdrawing...')
            time.sleep(2)
            return ("Insufficient funds")
        else:
            self.balance -= amount
            print('Withdrawing...')
            time.sleep(2)
            return (f"Withdrew {amount}. New balance: {self.balance}")

    @classmethod
    def from_balance(cls, starting_balance):
        new_account = cls()
        new_account.balance = starting_balance
        return new_account

    @staticmethod
    def transfer(account1, account2, amount):
        account1.withdraw(amount)
        print(f"Transferred {amount} from account1 to account2")
        time.sleep(1)
        print(f"New balance for account1: {account1.balance}")
        account2.deposit(amount)
        print(f"New balance for account1: {account1.balance}")
        print(f"New balance for account2: {account2.balance}")


acct1 = BankAccount.from_balance(100)
acct2 = BankAccount.from_balance(50)
print(acct1.balance) # 100
print(acct2.balance) # 50
print(acct1.deposit(50)) # Deposited 50. New balance: 150
print(acct2.deposit(100)) # Deposited 100. New balance: 150
print(acct1.withdraw(75)) # Withdrew 75. New balance: 75
print(acct2.withdraw(200)) # Insufficient funds