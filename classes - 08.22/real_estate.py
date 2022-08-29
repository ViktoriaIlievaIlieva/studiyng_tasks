#
# Understand method override first!
#
# A house will be characterized by indoor area and outdoor area size as well as room count and amount of floors that it has.
# An apartment will be characterized by indoor area, room count and on which floor it is from the building.
# Both of them should have a method for getting the total indoor an outdoor area
#
# Create a separate function that is given either a house or an apartment and a price per square meter.
# It should then print out the price for the total area of the estate by multiplying the area with the price.
#
# Create the classes so that you reuse as much code as possible. Not all attributes need to be used in this task.
#

class Building:
    def __init__(self, indoor_area, room_count):
        self.indoor_area = indoor_area
        self.room_count = room_count

    def get_area(self):
        return self.indoor_area


class House(Building):
    def __init__(self, indoor_area, outdoor_area, room_count, num_floors):
        super().__init__(indoor_area, room_count)
        self.outdoor_area = outdoor_area
        self.num_floors = num_floors

    def get_area(self):
        area = self.outdoor_area + self.indoor_area

        return area


class Apartment(Building):
    def __init__(self, indoor_area, room_count, floor):
        super().__init__(indoor_area, room_count)
        self.floor = floor


def price_property(price, building: Building):
    area = building.get_area()
    final_price = area * price

    return final_price


apartment = Apartment(50, 3, 5)
house = House(60, 100, 4, 2)

price_property(100, apartment)
price_property(10, house)
