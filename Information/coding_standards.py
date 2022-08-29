# Comment


x: int = 5
y: str = "rose"
z: int = 3

a: int = z * x


class User:

    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password


user: User = User("viki", "example")


def print_user(person: User):
    print(person.username)
    print(person.password)


print_user(user)


def get_greeting(name: str) -> str:
    return f"Hello, {name}"


list_of_numbers: list[int] = [5, 6, 7]

dictionary_of_values: dict = {"a": 5, "b": "hello"}
