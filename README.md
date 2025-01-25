## Bank Management System 
This bank management system allows customers to interact with there bank accounts and loan services. It allows the creation of bank accounts (both savings and current), depositing and withdrawing funds, checking balances, displaying account information, applying for loans, making loan payments, and viewing loan details. The system uses Python classes to model different components and functionalities.
 
#### Imports:
 •	random: Used to generate random account and loan IDs.

 •	pandas: A data manipulation library used to read, modify, and save data from/to CSV files.

 •	csv: Standard Python library to read and write CSV files, used for saving and loading account and loan data.

#### Classes:
1.	BankAccount Class:
  ##### o	Has methods for depositing, withdrawing, getting balance, and displaying account information.

  ##### o	When a deposit or withdrawal happens, the balance is updated.

3.	SavingsAccount Class:
  ###### o	Inherits from BankAccount.

  ###### o	Adds an interest rate and a method to calculate interest.
 
  ###### o	When interest is calculated, it's added to the balance.

5.	CurrentAccount Class:
 ###### o	Also inherits from BankAccount.

 ###### o	Adds features for an overdraft limit and withdrawal fee.
 
 ###### o	It overrides the withdraw method to handle withdrawals that exceed the balance but remain within the overdraft limit.

7.	Loan Class:
 ###### o	Contains information like loan ID, account number, principal amount, interest rate, and loan term.

 ###### o	It calculates monthly payments based on the loan parameters.

#### Functions:
1.	save_accounts: Saves account details to a CSV file.
2.	load_accounts: Loads accounts from a CSV file.
3.	save_loans: Saves loan details to a CSV file.
4.	load_loans: Loads loan details from a CSV file.

#### Main Function:
The main() function provides a user interface in the form of a console menu. Users can choose different options such as creating accounts, depositing funds, withdrawing funds, checking balances, and applying for loans. The system interacts with CSV files to persist account and loan information.

#### File Persistence:
•	The system uses CSV files (accounts.csv and loans.csv) to store and load account and loan information, ensuring that data is persisted even if the program is closed and reopened.

