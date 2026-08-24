# ============================= Day 5: Lists =============================

"""
---- Python Collections ----

1. List     -> ordered, indexed and modifiable collection that allows duplicates
2. Tuple    -> ordered and unmodifiable collection that allows duplicates
3. Set      -> unordered, un-indexed, unmodifible, can add to a set but NO duplicates
4. Dictionry -> unordered, modifiable, indexed collection. NO DUPLICATES
"""

# -------------------------------------
# Creating a list -> Built in function
# -------------------------------------

lst = list()  # This is an empty list
print(len(lst))  # 0

# Creating list using square brackets
lst = []
fruits = ["banana", "apple", "orange", "mango"]

print("Fruits: ", fruits)
print("Number of fruits: ", len(fruits))


# List may hold items from different data types - watch out
lst = ["Benjamin", 300, True, {"country": "ESA", "city": "SIVAR"}]


# ---------------------------------
# Accessing Items through indexing
# ---------------------------------

# We access each item using their index starting from zero

# Accessing firts item
first_fruit = fruits[0]
print(first_fruit)

# Accessing second item
second_fruit = fruits[1]
print(second_fruit)

# Accessing last item
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)


# We can also use negative indexing where:

#     index ->   -4       -3        -2       -1
#   fruits = ['banana', 'apple', 'orange', 'mango']

first_fruit = fruits[-4]
print(first_fruit)  # banana


# Items of a list can also be unpacked
items = ["item 1", "item 2", "item 3", "item 4", "item 5"]

first, second, third, *rest = items
print(first)  # item 1
print(second)  # item 2
print(third)  # item 3
print(rest)  # ['item 4', 'item 5']

# Second Example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

# Third Example about unpacking list
countries = [
    "Germany",
    "France",
    "Belgium",
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland",
    "Estonia",
]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


# List slicing is very similar to that one of string slicing
all_fruits = fruits[0:4]
all_fruits = fruits[0:]  # same result
apple_orange = fruits[1:3]
apple_mango = fruits[::2]  # take every second item

# With negative index
all_fruits = fruits[-4]  # same result
apple_orange = fruits[-3:-1]
last_three = fruits[-3:]
apple_mango = fruits[::2]  # take every second item


# ----------------
# Modifying Lists
# ----------------

# Lists are mutable. their items can be changed to whatever we need/want

fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)  #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = "apple"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lime']


# ------------------
# Checking Presence
# ------------------

does_exists = "apple" in fruits
print(does_exists)  # True
does_exists = "lemon" in fruits
print(does_exists)  # False


# --------------------------
# Modifying items in a list
# --------------------------

# Adding at the end -> append(item)
fruits.append("avocado")  # ['avocado', 'apple', 'mango', 'lime', 'avocado']
print(fruits)
fruits.append("tomato")  # ['avocado', 'apple', 'mango', 'lime', 'avocado', 'tomato']
print(fruits)

# Removing items into a list -> remove(item)
fruits.remove("avocado")  # ['apple', 'mango', 'lime', 'avocado', 'tomato']
print(fruits)
fruits.remove("tomato")  # ['apple', 'mango', 'lime', 'avocado']
print(fruits)

# Inserting intems into a list -> inset(index, item) other items are shifted to the right
fruits.insert(2, "tomato")  # ['apple', 'mango', 'tomato', 'lime', 'avocado']
print(fruits)
fruits.insert(
    3, "avocado"
)  # ['apple', 'mango', 'tomato', 'avocado', 'lime', 'avocado']
print(fruits)

# Popping items off of a list -> pop(index or empty) if empty removes last item
fruits.pop()  # ['apple', 'mango', 'tomato', 'avocado', 'lime']
print(fruits)
fruits.pop(3)  # ['apple', 'mango', 'tomato', 'lime']
print(fruits)


# Deleting items off the list -> del keyword
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]

del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[
    1:3
]  # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)  # ['orange', 'lime']
# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# Clearing List items -> clear() deletes the items but not the list itself
fruits.clear()
print(fruits)  # []

# Copying a list -> copy() creates a new list with the same elements. Avoids referencing issues
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']

# Counting elements in a list -> count(item) counts how many times the item appears on the list
print(fruits.count("banana"))  # 1

# Finding the index of an item -> index(item) returns the index of an item
print(fruits.index("mango"))  # 2

# Reversing a list -> reverse() literaly reverses the list
print(fruits.reverse())


# --------------------------------------
# Joining multiples lists different ways
# --------------------------------------

# Plus operator (+) -> concatenated lists remain the same
positives = [1, 2, 3, 4]
zero = [0]
negatives = [-4, -3, -2, -1]

integers = negatives + zero + positives
print(integers)  # [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# Extend method -> extend() changes the list permanently
negatives.extend(zero)
negatives.extend(positives)
print(negatives)  # [-4, -3, -2, -1, 0, 1, 2, 3, 4]


# ------------------------------
# Sorting Items from lists
# ------------------------------

# Modifying the original list -> sort()
numbers = [6, 9, 4, 5, 0, 1, 2]
print(numbers.sort())
print(numbers.sort(reverse=True))

# Not modifying original -> sorted(list)
numbers = [6, 9, 4, 5, 0, 1, 2]
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print("Original: ", numbers)


# ====================================== Exercises Day 5 =================================

# Level 1

empty_list = []

large_list = ["Diana", "Daniel", "Marcela", "Juan", "Lucia", "Tilin"]

print(len(large_list))

print(large_list[0])
print(large_list[len(large_list) // 2])
print(large_list[-1])

mixed = ["Daniel", 23, 175, "single...", "New York"]

companies = ["FB", "GOG", "MS", "APL", "IBM", "AMZ"]

print(companies)

print(companies[0])
print(companies[len(companies) // 2])
print(companies[-1])

companies[2].lower()  # ms
companies_string = "#; ".join(companies)

print("GOG" in companies)
print("X" in companies)

print(companies.sort())
print(companies.reverse())

print(companies[0:3])
print(companies[-3:])

print(
    companies[len(companies) // 2 - 1 : len(companies) // 2 + 1]
)  # Even number of elements

print(companies.pop(0))
print(companies.pop(len(companies) // 2))
print(companies.pop(len(companies) - 1))
print(companies.clear())
del companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

full_stack = front_end + back_end
full_stack.insert(full_stack.index("Redux"), ["Python", "SQL"])

print(full_stack)


# LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

srt_ages = sorted(ages)

mini = srt_ages[0]
maxi = srt_ages[-1]

print(mini, maxi)
print(mini + maxi)

ages.append(mini)
ages.append(maxi)

median_age = (srt_ages[(len(srt_ages) - 1) // 2] + srt_ages[(len(srt_ages) // 2)]) / 2

average = sum(srt_ages) / len(ages)

compare_with_min = abs(mini - average)
compare_with_max = abs(maxi - average)

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

middle_country = countries[(len(countries) - 1) // 2 : len(countries) // 2 + 1]

print(middle_country)

second_half, first_half = (
    countries[-(len(countries) // 2) :],
    countries[-len(countries) : -len(countries) // 2],
)

print("Countries lengths:")
print(len(first_half))
print(len(second_half))

china, russia, usa, *scandies = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark",
]

print(china)
print(russia)
print(usa)
print(scandies)
