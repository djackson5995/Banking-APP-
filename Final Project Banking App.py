import random

class Account:
    def __init__(self, first_name, last_name, ssn):
        """
        Initializes a new account with the given owner's details.
        
        Args:
            first_name (str): The first name of the account holder.
            last_name (str): The last name of the account holder.
            ssn (str): The social security number of the account holder.
        
        Attributes:
            account_number (int): Randomly generated account number.
            pin (str): Randomly generated 4-digit PIN for account security.
            balance (int): Account balance in cents (default is 0).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.account_number = random.randint(1000000000, 9999999999)
        self.pin = str(random.randint(1000, 9999))
        self.balance = 0

    def __str__(self):
        """
        Provides a human-readable representation of the account.
        
        Returns:
            str: A string representation of the account details with masked SSN.
        """
        ssn_masked = f"XXX-XX-{self.ssn[-4:]}"
        balance_str = f"${self.balance / 100:.2f}"
        return (f"Account Number: {self.account_number}\n"
                f"Owner: {self.first_name} {self.last_name}\n"
                f"SSN: {ssn_masked}\n"
                f"PIN: {self.pin}\n"
                f"Balance: {balance_str}\n")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        
        Args:
            amount (int): The amount to deposit in cents.
        
        Returns:
            int: The new balance after deposit.
        
        Doctest:
        >>> account = Account('John', 'Doe', '123456789')
        >>> account.deposit(500)
        500
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.
        
        Args:
            amount (int): The amount to withdraw in cents.
        
        Returns:
            int: The new balance after withdrawal.
        
        Raises:
            ValueError: If the amount is greater than the current balance.
        
        Doctest:
        >>> account = Account('John', 'Doe', '123456789')
        >>> account.deposit(500)
        500
        >>> account.withdraw(300)
        200
        >>> account.withdraw(300)
        Traceback (most recent call last):
        ...
        ValueError: Insufficient funds.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def change_pin(self, new_pin):
        """
        Changes the account PIN.
        
        Args:
            new_pin (str): The new PIN to set.
        
        Doctest:
        >>> account = Account('John', 'Doe', '123456789')
        >>> account.pin = '1234'
        >>> account.change_pin('5678')
        >>> account.pin
        '5678'
        """
        self.pin = new_pin

    def apply_interest(self, annual_rate):
        """
        Applies monthly interest to the account based on the annual interest rate.
        
        Args:
            annual_rate (float): The annual interest rate in percentage.
        
        Doctest:
        >>> account = Account('John', 'Doe', '123456789')
        >>> account.deposit(120000)  # $1200 in cents
        >>> account.apply_interest(12)  # 12% annual rate
        >>> account.balance
        121200.0
        """
        monthly_interest = self.balance * (annual_rate / 100) / 12
        self.deposit(monthly_interest)


class Bank:
    def __init__(self):
        """
        Initializes a new bank with an empty dictionary of accounts.
        """
        self.accounts = {}

    def add_account(self, account):
        """
        Adds an account to the bank.
        
        Args:
            account (Account): The account object to add.
        """
        self.accounts[account.account_number] = account

    def find_account(self, account_number):
        """
        Retrieves an account by its number.
        
        Args:
            account_number (int): The account number to search for.
        
        Returns:
            Account or None: The account object if found, otherwise None.
        """
        return self.accounts.get(account_number)

    def remove_account(self, account_number):
        """
        Removes an account from the bank.
        
        Args:
            account_number (int): The account number to remove.
        
        Returns:
            bool: True if the account was removed, False if not found.
        """
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False


class BankManager:
    """Interface for managing bank operations via console."""
    
    def __init__(self):
        """
        Initializes the BankManager with a new bank instance.
        """
        self.bank = Bank()

    def main(self):
        """
        Main menu for bank operations. Loops until the user chooses to exit.
        """
        options = {
            '1': self.open_account,
            '2': self.display_account_info,
            '3': self.change_account_pin,
            '4': self.deposit_into_account,
            '5': self.transfer_between_accounts,
            '6': self.withdraw_from_account,
            '7': self.atm_withdrawal,
            '8': self.close_account,
            '9': self.apply_interest_to_all_accounts,
            '10': self.deposit_change,
            '0': exit
        }
        while True:
            print("\nMain Menu")
            print("1: Open a New Account")
            print("2: Display Account Information")
            print("3: Change Account PIN")
            print("4: Deposit Money")
            print("5: Transfer Money Between Accounts")
            print("6: Withdraw Money")
            print("7: ATM Withdrawal")
            print("8: Close an Account")
            print("9: Apply Monthly Interest to All Accounts")
            print("10: Deposit Change")
            print("0: Exit")
            choice = input("Choose an option: ")
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please try again.")

    def get_account_by_pin(self):
        """
        Prompts user for PIN and retrieves the account if the PIN is correct.
        
        Returns:
            Account or None: The account object if the correct PIN is entered, otherwise None.
        """
        pin = input("Enter your 4-digit PIN: ")
        for account in self.bank.accounts.values():
            if account.pin == pin:
                return account
        print("Invalid PIN. Please try again.")
        return None
    
    def open_account(self):
        """
        Opens a new account by collecting user details.
        """
        print("\n--- Open a New Account ---")
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        
        while True:
            ssn = input("Enter the SSN (9 digits): ")
            if ssn.isdigit() and len(ssn) == 9:
                break
            else:
                print("Invalid SSN format. Please enter exactly 9 digits.")
        
        account = Account(first_name, last_name, ssn)
        self.bank.add_account(account)
        print("Account created successfully.")
        print(account)

    def display_account_info(self):
        """
        Displays information for a specific account based on the account number.
        """
        account = self.get_account_by_number()
        if account:
            print("\n--- Account Information ---")
            print(account)

    def change_account_pin(self):
        """
        Changes the PIN for a specific account after verifying the account number.
        """
        account = self.get_account_by_number()
        if account:
            while True:
                new_pin = input("Enter a new PIN (4 digits): ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    account.change_pin(new_pin)
                    print("PIN changed successfully.")
                    break
                else:
                    print("Invalid PIN format. PIN must be 4 digits.")

    def deposit_into_account(self):
        """
        Deposits money into a specific account after verifying the account PIN.
        """
        account = self.get_account_by_pin()
        if account:
            while True:
                try:
                    amount = float(input("Enter the amount to deposit ($): "))
                    if amount > 0:
                        account.deposit(int(amount * 100))  # Convert dollars to cents
                        print(f"Deposited ${amount:.2f} successfully.")
                        print(f"New Balance: ${account.balance / 100:.2f}")
                        break
                    else:
                        print("Amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

    def deposit_change(self):
        """
        Handles counting coins and depositing change into an account.
        """
        account = self.get_account_by_pin()
        if account:
            while True:
                try:
                    coins = input("Enter the number of coins to deposit (pennies, nickels, dimes, quarters): ")
                    pennies, nickels, dimes, quarters = map(int, coins.split())
                    total_cents = pennies + nickels * 5 + dimes * 10 + quarters * 25
                    account.deposit(total_cents)
                    print(f"Deposited ${total_cents / 100:.2f} in coins successfully.")
                    print(f"New Balance: ${account.balance / 100:.2f}")
                    break
                except ValueError:
                    print("Invalid input. Please enter four integers separated by spaces.")

    def transfer_between_accounts(self):
        """
        Transfers money from one account to another.
        """
        print("\n--- Transfer Money Between Accounts ---")
        print("From Account:")
        from_account = self.get_account_by_number()
        
        if from_account:
            print("To Account:")
            to_account = self.get_account_by_number()

            if to_account:
                while True:
                    try:
                        amount = input("Enter the amount to transfer ($), or type 'exit' to return to the main menu: ")
                        
                        if amount.lower() == 'exit':
                            print("Returning to main menu.")
                            break
                        
                        amount = float(amount)
                        
                        if amount > 0:
                            if from_account.balance >= amount * 100:
                                from_account.withdraw(int(amount * 100))
                                to_account.deposit(int(amount * 100))
                                print(f"Transferred ${amount:.2f} successfully.")
                                print(f"New Balance in From Account: ${from_account.balance / 100:.2f}")
                                print(f"New Balance in To Account: ${to_account.balance / 100:.2f}")
                                break
                            else:
                                print("Insufficient funds in the From Account. Please enter a lower amount or type 'exit' to return to the main menu.")
                        else:
                            print("Amount must be positive. Please enter a valid amount or type 'exit' to return to the main menu.")
                    
                    except ValueError:
                        print("Invalid input. Please enter a valid amount or type 'exit' to return to the main menu.")

    def withdraw_from_account(self):
        """
        Withdraws money from a specific account after verifying the account PIN.
        """
        account = self.get_account_by_pin()
        if account:
            while True:
                try:
                    amount = input("Enter the amount to withdraw ($), or type 'exit' to return to the main menu: ")
                    
                    if amount.lower() == 'exit':
                        print("Returning to main menu.")
                        break
                    
                    amount = float(amount)
                    
                    if amount > 0:
                        if account.balance >= amount * 100:
                            account.withdraw(int(amount * 100))  # Convert dollars to cents
                            print(f"Withdrew ${amount:.2f} successfully.")
                            print(f"New Balance: ${account.balance / 100:.2f}")
                            break
                        else:
                            print("Insufficient funds. Please enter a lower amount or type 'exit' to return to the main menu.")
                    else:
                        print("Amount must be positive. Please enter a valid amount or type 'exit' to return to the main menu.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount or type 'exit' to return to the main menu.")

    def atm_withdrawal(self):
        """
        Handles ATM-style withdrawals from an account using a PIN.
        """
        account = self.get_account_by_pin()
        if account:
            while True:
                try:
                    amount = input("Enter the amount to withdraw in multiples of $10 (up to $1000), or type 'exit' to return to the main menu: ")
                    
                    if amount.lower() == 'exit':
                        print("Returning to main menu.")
                        break
                    
                    amount = int(amount)
                    
                    if amount > 0 and amount <= 1000 and amount % 10 == 0:
                        if account.balance >= amount * 100:
                            account.withdraw(amount * 100)
                            twenties = amount // 20
                            tens = (amount % 20) // 10
                            print(f"Withdrew ${amount:.2f} in ${twenties} twenties and ${tens} tens.")
                            print(f"New Balance: ${account.balance / 100:.2f}")
                            break
                        else:
                            print("Insufficient funds. Please enter a lower amount or type 'exit' to return to the main menu.")
                    else:
                        print("Invalid withdrawal amount. Please enter a multiple of $10 up to $1000 or type 'exit' to return to the main menu.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount or type 'exit' to return to the main menu.")

    def close_account(self):
        """
        Closes a specific account by verifying the account number.
        """
        while True:
            account_number = input("Enter the account number to close: ")
            if account_number.isdigit() and self.bank.remove_account(int(account_number)):
                print("Account closed successfully.")
                break
            else:
                print("Account not found or invalid account number. Please try again.")

    def apply_interest_to_all_accounts(self):
        """
        Applies monthly interest to all accounts in the bank.
        """
        while True:
            try:
                annual_rate = float(input("Enter the annual interest rate (%): "))
                if annual_rate > 0:
                    for account in self.bank.accounts.values():
                        account.apply_interest(annual_rate)
                    print("Monthly interest applied to all accounts.")
                    break
                else:
                    print("Interest rate must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid interest rate.")

    def get_account_by_number(self):
        """
        Prompts user for account number and retrieves the account from the bank.
        
        Returns:
            Account or None: The account object if found, otherwise None.
        """
        while True:
            account_number = input("Enter the account number: ")
            if account_number.isdigit():
                account = self.bank.find_account(int(account_number))
                if account:
                    return account
            print("Invalid account number or account not found. Please try again.")

if __name__ == "__main__":
    manager = BankManager()
    manager.main()

