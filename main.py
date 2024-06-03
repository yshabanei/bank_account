from random import randrange
from typing import Set


class BankAccount:
    """
    A class representing a bank account with a unique account number, a name, and a balance.

    Attributes:
        all_account_numbers (Set[int]): A set of all generated account numbers.
        account_number (int): A unique account number for the bank account.
        name (str): The name of the account holder.
        balance (float): The current balance of the account.

    Methods:
        __init__(self, name: str) -> None: Initializes a new bank account with a unique account number and the given name.
        display(self) -> None: Displays the current balance of the account.
        deposit(self) -> None: Allows the user to deposit an amount into the account.
        withdraw(self) -> None: Allows the user to withdraw an amount from the account.
    """

    all_account_numbers: Set[int] = set()

    def __init__(self, name: str) -> None:
        """
        Initializes a new bank account with a unique account number and the given name.

        Args:
            name (str): The name of the account holder.

        Returns:
            None
        """
        while True:
            an = randrange(10000, 100000)
            if an not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number: int = an
                break
        self.name = name
        self.balance: float = 0.0

    def display(self) -> None:
        """
        Displays the current balance of the account.

        Args:
            None

        Returns:
            None
        """
        print(f"Hi, {self.name}\nYour current balance: {self.balance:.2f}")

    def deposit(self) -> None:
        """
        Allows the user to deposit an amount into the account.

        Args:
            None

        Returns:
            None
        """
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

    def withdraw(self) -> None:
        """
        Allows the user to withdraw an amount from the account.

        Args:
            None

        Returns:
            None
        """
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
