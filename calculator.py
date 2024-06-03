import math

class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self, num1, num2):
        """Initialize the calculator with two numbers."""
        self.num1 = num1
        self.num2 = num2

    def Total(self):
        """Return the sum of the two numbers."""
        return self.num1 + self.num2

    def Subtraction(self):
        """Return the difference between the two numbers."""
        return self.num1 - self.num2

    def Multiplication(self):
        """Return the product of the two numbers."""
        return self.num1 * self.num2

    def Power(self):
        """Return the result of raising num1 to the power of num2, and vice versa."""
        return self.num1**self.num2, self.num2**self.num1

    def Root(self):
        """Return the square root of num1 and num2 separately."""
        return math.sqrt(self.num1), math.sqrt(self.num2)
    
    
    
calculator = Calculator(10, 5)


sum_result = calculator.Total()
print("جمع دو عدد: ", sum_result)


subtraction_result = calculator.Subtraction()
print("تفریق دو عدد: ", subtraction_result)


multiplication_result = calculator.Multiplication()
print("ضرب دو عدد: ", multiplication_result)


power_result = calculator.Power()
print("توان اولیه از دو عدد: ", power_result[0])
print("توان دومیه از دو عدد: ", power_result[1])


root_result = calculator.Root()
print("جذر اولیه از دو عدد: ", root_result[0])
print("جذر دومیه از دو عدد: ", root_result[1])

