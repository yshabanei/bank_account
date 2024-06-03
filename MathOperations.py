class MathOperations:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2


def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    operations = MathOperations(number1, number2)

    sum_result = operations.add()
    difference_result = operations.sub()
    print(f"The sum of {number1} and {number2} is: {sum_result}")
    print(f"The difference between {number1} and {number2} is: {difference_result}")


if __name__ == "__main__":
    main()
