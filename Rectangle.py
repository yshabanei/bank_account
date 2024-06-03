class Rectangle:
    """
    A class representing a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new rectangle with the given width and height.
        area(): Calculates and returns the area of the rectangle.
        perimeter(): Calculates and returns the perimeter of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Returns:
            None
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)
