import hashlib
import datetime
class Account:
    def __init__(self, account_number, owner_name, pin):
        self.account_number = account_number
        self.owner_name = owner_name
        self.pin_hash = self._hash_pin(pin)
        self.balance = 0.0
        self.transactions = []
        self.is_locked = False
        self.failed_attempts = 0


    def _hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    
    def verify_pin(self, pin):
        if self.is_locked:
            print("Account is locked. contact support")
            return False
        
        if self._hash_pin(pin) == self.pin_hash:
            self.failed_attempts = 0  # reset on success
            return True
        
        else:
            self.failed_attempts += 1
            remaining = 3 - self.failed_attempts
            if self.failed_attempts >= 3:
                self.is_locked = True
                print("Too many failed attempts Account Locked.")

            else:
                print(f"Wrong PIN. {remaining} attempt(s) remaining. ")
                return False
            
    def deposit(self, amount):
        if amount<= 0:
            print("Deposit amount must be greater than 0")
            return
        
        self.balance += amount 
        self._record_transaction("Deposit", amount)
        print(f"₦{amount:,.2f} deposited successfully")
        print(f"New balance: ₦{self.balance:,.2f}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            return
        
        if amount > self.balance:
            print(f"Insufficient Funds. your balance is ₦{self.balance:.2f}")
            return
        
        self.balance -= amount
        self._record_transaction("WITHDRAWAL", amount)
        print(f"₦{amount:2f} has been withdrawn successfully ")
        print(f"New Balance: ₦{self.balance:.2f}")

    def check_balance(self):
        print(f"\nAccount balance for {self.owner_name}")
        print(f"Account no: {self.account_number}")
        print(f"New Balance ₦{self.balance:.2f}")

    def view_transaction(self):
        print(f"Transaction History - {self.owner_name}")
        print("-"* 50)

        if len(self.transactions) == 0:
            print("No transactions Yet")
        else:
            for transaction in self.transactions:
                print(transaction)
        print("-"*50)

    def _record_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{timestamp}] {transaction_type:<12} ₦{amount} Balance: ₦{self.balance:,.2f}"
        self.transactions.append(record)


    def display_summary(self):
        print(f"\n {'=' * 40}")
        print(f"Account Holder: {self.owner_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account balance: {self.balance}")
        lock_status = "LOCKED" if self.is_locked else "ACTIVE"
        print(f"STATUS   : {lock_status}")
        print(f"{"="*40}")


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
        self.next_account_number = 1001


    def create_account(self, owner_name, pin):
        account_number = str(self.next_account_number)
        self.next_account_number += 1

        new_account = Account(account_number, owner_name, pin)
        self.accounts[account_number] = new_account


        print(f"\nAccount Successfully Created")
        print(f"Welcome to {self.bank_name}, {owner_name}")
        print(f"Your account number is {account_number}")
        print(f"Keep your PIN safe - it is never stored in plain text")
        return new_account
    
    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} not found!")



    def login(self, account_number, pin):
        account = self.find_account(account_number)
        if account is None:
            return None
        if account.verify_pin(pin):
            return account
        return None
    
    def show_all_account(self):
        print(f"\n{'=' * 40}")
        print(f"{self.bank_name} ----ALL ACCOUNTS")
        print(f"{'=' * 40}")


        if len(self.accounts) == 0:
            print("No accounts yet")
        else:
            for account_number, account in self.accounts.items():
                status = "LOCKED" if account.is_locked else "ACTIVE"
                print(f"{account_number} | {account.owner_name:<20} | ₦{account.balance:.2f} | {status}")
                
                print("="*40)
                print(f"TOTAL ACCOUNTS: {len(self.accounts)}")


def print_banner(bank_name):
    print("\n" + "=" * 50)
    print(f"Welcome to {bank_name}")
    print(f"Secure. Simple. Yours")
    print("="*50)


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Please enter a positive number")
                
        except ValueError:
            print("Invalid input. Enter a number (e.g 5000)")


def account_menu(account):
    while True:
        print(f"\n------- ACCOUNT MENU -------")
        print("1    Check Balance")
        print("2    Deposit")
        print("3    Withdraw")
        print("4    View Transaction history")
        print("5    LogOut")

        choice = input("Choose an option (1 - 5): ").strip()

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = get_valid_amount("Enter Deposit amount: ")
            account.deposit(amount)

        elif choice == "3":
            amount = get_valid_amount("Enter Withdrawal amount: ")
            account.withdraw(amount)
            
        elif choice == "4":
            account.view_transaction()

        elif choice == "5":
            print(f"\n Goodbye, {account.owner_name} Stay Secure.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5")


def main():
    bank = Bank("SecureBank Nigeria")
    print_banner(bank.bank_name)

    bank.create_account("praiz", "2020")

    while True:
        print("\n=============MAIN MENU==============")
        print("1. Create new account")
        print("2. Login to Account")
        print("3. View all account" )
        print("4. Exit")

        choice = input("Enter choice from (1-4): ").strip()
        if choice == "1":
            print("\n-----Create New Account----------")
            name = input("Enter Full Name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            pin = input("Create a 4 digit pin: ").strip()
            if not pin.isdigit() or len(pin) != 4:
                print("pin must be 4 digits")
                continue
            bank.create_account(name, pin)        


        elif choice == "2":
            print("---------Login-------------")
            account_number = input("Enter account Number: ").strip()
            pin = input("Enter Pin: ").strip()
            account = bank.login(account_number, pin)
            if account:
                account_menu(account)

        elif choice == "3":
            bank.show_all_account()

        elif choice == "4":
            print("\nThank you for using SecureBank Nigeria. Goodbye")
            break
        else:
            print("Invalid Choice please enter from (1-4)")

if __name__ == "__main__":
    main()








    