from bank.exceptions import BalanceException

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return True
        else:
            raise BalanceException(f"❌ Insufficient funds in '{self.name}' (Balance: ${self.balance:.2f})")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'Withdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n***** Beginning Transfer *****')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer complete!\n***************************')
        except BalanceException as error:
            print(f'Transfer interrupted: {error}')


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("Deposit with interest complete.")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("Withdraw with fee complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'Withdraw interrupted: {error}')
