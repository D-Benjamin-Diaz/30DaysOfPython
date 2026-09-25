# =================================== Day 13: List Comprehension =========================
"""
Is a compact way of creating a list from a sequence.
It is a short way to create a new list. even quicker
than processing a list using a for loop
"""

# One way
language = "Python"
lst = list(language)  # changing the string to list
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']


# Now using numbers we have
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


# To make things better, you can even add conditionals in the list comprehension expression
# Generating even numbers
even_numbers = [
    i for i in range(21) if i % 2 == 0
]  # to generate even numbers list in range 0 to 21
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [
    i for i in range(21) if i % 2 != 0
]  # to generate odd numbers in range 0 to 21
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# =========== LAMBDA FUCNTIONS =====================
"""
Is a small anonymous function. It can take any number of arguments,
but can only have one expression. They are helpful when writing 
functions inside of another function
"""


def add_numbers(a, b):
    return a + b


print(add_numbers(3, 4))

# Now this can be written into a lambda expression:
addition = lambda a, b: a + b
print(addition(2, 7))


# Here is a self invoking lambda
(lambda a, b: a + b)(
    2, 5
)  # -> must be encapsulated on a print to display result in console


# Here is a Lambda function inside a regular function
def power(x):
    return lambda n: x**n


cube = power(2)(3)  # The first parenthesis is for the x, the second for the n in lambda


# ============================= Exercises Day 13 =====================================

numbers = [-4, -3, -2, -1, 0, 1, 2, 4, 6]
filtered = [i for i in numbers if i < 1]
print(filtered)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for r in list_of_lists for n in r]
print(flat)

powers = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(powers)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

flattened = [
    [country.upper(), country[:3].upper(), city.upper()]
    for pair in countries
    for country, city in pair
]
print(flattened)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

dictionaries = [
    {"country": country.upper(), "city": city.upper()}
    for pair in countries
    for country, city in pair
]


names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

full_names = [first + last for pair in names for first, last in pair]

slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
