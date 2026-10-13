#code
class BankAccount:
    def __init__(self, account_number: int, balance: float): #This triggers the attributes once a class is made
        self.set_account_number(account_number) #This is attribute 1
        self.__balance = float(balance) #This is attribute 2
        print("Account 1")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}\n")
        
    def set_account_number(self, account_number: int): #This defines the administrator for the account number
        self.__account_number = account_number
        
    def set_balance(self, balance: float): #This defines the administrator for the balance
        print(f"Update balance to {balance}")
        if balance < 0:
            print("Balance must not be a negative number") #This issues a warning if the user enters a negative number for the balance
        else:
            self.__balance = float(balance)
            
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}\n")
        
    @property #The @property decorator is used to define a method as a property, allowing it to be accessed like an attribute.
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
 
#This is the Bank Account of Account 1   
a1 = BankAccount(16167, 1000.00)
a1.set_balance(126)
a1.set_balance(-114)
        