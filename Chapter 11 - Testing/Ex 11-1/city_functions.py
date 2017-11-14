def city_country(city, country, population=""):
    if population:
        return city + ", " + country + " - population " + population
    else:
        return city + ", " + country