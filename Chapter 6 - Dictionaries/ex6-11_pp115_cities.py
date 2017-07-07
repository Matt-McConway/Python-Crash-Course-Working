"""

"""

cities = {"Auckland": {"Country": "New Zealand", "population": 1300000,
            "fact": "Originally the capital"},
          "Wellington": {"Country": "New Zealand", "population": 300000,
                      "fact": "Currently the capital"},
          "Dunedin": {"Country": "New Zealand", "population": 120000,
                      "fact": "Largest city in Otago"}
         }

for city, fact in cities.items():
    print(city + ":")
    for key, value in fact.items():
        print(key + ": " + str(value))
    print("\n")
