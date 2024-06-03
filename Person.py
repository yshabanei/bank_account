class Person:
    category = "mammel"

    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating")

    def walk(self):
        print(f"{self.name} is walking")

    def talk(self):
        print(f"{self.name} is talking")


reza = Person("reza", 28, 180, 90)
reza.walk()
reza.talk()
reza.eat()
