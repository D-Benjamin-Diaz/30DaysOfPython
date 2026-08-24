# Day - 2 30DaysOfPython Challenge

"""Python Built-in functions

print(),len(), type(), int(), float(),
str(), input(), list(), dict(), min(),
max(), sum(), sorted(), open(), file(),
help(), and dir()
"""

# Variables in Python
first_name = "Asabeneh"
last_name = "Yetayeh"
country = "Finland"
city = "Helsinki"
age = 250
is_married = True
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
    "firstname": "Asabeneh",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

# Printing the values stored in the variables
print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

# Multiple variables can be declared in one line:
first_name, last_name, country, age, is_married = (
    "Asabeneh",
    "Yetayeh",
    "Helsink",
    250,
    True,
)


# You can take the input from a user using the following:
first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)

# Input is taken as a string, you might want to parse that into numbers sometimes...Worth revisiting data types:
# Different python data types
# Let's declare variables with various data types

first_name = "Asabeneh"  # str
last_name = "Yetayeh"  # str
country = "Finland"  # str
city = "Helsinki"  # str
age = 250  # int, it is not my real age, don't worry about it

# Printing out types
print(type("Asabeneh"))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({"name": "Asabeneh"}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))  # zip


# Here is how casting works in Python using the str(), the int(), the list() and float() functions:
# int to float
num_int = 10
print("num_int", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = "10.6"
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)  # Then convert the float to an integer
# print("num_int", int(num_str))  # ERRORS OUT
print("num_float", float(num_str))  # 10.6
num_int = int(num_float)
print("num_int", int(num_int))  # 10

# str to list
first_name = "Asabeneh"
print(first_name)  # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


# ---------------------------------------------------------------------------------
#                           Exercises of Day 2 below
# ---------------------------------------------------------------------------------

# ================================ LEVEL 1 ========================================

first_name = "Daniel"
last_name = "Diaz"
full_name = "Daniel Benjamin Diaz"
country = "El Salvador"
age = 23
year = 2026
is_married = False
is_light_on = True

make, model, year, mileage, double_traction = "Honda", "CRV", 2015, 200000, False

# ================================ Level 2 ========================================

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(mileage))
print(type(double_traction))

print(len(first_name))

first_name_length = len(first_name)
last_name_length = len(last_name)

print(max(first_name_length, last_name_length))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
prodcut = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

# Radius of circle is 30 meters
area_of_circle = 3.14 * 30**2
circum_of_circle = 2 * 30 * 3.14

# User Input Circle calculations:
radius = int(input("Type your radius: "))

area = 3.14 * radius**2
cirucm = 3.14 * 2 * radius

# User info
user = {
    "first_name": input("Type your first name: "),
    "last_name": input("Type your last name:"),
    "age": int(input("Type your age:")),
}

print(user)

""" HERE IS WHAT help('keywords') displays

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""
