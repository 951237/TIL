class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def with_draw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
        