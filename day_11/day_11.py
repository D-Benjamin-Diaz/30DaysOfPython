# ============================= Day 11: Functions =========================

"""
A function is a reusable block of code designed  to perform a task.
Use de 'def' keyword to define a function in Python.

The block of code will only run whenever the function is invoked/called
"""

# Functions without parameters


def generate_full_name():
    first = "Daniel"
    last = "Diaz"
    space = " "
    full = first + space + last
    print(full)


generate_full_name()  # Calling the function


# Returning a Value

"""
Functions return a value using the 'return' statement.
If there is no return statement, then it returns None.
From now, the function returns a value that can be printed.
We no longer have to print the value inside the function.
What's better is that functions can return any datatype!
"""

# Rewriting the function to return a value we get:


def generate_name():
    first = "Benjamin"
    last = "Diaz"
    space = " "
    full = first + space + last
    return full


print(generate_name)


# Functions with parameters

"""
Functions may get multiple datatypes passed as parameters.
When calling a function we must pass the parameters in the order
they are written in the function declaration
"""


def area_of_circle(radius):
    PI = 3.14
    return PI * radius**2


area_of_circle(10)  # Prints the area of a circle with radius 10


def calculate_weight(mass, grav_accel):
    return str(mass * grav_accel) + " N"


# Passing Arguments with key and value

"""
By doing this we force the parameters to be used where we want them to be used.
Therefore, there is no need to pass them in order as long as they are being
called properly inside the code block. Here is how to call a function using
Arguments with key and value
"""

calculate_weight(grav_accel=9.81, mass=180)  # Order has been reversed


# Functions with Default Parameters
"""
If we forget to pass the values to parameters, we can design our
function to have default values to use in case we or the user forgets
to declare them when calling the function.
"""


def adding_vectors(v1=[1, 1], v2=[5, 4]):  # Returns [6,5] y default
    if len(v1) != len(v2):
        print("Can't add vectors of diferent dimensions")
        return

    vec = []
    for i in range(len(v1)):
        vec.append(v1[i] + v2[i])

    return vec


# Arbitrary number of Parameters
"""
WE may fnd situations in which we don't know how many parameters the user will
need to pass. One example is the sum function from excel. How does it know
how many cells/numbers are we adding? It doesn't!!

Use a * before the argument in order to say those are arbitrary
"""


def sum_all(*numbers):  # *args
    total = 0
    for num in numbers:
        total += num

    return total


# Dictionary unpacking - **kargs
"""
We can write a function where we allow the user to define what the
name of the parameter is and its value. This is done by passing the
parameter using ** on the function declaration. Then the function will
treat it as a dictionary
"""


def greet(**kwargs):
    print(kwargs)


greet(name="Juan", last="Perez", age=30)

"""
Now if that operator is used on the function call, that means
that we are telling the function to unpack the dictionary first and
treat its key and values as parameter names and values
"""


def greeting(name, age):  # The parameters are defined!!
    print(f"{name} is {age} years old")


info = {"name": "Alice", "age": 30}
greet(**info)
# Output: Alice is 30 years old


# Function as a parameter of another functio - FUNCTIONAL PROGRAMMING!!!!
"""
This is the basis of functional programming which is allowing functions to
be passed as parameters of other function. Where the passed function is
applied by the other function during the other function's execution
"""


def square_number(n):
    return n**n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27

# Remember - Filtering, Mapping and Sorting??


# ================================ Execrises: LEVEL 1 ===============================


def add_two_numbers(n1, n2):
    return n1 + n2


def add_all_nums(*args):
    total = 0
    for num in args:
        if type(num) != int:
            print("Can't add non-integers")
            return
        total += num

    return total


def c_to_f(celsius=0):
    return (celsius * 9 / 5) + 32


def check_season(month="August"):
    Fall = ["September", "October", "November"]
    Winter = ["December", "January", "February"]
    Spring = ["March", "April", "May"]
    Summer = ["June", "July", "August"]

    if month in Fall:
        return "Fall"
    elif month in Winter:
        return "Winter"
    elif month in Spring:
        return "Spring"
    elif month in Summer:
        return "Summer"
    else:
        return "Something went wrong!!! Try Again"


def solve_quadratic(a, b, c):
    aux = (b**2) - 4 * a * c
    rooted = aux ** (1 / 2)
    root_1 = (-b + rooted) / (2 * a)
    root_2 = (-b - rooted) / (2 * a)
    return root_1, root_2


def print_list(list):
    for i in list:
        print(i)
    return


def reverse_list(list):
    reversed_list = []

    for i in range(len(list), 0, -1):
        reversed_list.append(i)
    return reversed_list


def capitalize_items(list):
    capitalized = []
    for i in list:
        i = str(i)
        capitalized.append(i[0].upper())
    return


def sum_of_all(n):
    total = n
    for i in range(n):
        total += i
    return total


def sum_of_evens(n):
    if n % 2 == 0:
        total = n
    else:
        total = 0

    for i in range(n):
        if i % 2 == 1:
            total += i
    return


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_empty(item):
    return len(item) == 0


def calculate_mean(*args):
    return sum_of_all(args) / len(args)


def calculate_median(*args):

    sorted_nubmbers = sorted(args)
    size = len(args)

    if len(sorted_nubmbers) % 2 == 0:
        return (sorted_nubmbers[size // 2] + sorted_nubmbers[size // 2 + 1]) / 2
    else:
        return sorted_nubmbers[size // 2]


def calculate_mode(*args):

    count = {}

    for arg in args:
        if not arg in count.keys():
            count[arg] = 1
        else:
            count[arg] = count[arg] + 1

    max = [0, 0]

    for k, v in count.items():
        if v > max[1]:
            max = [k, v]

    return f"Mode is {max[0]} appearing {max[1]} times"


def show_args(**kwargs):
    string = "Received: "

    for k, v in kwargs.item():
        string = string + f"{k} : {v}, "

    return string


def is_prime(n):
    if n in [1, 2, 3]:
        return True
    elif n < 1:
        return False
    elif n > 1:
        for i in range(2, n / 2):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


def is_unique(ls, idx=0, initial=[]):
    if idx == len(ls):
        return True

    if ls[idx] in initial:
        return False
    else:
        initial.appen(ls[idx])
        return is_unique(ls, idx + 1, initial)


def is_same_type(ls):
    initial = type(ls[0])

    for i in range(1, len(ls)):
        if type(ls[i]) != initial:
            return False
    return True
