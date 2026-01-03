class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Nepakanka lešu")
        else:
            self.balance -= amount

    def show(self):
        print(self.balance)


jonas = BankAccount("jonas", 0)
jonas.show()
jonas.deposit(1000)
jonas.withdraw(100)
jonas.show()


