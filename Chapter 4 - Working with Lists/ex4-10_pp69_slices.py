"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
      lines to the end of the program that do the following:
      •	Print the message, The first three items in the list are:.
        Then use a slice to print the first three items from that program’s
        list.
      •	Print the message, Three items from the middle of the list are:.
        Use a slice to print three items from the middle of the list.
      •	Print the message, The last three items in the list are:.
        Use a slice to print the last three items in the list.
"""
# Used code from EX 4-2:
commonAnimals = ["Dog", "Cat", "Crocodile"]

for animal in commonAnimals:
    print(animal)

print()
# Statement about each animal

for animal in commonAnimals:
    print("A " + animal + " has four legs.")
print()

# Final statement out side of loop
for animal in commonAnimals:
    print("A " + animal + " has four legs.")
print("All of these animals have four legs!")

print()
print("EX 4-10:")
commonAnimals.append("Mouse")
commonAnimals.append("Sheep")
print("The first three items from the list are: " +
      str(commonAnimals[:3]))
print("The middle three items from the list are: " +
      str(commonAnimals[1:4]))
print("The last three items from the list are: " +
      str(commonAnimals[2:]))
