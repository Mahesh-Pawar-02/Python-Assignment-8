# Problem Statment : Write a program which contains one class named as Numbers.  Arithmetic class contains one instance variables as Value.  
# Inside init method initialise that instance variables to the value which is accepted from user. There are four instance methods inside 
# class as ChkPrime(), ChkPerfect(), SumFactors(), Factors(). ChkPrime() method will returns true if number is prime otherwise return false. 
# ChkPerfect() method will returns true if number is perfect otherwise return false. Factors() method will display all factors of instance 
# variable. SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required. 
# After designing the above class call all instance methods by creating multiple objects

class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        return False

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

No = Numbers(int(input("Enter a number: ")))

print("Factors:", No.Factors())
print("Sum of factors:", No.SumFactors())
print("Is Prime:", No.ChkPrime())
print("Is Perfect:", No.ChkPerfect())

# Test Case : 1
# Input  : Enter a number: 10
# Output : Factors: [1, 2, 5, 10]
#          Sum of factors: 18
#          Is Prime: False
#          Is Perfect: False

# Test Case : 2
# Input  : Enter a number: 5
# Output : Factors: [1, 5]
#          Sum of factors: 6
#          Is Prime: True
#          Is Perfect: False