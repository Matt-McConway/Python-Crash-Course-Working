num1 = input("Input number 1: ")
num2 = input("Input number 2: ")

try:
    print(str(int(num1) + int(num2)))
except:
    print("One of the inputs is not a number!")
