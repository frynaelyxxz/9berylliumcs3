#code
class BankAccount: #dito ginagawa ang template para makacreate ng account objects
    def __init__(self, account_number: int, balance: float): #Ipinapakita nito ang mga details that you need sa screen to know if the data ay nainput na
        self.set_account_number(account_number) #This is attribute 1
        self.__balance = float(balance) #This is attribute 2
        print("Account 1")#this prints "account 1"
        print(f"Account Number: {self.__account_number}") #this prints "Account number"
        print(f"Balance: {self.__balance:.2f}\n") #this prints the balance
        
    def set_account_number(self, account_number: int): #This defines the setter for the account number
        self.__account_number = account_number #The "__" makes the variable private para maprotect ung data sa loob
        
    def set_balance(self, balance: float): #This defines the setter for the balance
        print(f"Update balance to {balance}")#Dito lumalabas ang data kapag inuupdate ng user ang balance sa bank account
        if balance < 0: #if mas maliit sa 0 ung number ibig sabihin nito ay negative ung number which will cause an error
            print("Balance must not be a negative number") #This issues a warning if the user enters a negative number for the balance dahil it will be an error since bawal magnegative ung balance
        else: #if hindi negative ung number na ininput for the balance it will proceed to the next line
            self.__balance = float(balance)#dito magshshow yung updated na balance
            
        print(f"Account Number: {self.__account_number}") #this prints the account number of the user
        print(f"Balance: {self.__balance:.2f}\n") #this prints the updated balance nung account and ung ":.2f" ay para magkaron ng two decimal places like "126.00" instead na "126"
        
    @property #The @property decorator is used to define a method as a property, allowing it to be accessed like an attribute.
    def account_number(self):#This defines the getter method para dun sa account number
        return self.__account_number #binabalik nito ung value as per the word return means and since naka"__" siya edi it means that its private and na wala makakaedit nung value outside the class
    
    @property #This is a decorator na parang "shortcut" since dahil sa @property hindi mo na need na maglagay ng "()" para macheck yung money compared sa walang @property na need mo pa magtype ng "()"
    def balance(self): #This defines the getter method para sa balance nung bank account
        return self.__balance #this returns the value so binibigay nito ung balance na asa bank account
 
#This is the Bank Account of Account 1   
a1 = BankAccount(16167, 1000.00) #This creates a new account object named a1
a1.set_balance(126) # This updates the balance to 126 and since the number 126 is positive it will update the balance to "126.00"
a1.set_balance(-114) # This tries to update the balance to -114 which is a negative value so magpapalabas siya ng message na magsasabi na dapat ang balance ay hindi negative number
        
