Bank Management System that allows customers to interact with there bank accounts and loan services. It allows the creation of bank accounts (both savings and current), depositing and withdrawing funds, checking balances, displaying account information, applying for loans, making loan payments, and viewing loan details. The system uses Python classes to model different components and functionalities.
 
Imports:
-random: Used to generate random account and loan IDs.
-pandas: A data manipulation library used to read, modify, and save data from/to CSV files.
-csv: Standard Python library to read and write CSV files, used for saving and loading account and loan data.

Classes:
-BankAccount Class:
  Models a generic bank account.
  Has methods for depositing, withdrawing, getting balance, and displaying account information.
  When a deposit or withdrawal happens, the balance is updated.

-SavingsAccount Class:
  Inherits from BankAccount.
  Adds an interest rate and a method to calculate interest.
  When interest is calculated, it's added to the balance.

-CurrentAccount Class:
  Also inherits from BankAccount.
  Adds features for an overdraft limit and withdrawal fee.
  It overrides the withdraw method to handle withdrawals that exceed the balance but remain within the overdraft limit.

-Loan Class:
  Models a loan.
  Contains information like loan ID, account number, principal amount, interest rate, and loan term.
  It calculates monthly payments based on the loan parameters.

Functions:
  save_accounts: Saves account details to a CSV file.
  load_accounts: Loads accounts from a CSV file.
  save_loans: Saves loan details to a CSV file.
  load_loans: Loads loan details from a CSV file.

Main Function:
  The main() function provides a user interface in the form of a console menu. Users can choose different options such as creating accounts, depositing funds, withdrawing funds, checking balances, and applying for loans. The system interacts with CSV files to persist account and loan information.

Core Operations in the Program:
  Creating an account: When creating an account, the system asks for the account type (savings or current), customer name, and account number is generated randomly.
  Depositing/Withdrawing funds: Allows the user to deposit or withdraw money from an account by selecting the account number and entering the amount. If withdrawing from a       CurrentAccount, it checks whether the overdraft limit is exceeded.
  Loan Application: Users can apply for a loan, and the system generates a loan ID, calculates monthly payments based on interest rate and loan term, and saves the loan information.
  Loan Payments: Users can make payments toward their loans, which updates the remaining loan balance.

File Persistence:
  The system uses CSV files (accounts.csv and loans.csv) to store and load account and loan information, ensuring that data is persisted even if the program is closed and reopened.
