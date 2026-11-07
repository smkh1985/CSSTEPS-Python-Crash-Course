class BankAccount:
    min_balance = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.min_balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
            
account = BankAccount("Emma", 500)
account.withdraw(300)
account.withdraw(150)
