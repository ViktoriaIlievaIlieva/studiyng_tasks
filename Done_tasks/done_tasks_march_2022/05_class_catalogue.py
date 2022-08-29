# Catalogue
# Create a class Catalogue. The __init__ method should accept the name of the catalogue (string).
# Each catalogue should also have an attribute called products, an empty list. The class should also have three more
# methods:
# add_product(product_name: str) - adds the product to the products' list
# get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter
# __repr__ - returns the catalogue info in the following format:
# "Items in the {name} catalogue:
# {item1}
# {item2}
# …
# {itemN}"
# The items should be sorted alphabetically in ascending order.

class Catalogue:
    def __init__(self, name: str):
        self.name: str = name
        self.products: list = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list:
        list_with_first_letter_products: list = []
        for letter in self.products:
            if letter[0] == first_letter:
                list_with_first_letter_products.append(letter)
        return list_with_first_letter_products

    def __repr__(self) -> str:
        self.products.sort()
        result = f"Items in the {self.name} catalogue:\n"
        for item in self.products:
            result += item + "\n"

        return result.strip()


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
