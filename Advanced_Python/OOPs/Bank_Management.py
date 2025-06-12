class BankAccount:
    totalAccounts = 0
    next_account_number = 1001

    def __init__(self, name, balance, account_type):
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

        self.name = name
        self.balance = balance
        self.account_type = account_type

        BankAccount.totalAccounts += 1

    def display_details(self):
        print(f"Account number : {self.account_number} || Name : {self.name} || Balance : ₹{self.balance} || Account type : {self.account_type}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Amount = ₹{amount}, New Balance = ₹{self.balance}")
        else:
            print("Deposit cannot be negative!!!")

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f"Withdrawn Amount = ₹{amount}, Remaining Amount = ₹{self.balance}")
        else:
            print("Not Sufficient Funds")

    @classmethod
    def get_total_accounts(cls):
        print(f"Total active accounts: {cls.totalAccounts}")

user1 = BankAccount("Ritik", 50000, "Savings")
user2 = BankAccount("Raghav", 75000, "Current")

user1.display_details()
user2.display_details()

user1.deposit(10000)
user2.withdraw(10000)

user1.display_details()
user2.display_details()

BankAccount.get_total_accounts()