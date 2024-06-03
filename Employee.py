class Employee:
    def __init__(self, name: str, rights: int) -> None:
        self.name = name
        self.rights = rights

    def salary_increase(self, amount):
        self.rights += amount

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.rights}")


employee1 = Employee("Ali", 50000)
employee1.display()

employee1.salary_increase(5000)
employee1.display()
