class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount - (amount * 0.01)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount + (amount * 0.01)
        else:
            print("Недостаточно средств на счете.")

    def get_balance(self):
        return self.balance


account1 = BankAccount("1234567890", "Ахмет Венгалби", 1000)
account2 = BankAccount("0987654321", "Асхаб Тамаев", 500)

account1.deposit(200)
account2.deposit(300)

account1.withdraw(150)
account2.withdraw(250)

print("Баланс счета {}: {}".format(account1.account_number, account1.get_balance()))
print("Баланс счета {}: {}".format(account2.account_number, account2.get_balance()))
