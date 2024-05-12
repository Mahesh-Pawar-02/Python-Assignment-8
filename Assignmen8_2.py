# Problem Statement : Write a program which contains one class named as BankAccount.  BankAccount class contains two instance variables as
# Name & Amount. That class contains one class variable as ROI which is initialise to 10.5. Inside init method initialise all name and amount
# variables by accepting the values from user. There are Four instance methods inside class as Display(), Deposit(), Withdraw(), 
# CalculateIntrest(). Deposit() method will accept the amount from user and add that value in class instance variable Amount. 
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount. 
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI. 
# And Display() method will display value of all the instance variables as Name and Amount. 
# After designing the above class call all instance methods by creating multiple objects. 

class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter name: ")
        self.Amount = float(input("Enter amount: "))

    def Display(self):
        print("Name:", self.Name)
        print("Amount:", self.Amount)

    def Deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + amount

    def Withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.Amount:
            print("Insufficient balance!")
        else:
            self.Amount -= amount

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest calculated:", interest)
        self.Amount = self.Amount + interest

acc1 = BankAccount()
acc1.Display()
acc1.Deposit()
acc1.Display()
acc1.Withdraw()
acc1.Display()
acc1.CalculateInterest()
acc1.Display()

# Test Cases using some inputes : 

# Enter name: Mahesh
# Enter amount: 1000
# Name: Mahesh
# Amount: 1000.0
# Enter amount to deposit: 0
# Name: Mahesh
# Amount: 1000.0
# Enter amount to withdraw: 700
# Name: Mahesh
# Amount: 300.0
# Interest calculated: 31.5
# Name: Mahesh
# Amount: 331.5