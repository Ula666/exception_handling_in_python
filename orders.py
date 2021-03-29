# Dealing with files and error/exception handling

# There is a built in method in Python called open("") it takes a string

# file = open("orders.text") # looks for the file called orders.txt

try:
    file = open("orders.text")
    print("File was found")
except FileNotFoundError as errmsg:
    print(f"the above block of code wasn't executed {errmsg}")
    # raise
finally:
    print("Your task is to read the data and display as a list")

# second iteration:


try:
    file = open("orders.text")
    print("File was found")
    print(file.read())
except FileNotFoundError as errmsg:
    print(errmsg)
finally:
    print("Your task is to read the data and display as a list")

# 3rd iteration
# Create a function to do the same job DRY
def read_file():
    file = open("orders.text")
    print(file.read())

# 4th interation

