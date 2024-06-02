from random import randrange
from typing import Set


class BankAccount:
    all_account_numbers:Set[int] = set()

    def __init__(self, name:str) -> None:
        while True:
            an = randrange(10000, 100000)
            if an not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number:int = an
                break
        self.name = name
        self.balance:float = 0.0

    def display(self):
        print(f"Hi, {self.name}\nYour current balance: {self.balance:.2f}")

    def deposit(self):
        print(40 * "_")
        try:
            amount = float(input("Please enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            self.balance += amount
            self.display()
        except ValueError:
            print("Invalid amount entered. Please enter a numerical value.")

    def withdraw(self):
        print(40 * "_")
        try:
            amount = float(input("Please enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            if amount > self.balance:
                print("Insufficient Balance!")
            else:
                self.balance -= amount
            self.display()
        except ValueError:
            print("Invalid amount entered. Please enter a numerical value.")


def main():
    account1 = BankAccount("Reza")
    print(40 * "_")
    print(f"account_number: {account1.account_number}")
    print(40 * "_")
    account1.display()
    while True:
        choice = int(
            input(
                "Enter \n1 to see your balance,\n2 to deposit\n"
                "3 to withdraw, \n4 to exit.\n\t\tyour choice: "
            )
        )
        if choice == 1:
            account1.display()
        elif choice == 2:
            account1.deposit()
        elif choice == 3:
            account1.withdraw()
        elif choice == 4:
            break
        else:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
