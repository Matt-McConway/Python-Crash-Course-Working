"""

"""

magicians = ["Houdini", "Blaine", "Angel", "Dynamo"]
great_magicians = []

def make_great(magician_list, great_magicians):
    for magician in magician_list:
        great_magicians.append("the Great " + magician)
    return great_magicians

def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

great_magicians = make_great(magicians[:], great_magicians)
show_magicians(magicians)
print("")
show_magicians(great_magicians)
