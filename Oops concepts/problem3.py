"""
Q-3:Computation class
Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
"""
class computation:
    def __init__ (self):
        pass
    def factorial(self, n):
        j = 1
        for i in range(1,n+1):
            j = j * i
        return j 
    def naturalSum(self,n):
        j = 1
        for i in range(1,n+1):
            j = j + i
        return j
    def testPrime(self,n):
        j = 0
        for i in range(1,n+1):
            if n % i == 0:
                j += 1
        if j == 2 : 
            return True
        else: 
            False