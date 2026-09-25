# =============================== Day 14 =================================
"""
In functions are treated as a first class citizens, allowing you to
perform the following operations on functions:

    - A function can take on or more functions as parameters (Covered here)
    - A function can be returned as a result of another (Covered here)
    - A function can be modified
    - A function can be assigned to a variable

Also we are gonna be using decorator here
"""


# Functions as parameters
from functools import reduce


def sum_numbers(nums):  # a normal function
    return sum(nums)  # a sad function abusing the built-in sum function


def higher_order_function(f, lst):
    summation = f(lst)  # Summation is whatever the result of applyin f on lst is
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)


# Functions as a return value


def square(x):  # a square function
    return x**2


def cube(x):  # a cube function
    return x**3


def absolute(x):  # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


# Whatever value is passed to result, the function set up will be applied to it
result = higher_order_function("square")
print(result(3))  # 9
result = higher_order_function("cube")
print(result(3))  # 27
result = higher_order_function("absolute")
print(result(-3))  # 3


# Python Closures
"""
Python allow a nested function/loop access the outer scope of the enclosing function.
This is known as closure
"""


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


# Add_ten does not take in any parameters, but the parameter passed can be accessed by add()
closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


# Python Decorators
"""
It is a design pattern in python that allows a user to ad new functionality
to an existing object without modifying its structure. They are usually
called before the definition of a function you want to decorate
"""


# Normal function
def greeting():
    return "Welcome to Python"


def uppercase_decortor(function):
    def wrapper():
        func = function()
        make_upprcase = func.upper()
        return make_upprcase

    return wrapper


g = uppercase_decortor(greeting)
print(g())

## Decorator implementtion of this same example


def uppercase_decortor(function):
    def wrapper():
        func = function()
        make_upprcase = func.upper()
        return make_upprcase

    return wrapper


@uppercase_decortor
def greeting():
    return "Welcome to Python"


print(greeting())
# This can be useful whenever we want a function to repeat a
# Behavior every time is called. Like checking if the user is logged in


# Here is an example applying multiple decorators

"""These decorator functions are higher order functions
that take functions as parameters"""


# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


# Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator  # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return "Welcome to Python"


print(greeting())  # ['WELCOME', 'TO', 'PYTHON']


# The usage of input parameters can be splited between the function and the decorator
def decorator_with_parameters(function):  # Only uses parameter 3
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):  # Uses the first and second param
    print("I am {} {}. I love to teach.".format(first_name, last_name))


print_full_name("Asabeneh", "Yetayeh", "Finland")


# Here are some Built-in Higher Order Functions
"""
Here is where lambda functions thrive since they can be passed
as parameters for these Built-in Higher order functions
"""


# MAP - Takes a function and iterable as parameters. Returns the function applied to the iterable

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

squared = map(square, numbers)
print(list(squared))

# Here is cubing in lambda
cubed = map(lambda x: x**3, numbers)
print(list(cubed))


# FILTER - Calls a function that returns a boolean on the items of the iterable. Filters from that "condition"
def is_even(s):
    if  s%2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))


# REDUCE/FOLD - Takes a function and iterable. It returns the composition of operating all items on the iterable
def add_two(x,y):
    return x + y

total = reduce(add_two, numbers)
print(total)



# ================================= Day 14 Exercises ============================================


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

u_countries = map(lambda name: name.upper(), countries)
squared = map(lambda x: x**2, numbers)
u_names = map(lambda name: name.upper(), names)

land = filter(lambda name: name.endswith('land'), countries)
lengthy = filter(lambda name: len(name) == 6, countries)
lengthier = filter(lambda name: len(name) >= 6, countries)
e_countries = filter(lambda name: name.startswith('E'), countries)

get_string_list = map(lambda item: str(item), numbers)

total = reduce(lambda x,y: x+y, numbers)


def count_by_starting_letter(countries):
    result = {}
    for country in countries:
        letter = country[0].upper()
        result[letter] = result.get(letter, 0) + 1
    return result



