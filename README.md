Banking Application
Overview
This is a Python-based console application that simulates basic banking operations. It allows users to manage multiple accounts, deposit and withdraw money, transfer funds, change PINs, and apply interest to accounts. This application is designed to provide a simple and secure way to handle banking transactions.

Features
Account Management: Open new accounts, close existing accounts, and manage account details.
Deposit and Withdrawal: Deposit money into accounts and withdraw money using account numbers or PINs.
Fund Transfers: Transfer money between different accounts within the bank.
PIN Management: Change account PINs securely.
Interest Application: Apply monthly interest to all accounts based on an annual rate.
ATM Withdrawals: Simulate ATM-style cash withdrawals with specific denominations.
Change Deposit: Deposit coins by counting pennies, nickels, dimes, and quarters.
Data Security: Secure account information using random account numbers and PINs.

Installation
Clone the Repository: Download or clone the repository to your local machine.

bash
Copy code
git clone <repository-url>
Navigate to the Directory: Open the terminal or command prompt and navigate to the project directory.

bash
Copy code
cd banking-app
Run the Application: Execute the main Python script to start the banking application.

bash
Copy code
python bank_manager.py
Usage
Once the application starts, you will see a menu with various options. Simply enter the corresponding number for the action you wish to perform:

Open a New Account: Create a new account by providing your details.
Display Account Information: View details of an existing account.
Change Account PIN: Update the security PIN for your account.
Deposit Money: Add funds to an account.
Transfer Money Between Accounts: Move funds from one account to another.
Withdraw Money: Take money out of an account.
ATM Withdrawal: Withdraw money in specific denominations.
Close an Account: Remove an account from the bank's records.
Apply Monthly Interest to All Accounts: Increase account balances based on a provided annual interest rate.
Deposit Change: Deposit coins into an account by specifying quantities of pennies, nickels, dimes, and quarters.
Exit: Exit the application.
Examples
Opening a New Account
Choose option 1 from the menu.
Enter the first name, last name, and SSN (Social Security Number).
An account is created with a random account number and PIN.
Depositing Money
Choose option 4 from the menu.
Enter your PIN to authenticate.
Enter the amount to deposit.
Transferring Money Between Accounts
Choose option 5 from the menu.
Enter the account numbers for both the source and destination accounts.
Enter the transfer amount.
Code Structure
Account Class: Represents individual bank accounts, including methods for deposits, withdrawals, PIN changes, and applying interest.
Bank Class: Represents the bank, holding multiple accounts and providing methods for adding, finding, and removing accounts.
BankManager Class: Provides a console-based interface for interacting with the bank and managing operations.
