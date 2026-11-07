class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}'s account: balance {self.balance}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.balance})"
        
account = BankAccount("Emma", 500)
print(account)
print(f"Account: {account}")
accounts = [account, BankAccount("Sam", 200)]
print(accounts)
print(repr(account))
