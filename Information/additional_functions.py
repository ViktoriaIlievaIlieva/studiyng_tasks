

def add(a: float, b: float, c: float = 0) -> float:
    result = a + b + c
    return result


print(add(3, 4, 5))
print(add(1, 2, 3))
print(add(1, 2))


def my_cool_function(first, second, third="", fourth=0):
    pass


value = 5
my_cool_function("1", "2", fourth=value)


print("my text", "second text", sep=", ", end="")


