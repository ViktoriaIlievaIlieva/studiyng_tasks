# ⦁	Плод или зеленчук
# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# ⦁	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# ⦁	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# ⦁	Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.

product: str = input()

list_with_fruit: list = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
list_with_vegetable: list = ["tomato", "cucumber", "pepper", "carrot"]

if product in list_with_fruit:
    print("fruit")
elif product in list_with_vegetable:
    print("vegetable")
else:
    print("unknown")


