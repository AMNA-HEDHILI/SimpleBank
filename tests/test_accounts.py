import unittest
from bank.accounts import BankAccount, SavingsAccount, InterestRewardsAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount(100, "Test")
        acc.deposit(50)
        self.assertEqual(acc.balance, 150)

    def test_withdraw(self):
        acc = BankAccount(200, "Test")
        acc.withdraw(50)
        self.assertEqual(acc.balance, 150)

    def test_insufficient_funds(self):
        acc = BankAccount(50, "Test")
        with self.assertRaises(Exception):
            acc.withdraw(100)

if __name__ == '__main__':
    unittest.main()
