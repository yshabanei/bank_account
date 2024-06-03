from typing import List
from pprint import pprint


class User:
    all_users: List["User"] = []

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"{self.username}"


user1 = User("ttt", "reza@gmail.com", "11111")
User.all_users = []
user2 = User("ttt", "reza@gmail.com", "11111")
user3 = User("ttt", "reza@gmail.com", "11111")
pprint(User.all_users)
