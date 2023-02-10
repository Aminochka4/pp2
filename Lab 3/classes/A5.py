class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, cash):
        self.balance += cash
    def withdraw(self, cash2):
        if (cash2>self.balance):
            print("Error")
        else:
            self.balance -= cash2

name = input("Name:")
money = int(input("Cash:"))
money1 = Account(name, money)
money1.deposit(5000000)
print (money1.balance)
money1.withdraw(450)
print(money1.balance)


