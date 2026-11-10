class Patient: #This is the base class
    def __init__(self, name, bill_amount): #This is the constructor for the class and it initializes the name and bill amount
        self.__name = name #This makes a private attribute called name and it cannot be accessed outside the class
        self.__bill_amount = bill_amount #This makes a private attribute called bill_amount and it cannot be accessed outside the class
    def get_name(self): #This is a getter method that returns the name of the patient. It allows access to the private attribute __name from outside the class.
        return self.__name #This is a getter method that returns the name of the patient. It allows access to the private attribute __name from outside the class.
    def set_name(self, name): #This is a setter method that sets the name of the patient. It allows modification of the private attribute __name from outside the class.
        self.__name = name #This is a setter method that sets the name of the patient. It allows modification of the private attribute __name from outside the class.
    def get_bill_amount(self): #This is a getter method that returns the bill amount of the patient. It allows access to the private attribute __bill_amount from outside the class.
        return self.__bill_amount #This is a getter method that returns the bill amount of the patient. It allows access to the private attribute __bill_amount from outside the class.
    def set_bill_amount(self, bill_amount): #This is a setter method that sets the bill amount of the patient. It allows modification of the private attribute __bill_amount from outside the class.
        self.__bill_amount = bill_amount #This is a setter method that sets the bill amount of the patient. It allows modification of the private attribute __bill_amount from outside the class.
    def calculate_bill(self): #This is a method that calculates the final bill amount for the patient. It can be overridden by subclasses to provide specific billing calculations for different types of patients.v
        return self.__bill_amount #This is a method that calculates the final bill amount for the patient. It can be overridden by subclasses to provide specific billing calculations for different types of patients. 
    def display_patient_type(self): #This is a method that displays the type of patient. It can be overridden by subclasses to provide specific patient types for different types of patients.
        print("Patient type: Regular Patient") #This is a method that displays the type of patient. It can be overridden by subclasses to provide specific patient types for different types of patients.
class Senior_Patient(Patient): #This defines a new class named Senior_Patient and it inherits from the Patient class
    def calculate_bill(self): #This is a method that calculates the final bill amount for the senior patient. It overrides the calculate_bill method of the parent class Patient to provide a specific billing calculation for senior patients.
        return self.get_bill_amount() * 0.8 #This is a method that calculates the final bill amount for the senior patient. It overrides the calculate_bill method of the parent class Patient to provide a specific billing calculation for senior patients.
    def display_patient_type(self): #This is a method that displays the type of patient. It overrides the display_patient_type method of the parent class Patient to provide a specific patient type for senior patients.
        print("Patient type: Senior Citizen") #This is a method that displays the type of patient. It overrides the display_patient_type method of the parent class Patient to provide a specific patient type for senior patients.
class PhilHealth_Patient(Patient): #This defines a new class named PhilHealth_Patient and it inherits from the Patient class
    def calculate_bill(self): #This is a method that calculates the final bill amount for the PhilHealth patient. It overrides the calculate_bill method of the parent class Patient to provide a specific billing calculation for PhilHealth patients.
        return self.get_bill_amount() * 0.85 #This is a method that calculates the final bill amount for the PhilHealth patient. It overrides the calculate_bill method of the parent class Patient to provide a specific billing calculation for PhilHealth patients.
    def display_patient_type(self): #This is a method that displays the type of patient. It overrides the display_patient_type method of the parent class Patient to provide a specific patient type for PhilHealth patients.
        print("Patient type: PhilHealth Member") #This is a method that displays the type of patient. It overrides the display_patient_type method of the parent class Patient to provide a specific patient type for PhilHealth patients.

        
print("Hospital Billing System")
print("-----------------------")
#Patient 1 - Regular Patient
p1 = Patient("John Dela Cruz", 15000.00)
print(f"Patient Name: {p1.get_name()}")
p1.display_patient_type()
print(f"Original Bill: ₱{p1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p1.calculate_bill():,.2f}")
print()
#Patient 2 - Senior Patient
p2 = Senior_Patient("Maria Santos", 15000.00)
print(f"Patient Name: {p2.get_name()}")
p2.display_patient_type()
print(f"Original Bill: ₱{p2.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p2.calculate_bill():,.2f}")
print()
#Patient 3 - PhilHealth Patient
p3 = PhilHealth_Patient("Pedro Reyes", 15000.00)
print(f"Patient Name: {p3.get_name()}")
p3.display_patient_type()
print(f"Original Bill: ₱{p3.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")