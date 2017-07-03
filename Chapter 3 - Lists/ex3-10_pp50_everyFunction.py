"""
3-10. Every Function: Think of something you could store in a list. For example,
      you could make a list of mountains, rivers, countries, cities, languages,
      or anything else you’d like. Write a program that creates a list
      containing these items and then uses each function introduced in this
      chapter at least once.
"""


programmingLanguages = ["HTML", "CSS", "Java", "Javascript", "Python"]

print(programmingLanguages)

print(programmingLanguages[-2])

programmingLanguages[2] = "C#"
print(programmingLanguages)

programmingLanguages.append("Java")
print(programmingLanguages)

programmingLanguages.insert(0, "Swift")
print(programmingLanguages)

del programmingLanguages[0]
print(programmingLanguages)

print(programmingLanguages.pop())
print(programmingLanguages)

programmingLanguages.remove("C#")
print(programmingLanguages)

programmingLanguages.sort()
print(programmingLanguages)

print(sorted(programmingLanguages, reverse=True))
print(programmingLanguages)

print(len(programmingLanguages))
