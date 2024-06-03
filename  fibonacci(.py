class Fibonacci:
    def __init__(self, n: int):
        self.n = n

    def fibonacci(self, num1: int, num2: int):
        fib_list = []
        for _ in range(self.n):
            fib_list.append(num1)
            num1, num2 = num2, num1 + num2
        return fib_list


def main():
    n = int(input("تعداد اعداد دنباله‌ی فیبوناچی را وارد کنید: "))
    fib = Fibonacci(n)
    result = fib.fibonacci(0, 1)
    print(f"اعداد دنباله‌ی فیبوناچی: {result}")


if __name__ == "__main__":
    main()
