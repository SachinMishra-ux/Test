class BankAccount:
    ## arguments: When we pass values to parameters, those values are called arguments
    def __init__(self, name, balance):  ## constructor , method
        self.name = name
        self.balance = balance

    def deposit(self, amount):   #method because they are within class
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
            
    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew {amount}. New balance: {self.balance}"
            else:
                return "Insufficient balance"

    def display_balance(self):
            return f"Balance: {self.balance}"
    