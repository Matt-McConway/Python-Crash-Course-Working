"""
3-11. Intentional Error: If you haven’t received an index error in one of your
      programs yet, try to make one happen. Change an index in one of your
      programs to produce an index error. Make sure you correct the error
      before closing the program.
"""

# Code from ex3-3_pp40_yourOwnList.py

statement = "I like cars. I would love to own a "
cars = ["Tesla Model S", "Tesla Model X", "Audi RS 7", "Toyota Hilux"]

print(statement + cars[0])
print(statement + cars[1])
print(statement + cars[2])
print(statement + cars[3])

print(statement + cars[4])
# Error causing statement. This is because there are
# only 4 elements in the list, so by accessing index
# 4 (element 5), an index error occurs. This is
# because the index is out of range.
