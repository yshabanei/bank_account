class Book:
    """
    A class representing a book with its title, author, and publication year.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.

    Methods:
        __init__(self, title: str, author: str, year: int) -> None:
            Initialize a new Book instance with the given title, author, and year.

        display_info(self) -> None:
            Display the title, author, and year of the book.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Initialize a new Book instance with the given title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.

        Returns:
            None
        """
        self.title = title
        self.author = author
        self.year = year

    def display_info(self) -> None:
        """
        Display the title, author, and year of the book.

        Args:
            None

        Returns:
            None
        """
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}")
