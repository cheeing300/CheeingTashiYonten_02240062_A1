# test_banking_app.py

import unittest
from CheeingTashiYonten_02240062_A3_PA import BankingSystem, NotEnoughMoney, TransferError, InvalidInputError

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        """Set up a new banking system and accounts for testing."""
        self.system = BankingSystem()
        self.system.create_account("Personal")  # Create a personal account for testing
        self.system.create_account("Business")  # Create a business account for testing
        self.personal_account = self.system.accounts[next(iter(self.system.accounts))]
        self.business_account = self.system.accounts[next(iter(self.system.accounts, self.personal_account.number))]

    def test_deposit_valid_amount(self):
        """Test that depositing a valid amount increases the balance."""
        initial_balance = self.personal_account.balance
        self.personal_account.deposit(100)
        self.assertEqual(self.personal_account.balance, initial_balance + 100)

    def test_deposit_invalid_amount(self):
        """Test that depositing a negative amount raises an error."""
        with self.assertRaises(InvalidInputError):
            self.personal_account.deposit(-50)

    def test_withdraw_valid_amount(self):
        """Test that withdrawing a valid amount decreases the balance."""
        self.personal_account.deposit(100)
        initial_balance = self.personal_account.balance
        self.personal_account.withdraw(50)
        self.assertEqual(self.personal_account.balance, initial_balance - 50)

    def test_withdraw_insufficient_funds(self):
        """Test that withdrawing more than the balance raises an error."""
        with self.assertRaises(NotEnoughMoney):
            self.personal_account.withdraw(50)

    def test_transfer_valid_amount(self):
        """Test that transferring a valid amount updates both accounts' balances."""
        self.personal_account.deposit(100)
        initial_personal_balance = self.personal_account.balance
        initial_business_balance = self.business_account.balance
        self.personal_account.transfer(50, self.business_account)
        self.assertEqual(self.personal_account.balance, initial_personal_balance - 50)
        self.assertEqual(self.business_account.balance, initial_business_balance + 50)

    def test_transfer_insufficient_funds(self):
        """Test that transferring more than the balance raises an error."""
        with self.assertRaises(NotEnoughMoney):
            self.personal_account.transfer(50, self.business_account)

    def test_transfer_invalid_account(self):
        """Test that transferring to an invalid account raises an error."""
        with self.assertRaises(TransferError):
            self.personal_account.transfer(50, None)

    def test_delete_account(self):
        """Test that deleting an account removes it from the system."""
        account_number = self.personal_account.number
        self.system.delete_account(account_number)
        self.assertNotIn(account_number, self.system.accounts)

    def test_top_up_mobile_valid_amount(self):
        """Test that topping up a mobile phone with a valid amount works."""
        # Here we just check if the method runs without raising an error
        try:
            self.system.top_up_mobile("1234567890", 50)
        except Exception as e:
            self.fail(f"top_up_mobile raised an exception: {e}")

    def test_top_up_mobile_invalid_amount(self):
        """Test that topping up with a negative amount raises an error."""
        with self.assertRaises(InvalidInputError):
            self.system.top_up_mobile("1234567890", -10)

if __name__ == '__main__':
    unittest.main()
