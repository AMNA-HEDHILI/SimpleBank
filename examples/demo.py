import sys
import os

# Ensure the 'bank' package is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bank.accounts import BankAccount, SavingsAccount, InterestRewardsAccount

print("\n🔐 Welcome to SimpleBank Demo 🔐\n")

# Create accounts
account1 = BankAccount(100, "RegularAccount")
account2 = SavingsAccount(200, "SavingsAccount")
account3 = InterestRewardsAccount(300, "RewardsAccount")

print("\n--- Testing Deposits ---")
account1.deposit(50)
account2.deposit(100)
account3.deposit(200)

print("\n--- Testing Withdrawals ---")
account1.withdraw(30)
account2.withdraw(50)  # Includes a 5-unit fee
account3.withdraw(100)

print("\n--- Testing Transfers ---")
account1.transfer(50, account2)
account2.transfer(100, account3)

print("\n--- Testing Error: Withdraw more than balance ---")
account1.withdraw(500)  # This should trigger BalanceException

print("\n--- Testing Error: Transfer more than balance ---")
account2.transfer(1000, account3)  # This should trigger BalanceException

print("\n✅ Demo completed.\n")
