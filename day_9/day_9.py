# ======================================= DAY 9: Conditionals =================================

"""
If the processing logic requires so, Python's sequential flow of execution can
can be altered in two ways:

1. Conditional Execution -> a block is executed if certain condition is True

2. Repetitive Execution -> a block is executed while a certain condition is True
"""

# If Statement -> Executes if a condition is met, otherwise ignores
a = 3
if a > 0:
    print("The variable a is a positive number")

# If Else Statement -> Executes if a condition is met,
# otherwise executes another block (avoids ignoring)

if a < 0:
    print("VAriable a is a negative number")
else:
    print("Variable a is a positive number")


# If Elif Else -> When having more than one options for
#  a condition. A non binary situation, you can use this
if a > 0:
    print("Variable a is a positive number")
elif a < 0:
    print("varibale a is a negative number")
else:
    print("Varibale a is zero")


# Short Hand -> An easier way to write if else statement
print('A is a positive number') if a > 0 else print('A is a negative number')

# Conditions can be nested, thet means inside other conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# --------- If Condtions and Logical Operators -------------------
# Using and
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# Using Or
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


# ================================== Exercises Day 9 =================================

age = int(input('Enter your age: '))
print('Old enough to drive') if age >= 18 else print(f'You need {18-age} years to learn to drive')

if age > 23:
    if age - 23 == 1:
        print('You are a year older than me')
    print(f'You are {age - 23} years older than me')
else:
    if 23 - age == 1:
        print('You are a year younger than me')
    print(f'You are {23 - age} years younger than me')


a = int(input('Enter the number A: '))
b = int(input('Enter the number B: '))

if a > b:
    print(f'Number A ({a}) is greater than B ({b})')
elif a < b:
    print(f'Number A ({a}) is less than B ({b})')
else:
    print('Both numbers are equal')


# GRADING

grade = int(input('Enter the grade: '))

if grade > 100 or grade < 0:
    print('That\'s not right!')
elif grade <= 100 and grade >= 90:
    print('You get an A')
elif grade >= 80:
    print('You get a B')
elif grade >= 70:
    print('You get a C')
elif grade >= 60:
    print('You get a D')
else:
    print('YOU FAILED!')


fall = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring= ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input('Enter a month! ').lower().capitalize()

if month in fall:
    print('Fall')
elif month in winter:
    print('Winter')
elif month in spring:
    print('Spring')
else:
    print('Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Give me a Fruit')

if not fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exists')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}



