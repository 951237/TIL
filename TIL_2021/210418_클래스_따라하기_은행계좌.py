class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_interest_rate(self, interest_rate):
        return self.interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000

    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)
    
a1 = SavingAccount("홍길동", 123456, 10000, 0.05)
a1.add_interest()
print("저축예금의 잔액 = ", a1.balance)

a2 = CheckingAccount("김철수", 1234567, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액 = ", a2.balance)
