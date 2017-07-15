"""

"""

magicians = ["Houdini", "Blaine", "Angel", "Dynamo"]

def make_great(magician_list):
    for num in range(0, len(magician_list)):
        magician_list[num] = "the Great " + magician_list[num]

def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

make_great(magicians)
show_magicians(magicians)
