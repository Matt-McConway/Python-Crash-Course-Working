"""

"""

def build_car(manufacturer, model_name, **car_info):
    car = {}
    car["Manufacturer"] = manufacturer
    car["Model Name"] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car

car = build_car("Tesla", "S", colour="Blue", battery="100kWh")

print(car)
