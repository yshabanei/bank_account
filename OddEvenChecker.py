class OddEvenChecker:
    def __init__(self, num: int):
        self.num = num

    def is_odd(self):
        return self.num % 2 != 0

    def is_even(self):
        return self.num % 2 == 0


def main():
    num = int(input("Please enter the number: "))

    checker = OddEvenChecker(num)
    is_even = checker.is_even()
    is_odd = checker.is_odd()

    if is_even:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")


if __name__ == "__main__":
    main()
