class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " is a(n) " + self.cuisine_type + " style restaurant")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, stand_name, cuisine_type="Ice Cream", number_served=0):
        super().__init__(stand_name, cuisine_type, number_served)
        self.flavours = ["Vanilla", "Mint Choc Chip", "Caramel", "Licorice"]

    def display_flavours(self):
        print("Flavours: ")
        for flavour in self.flavours:
            print(flavour)

myStand = IceCreamStand("Matt's Icecream")

myStand.display_flavours()
myStand.describe_restaurant()
myStand.open_restaurant()
myStand.increment_number_served(1)