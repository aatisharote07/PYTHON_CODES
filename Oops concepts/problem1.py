"""
Q-2: Bank Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.
"""
class bank:
    def __init__(self,name,acc_no,balance):
        self.__name = name
        self.__acc_no = acc_no
        self.__balance = balance

    def display(self):
        print(f"Account number:{self.__acc_no}")
        print(f"Account name:{self.__name}")
        print(f"Account balance:{self.__balance}$")
    def deposit(self,amount):
        self.__balance = self.__balance + amount
    def withdrawl(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance = self.__balance - amount
            reduction = self.__bankFees()
            self.__balance = self.__balance - reduction   

    def __bankFees(self):
        return 0.05 *    self.__balance   
cust = bank("Aatish",131232,525125)
cust.deposit(500)
cust.withdrawl(100)
cust.display()    
        