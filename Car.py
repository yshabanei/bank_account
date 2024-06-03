class Car:
    """
    A class representing a car with its brand, model, and year.

    Attributes:
        Brand (str): The car's brand.
        Model (str): The car's model.
        Year (int): The car's year of manufacture.

    Methods:
        __init__(self, Brand, Model, Year): Initializes a new car object.
        get_info(self): Returns a string containing the car's information.
    """

    def __init__(self, Brand, Model, Year):
        """
        Initializes a new car object.

        Args:
            Brand (str): The car's brand.
            Model (str): The car's model.
            Year (int): The car's year of manufacture.

        Returns:
            None
        """
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
