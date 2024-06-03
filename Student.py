class Student:
    """
    A class representing a student with a name, age, and grades.

    Attributes:
        name (str): The student's name.
        age (int): The student's age.
        grades (list): A list of the student's grades.

    Methods:
        __init__(self, name: str, age: int): Initializes a new student object.
        add_grade(self, grade: int): Adds a new grade to the student's grades list.
        calculate_average(self) -> float: Calculates the average of the student's grades.
    """

    def __init__(self, name: str, age: int):
        """
        Initializes a new student object.

        Args:
            name (str): The student's name.
            age (int): The student's age.

        Returns:
            None
        """
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade: int):
        """
        Adds a new grade to the student's grades list.

        Args:
            grade (int): The grade to be added.

        Returns:
            None
        """
        self.grades.append(grade)

    def calculate_average(self) -> float:
        """
        Calculates the average of the student's grades.

        Returns:
            float: The average of the student's grades.
        """
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
