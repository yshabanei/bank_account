import math


class Circle:
    PI = math.pi

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return self.radius**2 * Circle.PI

    def perimeter(self) -> float:
        return 2 * Circle.PI * self.radius


def main():
    radius = float(input("Please enter the radius of the circle: "))

    circle = Circle(radius)

    area = circle.area()
    perimeter = circle.perimeter()

    print(f"Area of the circle: {area}")
    print(f"Perimeter of the circle: {perimeter}")


if __name__ == "__main__":
    main()
