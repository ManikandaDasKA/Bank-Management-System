import random as r
import pandas as pd
import csv
class BankAccount:
    def __init__(self, account_number, customer_name,balance=0.0):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposit successful.")
        return self.get_balance()

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("Withdrawal successful.")
            return self.get_balance()

    def get_balance(self):
        print("Balances:",self.balance)
        return self.balance

    def display_info(self):
        print("Customer account details")
        print("Account number:",self.account_number)
        print("Customer name:",self.customer_name)
        print("Balance:",self.balance)
        q={"account_number":self.account_number,"customer_name":self.customer_name,"balance":self.balance}
        return q

class SavingsAccount(BankAccount):
    def __init__(self,account_number,customer_name,balance=0.0,interest_rate=0.0):
        super().__init__(account_number,customer_name,balance)
        self.interest_rate=interest_rate

    def calculate_interest(self, time_period):
        if time_period>0:
            interest=self.balance*(self.interest_rate/100)*time_period
            print("Interest:",interest)
            self.balance+=interest
            return interest

class CurrentAccount(BankAccount):
  def __init__(self, account_number, customer_name, balance=0.0,overdraftlimit=0.0,fee=0.0):
      super().__init__(account_number, customer_name, balance)
      self.overdraftlimit=overdraftlimit
      self.fee=fee
  def withdraw(self, amount):
      if amount>self.balance:
          if (amount-self.balance)<=self.overdraftlimit:
              self.balance=self.balance-amount-self.fee
              return super().get_balance()
          else:
              return super().get_balance()
      else:
          return super().withdraw(amount)

class Loan:
    def __init__(self,loan_id,account_number,customer_name,principal_amount,interest_rate,loan_term):
        self.loan_id=loan_id
        self.account_number=account_number
        self.customer_name=customer_name
        self.principal_amount=principal_amount
        self.interest_rate=interest_rate
        self.loan_term=loan_term

    def calculate_monthly_payment(self):
        monthly_rate=self.interest_rate/100/12
        num_payments=self.loan_term*12
        if monthly_rate==0:
            monthly_payment=self.principal_amount/num_payments
            return monthly_payment
        monthly_payment=(self.principal_amount*monthly_rate)/(1-(1+monthly_rate)**-num_payments)
        return monthly_payment
    
    def loan_info(self):
        print("Loan details")
        print("Loan id:",self.loan_id)
        print("Account number:",self.account_number)
        print("Customer name:",self.customer_name)
        print("Principal amount:",self.principal_amount)
        print("Interest rate:",self.interest_rate)
        print("Loan term:",self.loan_term)
        monthly_payment=self.calculate_monthly_payment()
        print("Monthly payment:",monthly_payment)
        e={"loan_id":self.loan_id,"account_number":self.account_number,"customer_name":self.customer_name,"principal_amount":self.principal_amount,"interest_rate":self.interest_rate,"loan_term":self.loan_term,"monthly_payment":monthly_payment}
        return e

def save_accounts(accounts,filename='accounts.csv'):
    fieldnames=accounts[0].keys()
    with open(filename,'a+',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        if file.tell()==0:
          writer.writeheader()
        writer.writerows(accounts)

def load_accounts(filename):
    accounts=[]
    with open(filename,'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            accounts.append(row)
    return accounts

def save_loans(loans,filename='loans.csv'):
    fieldnames=loans[0].keys()
    with open(filename,'a+',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        if file.tell()==0:
          writer.writeheader()
        writer.writerows(loans)

def load_loans(filename):
    loans=[]
    with open(filename,'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            loans.append(row)
    return loans

def main():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create a new bank account (savings or current)")
        print("2. Deposit funds into an account")
        print("3. Withdraw funds from an account")
        print("4. Check account balance")
        print("5. Display account information")
        print("6. Apply for a loan")
        print("7. View loan details")
        print("8. Make loan payments (update loan balance)")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_type = input("Enter account type (savings/current): ").strip().lower()
            customer_name = input("Enter customer name: ")
            if account_type=="savings":
                acc_no=["S"]
                for i in range(1,11):
                      acc_no.append(r.randint(0,9))
                acc_no="".join(map(str,acc_no))
                account_number=acc_no
                interest_rate =2.5
                balance=0.0
                print("Your interest rate will be:",interest_rate)
                s=SavingsAccount(account_number,customer_name,balance,interest_rate)
                o=[]
                t=s.display_info()
                o.append(t)
                save_accounts(o)
                print("Account created successfully.")
            elif account_type=="current":
                acc_no=["C"]
                for i in range(1,11):
                      acc_no.append(r.randint(0,9))
                acc_no="".join(map(str,acc_no))
                account_number=acc_no
                balance=0.0
                c=CurrentAccount(account_number,customer_name,balance,500,20)
                o=[]
                t=c.display_info()
                o.append(t)
                save_accounts(o)
                print("Account created successfully.")
            else:
                print("Invalid account type.")
                continue

        elif choice=='2':
            flag=0
            ac=input("Enter account number: ")
            amount=float(input("Enter amount to deposit: "))
            accounts=load_accounts("accounts.csv")
            for account in accounts:
                if account["account_number"]==ac:
                    m=BankAccount(account["account_number"],account["customer_name"],float(account["balance"]))
                    df1=pd.read_csv("accounts.csv")
                    df1.loc[df1["account_number"]==ac,"balance"]=m.deposit(amount)
                    df1.to_csv("accounts.csv",index=False)
                    flag=1
                    break
            if flag==0:
                print("Account not found.")

        elif choice=='3':
            flag=0
            ac=input("Enter account number: ")
            amount=float(input("Enter amount to withdraw: "))
            accounts=load_accounts("accounts.csv")
            df1=pd.read_csv("accounts.csv")
            for account in accounts:
                if account["account_number"]==ac:
                    if float(account["balance"])>=amount:
                        m=BankAccount(account["account_number"],account["customer_name"],float(account["balance"]))
                        df1.loc[df1["account_number"]==ac,"balance"]=m.withdraw(amount)
                        df1.to_csv("accounts.csv",index=False)
                        flag=1
                        break
                    else:
                        c=CurrentAccount(account["account_number"],account["customer_name"],float(account["balance"]),500,20)
                        h=c.withdraw(amount)
                        if h==float(account["balance"]):
                            print("Overdraft limit exceeded")
                            flag=1
                            break
                        else:
                            df1.loc[df1["account_number"]==ac,"balance"]=h
                            df1.to_csv("accounts.csv",index=False)
                            flag=1
                            break
            if flag==0:
                print("Account not found.")

        elif choice=='4':
            ac=input("Enter account number: ")
            accounts=load_accounts("accounts.csv")
            for account in accounts:
                if account["account_number"]==ac:
                    m=BankAccount(account["account_number"],account["customer_name"],float(account["balance"]))
                    m.get_balance()
                    break
            else:
                print("Account not found.")

        elif choice=='5':
              ac = input("Enter account number: ")
              accounts=load_accounts("accounts.csv")
              for account in accounts:
                  if account["account_number"]==ac:
                      m=BankAccount(account["account_number"],account["customer_name"],float(account["balance"]))
                      m.display_info()
                      break
              else:
                  print("Account not found.")

        elif choice=='6':
            flag=0
            ac = input("Enter account number: ")
            accounts=load_accounts("accounts.csv")
            for account in accounts:
                if account["account_number"]==ac:
                    Number=account["account_number"]
                    Name=account["customer_name"]
                    loan_id=[]
                    lo_id=[]
                    for i in range(0,12):
                        lo_id.append(r.randint(0,9))
                    lo_id="".join(map(str,lo_id))
                    loan_id=int(lo_id)
                    print("You loan has been approved")
                    print("Your loan id is:",loan_id)
                    print("Interest Rate will be:5.0")
                    print("Loan term will be:2")
                    principal_amount=int(input("Enter the loan amount needed:"))
                    l=Loan(loan_id,Number,Name,principal_amount,interest_rate=5.0,loan_term=2)
                    monthly_payment=l.calculate_monthly_payment()
                    print(f"Monthly payment for the loan:{monthly_payment:.2f}")
                    z=[]
                    u=l.loan_info()
                    z.append(u)
                    save_loans(z)
                    flag=1
            if flag==0:
                print("Account not found.\n")
                print("Create a new account")

        elif choice=='7':
            flag=0
            loan_id = int(input("Enter loan ID: "))
            loans=load_loans("loans.csv")
            for loan in loans:
                if int(loan["loan_id"])==loan_id:
                    g=Loan(loan["loan_id"],loan["account_number"],loan["customer_name"],int(loan["principal_amount"]),float(loan["interest_rate"]),int(loan["loan_term"]))
                    g.loan_info()
                    flag=1
                    break
            if flag==0:
              print("Loan id not found.")

        elif choice=='8':
            flag=0
            loan_id=int(input("Enter loan ID: "))
            amount=int(input("Enter loan amount to pay:"))
            loans=load_loans("loans.csv")
            for loan in loans:
                if int(loan["loan_id"])==loan_id:
                    g=Loan(loan["loan_id"],loan["account_number"],loan["customer_name"],int(loan["principal_amount"]),float(loan["interest_rate"]),int(loan["loan_term"]))
                    loan_balance=int(loan["principal_amount"])
                    loan_balance-=amount
                    df2=pd.read_csv("loans.csv")
                    df2.loc[df2["loan_id"]==loan_id,"principal_amount"]=loan_balance
                    df2.to_csv("loans.csv",index=False)
                    g.loan_info()
                    print("Loan amount paid successfully.")
                    print("Remaining loan amount:",loan_balance)
                    flag=1
                    break
            if flag==0:
                print("Loan id not found.")

        elif choice=='9':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")

if __name__ =="__main__":
    main()