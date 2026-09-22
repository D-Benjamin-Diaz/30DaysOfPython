# ====================================== DAY 12: Modules ===================================

"""
A module is a file containing a set of codes or a set of functions
which can be included to an application. It may contain variables
functions or a big code base
"""

# To use its contents, you just use the 'import <module>' expressions

"""
If you just want to import certain functions and certain variables
you change the expression to something like:

from <module> import <function, function, ...>
"""

from mateben import square

print(square(3))  # Should return 9

"""
Modules may have a longer name, and you might want to refer to them
differently in your code. To do this you do as follow:
"""

from numpy import bitwise_left_shift as bls

print(bls(58))


# ============================== Built in Modules ==================================

# OS Module
"""'
Used to perform many operating system tasks
"""
import os

# Create directory
os.mkdir("directory_name")

# Changing the current directory
os.chdir("path")

# Getting current working directory
os.getcwd()

# Remove Direcotry
os.rmdir()


# Sys module
"""
Provides functions and variables used to manipulate different 
parts of the Python runtime environment
"""
import sys

# Returning a list of command line arguments passed to a Python script
print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2]))
# sys.argv[0] is the file name... in this case is day_12.py

# To exit sys
sys.exit()

# To know the largest integer variable it takes
sys.maxsize

# To know environment path
sys.path

# To know the version of python you are using
sys.version


# Statistics Module
"""
Provides functions for mathematical statistics of numeric data
"""
from statistics import *  # Importing all the statistics functions

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))  # Standard deviation


# Math Modules
"""
Module that contains many mathematical operations and constants
"""
import math

print(math.pi)  # Pi constant
print(math.sqrt(2))  # Square root
print(math.pow(2, 3))  # Exponential 2^3
print(math.floor(9.81))  # Round down
print(math.ceil(9.81))  # Round up
print(math.log10(100))  # Log with base 10

# These may display the available functions in the module
help(math)
dir(math)


# Strign Module
"""
Is a useful module for many purposes...
"""
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


# Random Module
"""
Gives us a random number between 0 and 0.9999 or a random
number in a defined range of integers
"""
from random import random, randint

print(random())
print(randint(2, 40))


# ============================ Exercises: Day 12 ====================================


def random_user_id():

    pool = string.ascii_letters + string.digits
    pswd = ""

    for i in range(6):
        pswd = pswd + pool[randint(0, len(pool))]

    return pswd


def user_id_gen_by_user():
    length = int(input("How long should the IDs be? "))
    number = int(input("How many IDs do you need?"))

    pool = string.ascii_letters + string.digits

    for i in range(number):
        pswd = ""
        for j in range(length):
            pswd = pswd + pool[randint(0, len(pool))]
        print(pswd)
    return


def rgb_color_gen():
    return f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})"


def generate_hex():
    pool = string.digits + "ABCDEF"
    hexa = ""
    for i in range(6):
        hexa = hexa + pool[randint(0, len(pool))]

    return "#" + hexa


def list_of_hexa(num=5):
    ls = []
    for i in range(num):
        ls.append(generate_hex())
    return


def list_of_rgb(num=5):
    ls = []
    for i in range(num):
        ls.append(rgb_color_gen())
    return


def shuffle_lisr(ls: list):

    shuffled = []

    while len(ls) != 0:
        if len(ls) == 1:
            shuffled.append(ls.pop(0))
        else:
            shuffled.append(ls.pop(randint(0, len(ls))))

    return shuffled


def seven_numbers():
    numbers = set()

    while len(numbers) != 7:
        number = randint(0, 9)

        if number not in numbers:
            numbers.add(number)

    return list(numbers)
