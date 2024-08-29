# Banking Application
This is a simple Python program that simulates a banking system, allowing users to manage their accounts, perform transactions, and apply interest.

## How It Works
The program provides a console-based interface and prompts the user to:

1. Open a New Account: Enter personal details to create a new bank account.
2. Deposit Money: Enter the amount to deposit into an account.
3. Withdraw Money: Enter the amount to withdraw from an account, ensuring sufficient funds are available.
4. Transfer Money: Transfer funds between two accounts within the bank.
5. Change Account PIN: Update the PIN associated with an account for security purposes.
6. Apply Interest: Apply a specified annual interest rate to all accounts, compounded monthly.
7. ATM Withdrawals: Perform cash withdrawals with specific denominations.
8. Deposit Change: Deposit various coins (pennies, nickels, dimes, quarters) into an account.
9. Close an Account: Remove an account from the bank’s records.
   
It calculates:

- Account balances after deposits, withdrawals, and transfers.
- Interest application based on the provided annual rate.
- New account details after changing the PIN or closing an account.
- Example Usage
```plaintext
Copy code
Welcome to the Banking Application

Main Menu
1: Open a New Account
2: Display Account Information
3: Change Account PIN
4: Deposit Money
5: Transfer Money Between Accounts
6: Withdraw Money
7: ATM Withdrawal
8: Close an Account
9: Apply Monthly Interest to All Accounts
10: Deposit Change
0: Exit

Choose an option: 1

--- Open a New Account ---
Enter the first name: John
Enter the last name: Doe
Enter the SSN (9 digits): 123456789
Account created successfully.
Account Number: 1234567890
Owner: John Doe
SSN: XXX-XX-6789
PIN: 4321
Balance: $0.00
Depositing Money
plaintext
Copy code
Main Menu
Choose an option: 4

Enter your 4-digit PIN: 4321
Enter the amount to deposit ($): 100
Deposited $100.00 successfully.
New Balance: $100.00
Transferring Money Between Accounts
plaintext
Copy code
Main Menu
Choose an option: 5

--- Transfer Money Between Accounts ---
From Account:
Enter the account number: 1234567890
To Account:
Enter the account number: 0987654321
Enter the amount to transfer ($): 50
Transferred $50.00 successfully.
New Balance in From Account: $50.00
New Balance in To Account: $50.00 
