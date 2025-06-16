import random
import tkinter as tk
from tkinter import messagebox

# Custom error classes for specific problems
class NotEnoughMoney(Exception):
    "printed when trying to take out more money than the account has."
    pass

class TransferError(Exception):
    "printed when a transfer cannot be completed."
    pass

# Basic bank account class
class BankAccount:
    def __init__(self, number, password, acc_type, balance=0):
        self.number = number
        self.password = password
        self.type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited Nu.{amount}. Your new balance is Nu.{self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise NotEnoughMoney("Sorry, insufficient amount")
        self.balance -= amount
        print(f"You withdrew Nu.{amount}. Your new balance is Nu.{self.balance}.")

    def transfer(self, amount, other_account):
        if amount > self.balance:
            raise NotEnoughMoney("Sorry, insufficient amount ")
        if other_account is None:
            raise TransferError(" Invalid Account Number")
        self.withdraw(amount)
        other_account.deposit(amount)
        print(f"You sent Nu.{amount} to account {other_account.number}.")

# Personal account inherits from BankAccount
class PersonalAccount(BankAccount):
    def __init__(self, number, password, balance=0):
        super().__init__(number, password, "Personal", balance)

# Business account inherits from BankAccount
class BusinessAccount(BankAccount):
    def __init__(self, number, password, balance=0):
        super().__init__(number, password, "Business", balance)

# Main banking system class
class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    number, password, acc_type, bal = line.strip().split(',')
                    bal = float(bal)
                    if acc_type == "Personal":
                        self.accounts[number] = PersonalAccount(number, password, bal)
                    else:
                        self.accounts[number] = BusinessAccount(number, password, bal)
        except FileNotFoundError:
            print("No saved accounts found. Sign up! ")

    def save_accounts(self):
        with open("accounts.txt", "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.number},{acc.password},{acc.type},{acc.balance}\n")

    def create_account(self, acc_type):
        # Generate unique account number
        while True:
            number = str(random.randint(1000, 9999))
            if number not in self.accounts:
                break
        password = str(random.randint(100000, 999999))
        if acc_type.lower() == "personal":
            account = PersonalAccount(number, password)
        else:
            account = BusinessAccount(number, password)
        self.accounts[number] = account
        self.save_accounts()
        print(f"Account created!\nAccount number: {number}\nPassword: {password}")

    def login(self, number, password):
        account = self.accounts.get(number)
        if account is None:
            print("Account number does not exist.")
            return None
        elif account.password != password:
            print("Wrong password.")
            return None
        else:
            print(f"Welcome to your {account.type} account!"
                  "Please do not share your password ")
            return account

    def delete_account(self, number):
        if number in self.accounts:
            del self.accounts[number]
            self.save_accounts()
            print(f"Account {number} deleted.")
        else:
            print("Account not found.")

    def top_up_mobile(self, phone, amount):
        print(f"You topped up Nu.{amount} to phone number {phone}.")

    def process_choice(self, choice):
        if choice == "1":
            acc_type = input("Type of account? Personal or Business: ").strip()
            if acc_type.lower() not in ["personal", "business"]:
                print("Invalid account type.")
                return True
            self.create_account(acc_type)
        elif choice == "2":
            number = input("Enter your account number: ").strip()
            password = input("Enter your password: ").strip()
            account = self.login(number, password)
            if account:
                self.account_menu(account)
        elif choice == "3":
            print("Goodbye!")
            return False
        else:
            print("Please enter 1, 2, or 3.")
        return True

    def account_menu(self, account):
        while True:
            print("\nWhat would you like to do?")
            print("1. Check balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Transfer money")
            print("5. Delete account")
            print("6. Mobile phone top-up")
            print("7. Logout")

            choice = input("Choose 1-7: ").strip()
            if choice == "1":
                print(f"Your balance is Nu.{account.balance}.")
            elif choice == "2":
                try:
                    amount = float(input("How much to deposit? "))
                    if amount <= 0:
                        print("Enter a positive number.")
                        continue
                    account.deposit(amount)
                    self.save_accounts()
                except ValueError:
                    print("Please enter a number.")
            elif choice == "3":
                try:
                    amount = float(input("How much to withdraw? "))
                    if amount <= 0:
                        print("Enter a positive number.")
                        continue
                    account.withdraw(amount)
                    self.save_accounts()
                except ValueError:
                    print("Please enter a number.")
                except NotEnoughMoney as e:
                    print(e)
            elif choice == "4":
                recipient_num = input("Recipient account number: ").strip()
                recipient = self.accounts.get(recipient_num)
                if recipient is None:
                    print("Recipient account not found.")
                    continue
                try:
                    amount = float(input("Amount to transfer: "))
                    if amount <= 0:
                        print("Enter a positive number.")
                        continue
                    account.transfer(amount, recipient)
                    self.save_accounts()
                except ValueError:
                    print("Please enter a number.")
                except NotEnoughMoney as e:
                    print(e)
                except TransferError as e:
                    print(e)
            elif choice == "5":
                confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.delete_account(account.number)
                    break
            elif choice == "6":
                phone = input("Phone number to top up: ").strip()
                try:
                    amount = float(input("Amount to top up: "))
                    if amount <= 0:
                        print("Enter a positive number.")
                        continue
                    self.top_up_mobile(phone, amount)
                except ValueError:
                    print("Please enter a number.")
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Please enter a number between 1 and 7.")

bank = BankingSystem()
current_account = None

# Simple GUI to open the app (optional for beginners)
class BankingGUI:
    def __init__(self, system):
        self.system = system
        self.window = tk.Tk()
        self.window.title("Bank App")
        self.window.geometry("400x300")

        tk.Label(self.window, text="Welcome to Bank Of DrukYul ").pack(pady=10)
        tk.Button(self.window, text="Open Account", width=30, command=self.open_account).pack(pady=5)
        tk.Button(self.window, text="Login", width=30, command=self.login).pack(pady=5)
        tk.Button(self.window, text="Exit", width=30, command=self.window.quit).pack(pady=5)

    def open_account(self):
        acc_type = simpledialog.askstring("Account Type", "Personal or Business:", parent=self.window)
        if acc_type is None:
            return
        if acc_type.lower() not in ["personal", "business"]:
            messagebox.showerror("Error", "Type must be Personal or Business.")
            return
        self.system.create_account(acc_type)

    def login(self):
        acc_num = simpledialog.askstring("Account Number", "Enter your account number:", parent=self.window)
        pwd = simpledialog.askstring("Password", "Enter your password:", parent=self.window, show='*')
        if acc_num is None or pwd is None:
            return
        account = self.system.login(acc_num.strip(), pwd.strip())
        if account:
            messagebox.showinfo("Success", f"Logged into your {account.type} account!")
        else:
            messagebox.showerror("Error", "Login failed.")

    def run(self):
        self.window.mainloop()

def main():
    system = BankingSystem()
    gui = BankingGUI(system)
    gui.run()

main()


def terminal_menu():
    system = BankingSystem()
    print("Welcome to the Bank of Drukyul!")

    running = True
    while running:
        print("\nMain Menu:")
        print("1 - Open Account")
        print("2 - Login")
        print("3 - Exit")

        choice = input("Please enter your choice (1-3): ").strip()
        running = system.process_choice(choice)

terminal_menu()

