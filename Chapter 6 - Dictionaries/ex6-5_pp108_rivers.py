"""

"""

rivers = {"nile": "egypt",
          "waikato": "new zealand",
          "thames": "england"
         }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
