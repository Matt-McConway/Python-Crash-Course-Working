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

restaurant = Restaurant("Portofino", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)
restaurant.set_number_served(30)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)

