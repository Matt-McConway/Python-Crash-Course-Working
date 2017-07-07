"""

"""

harvey = {"kind": "cat",
          "owner": "matt"
         }
loki = {"kind": "husky",
          "owner": "gretchen"
         }
ice = {"kind": "sheep dog",
          "owner": "tom"
         }

pets = [harvey, loki, ice]

for pet in pets:
    print(pet['kind'].title())
    print(pet['owner'].title() + "\n")
