# ====================================== Day 6: Tuples ==================================

"""
A Tuple is a collection of different datatypes which is ordered
and immutable. Unlike lists, and because they are immutable
tuples have less methods that can be used.
"""

# Creating an empty tuple
empty_tuple = tuple()

# Creating a tuple with initial values
fruits = ("banana", "orange", "mango", "lemon")

# Tuple lenght -> len(tuple)
print(len(fruits))  # 4


# -----------------------------
# Accessing Tuple items
# -----------------------------

# Positive Indexing
banana = fruits[0]
mango = fruits[2]

# Negative indexing
orange = fruits[-3]
lemon = fruits[-1]


# -------------------------------
# Slicing Tuples
# -------------------------------

# Very similar to lists
# Positives
all_fruits = fruits[0:]
all_fruits = fruits[0:4]
orange_mango = fruits[1:3]
no_banana = fruits[1:]

# Negatives
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
no_banana = fruits[-3:]


# --------------------------
# Changing Tuples to Lists
# --------------------------

# There are tuple and lists methods that are interchangeable to convert to and back from a lits
fruits = list(fruits)  # ['banana', 'orange', 'mango', 'lemon']
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')


# Cheking for existence
print("apple" in fruits)  # True
print("banana" in fruits)  # False

# fruits[0] = 'banana' -> Produces an error


# Joining tuples. Use + operator
vegetables = ("potato", "tomato", "cabbagge", "carrot")
fruits_and_veggies = fruits + vegetables

# Deleting a full tuple
del vegetables  # Destroys veggies completely


# ============================== Exercises Day 6 ===================================

# LEVEL 1
empty = tuple()
fruits = ("berries", "bananas", "apples", "oranges")
veggies = ("zuchinni", "carrot", "broccoli", "onion")
animal_products = ("beef", "pork", "chicken", "milk")

groceries = fruits + veggies + animal_products
print(groceries)

family = ("Chana", "Dano", "Chela", "JP", "Tuli", "Tilin")

print(family)
print(len(family))

family = family + ("Pincho", "Yese")

print(family)


# LEVEL 2
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Estonia" in nordic_countries)
print("Denmark" in nordic_countries)

family_list = list(family)

*bichos, papa, mama = family_list
print(bichos)
print(mama)
print(papa)

grocery_list = list(groceries)

middle_item = grocery_list[(len(grocery_list) - 1) // 2 : len(grocery_list) // 2 + 1]

first_three = grocery_list[0:3]
last_three = grocery_list[-3:]

print(first_three)
print(last_three)

del groceries
