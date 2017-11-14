class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a(n) " + self.cuisine_type + " style restaurant")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


restaurant1 = Restaurant("Portofino", "Italian")
restaurant2 = Restaurant("Federal Delicatessen", "American")
restaurant3 = Restaurant("Tanpopo Ramen", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
