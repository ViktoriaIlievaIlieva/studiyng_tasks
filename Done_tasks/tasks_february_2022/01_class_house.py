# Create a class House with attributes (types are just for your information):
# area : float
# price_per_square_m : float
# address : string
# room_count : integer

# The constructor should take all the required attributes from its brackets

# Create a function in House called get_total_price that will return the area multiplied by the price per square m

# Create two House variables with values of your choice then print for each house the address and total price.
# Example:
# Osogovo str. #64 - 150000.0


class House:
    def __init__(self, area, price_per_square_m, address, room_count ):
        self.area = area
        self.price_per_square_m = price_per_square_m
        self.address = address
        self.room_count = room_count

    def get_total_price (self):
        total_price = self.area * self.price_per_square_m
        return total_price


house_1 = House(86.67, 22.50, "ul Osogovo 66", 3)
final_price = house_1.get_total_price()
print(house_1.address, "-", final_price)
