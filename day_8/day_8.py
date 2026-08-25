# ====================================== Day 8: Dictionaries ===================================

"""
A dictionary is a collection of unordered, modiafiable and paired elements
"""

# Creating an empty dictionary
empty = {}
empty_dictionary = dict()


# Loaded with data ' Literally any data
person = {
    "fname": "Daniel",
    "lname": "Diaz",
    "age": 23,
    "country": "ESA",
    "is_married": False,
    "skills": ["Coding", "Electronics", "Python"],
    "address": {"street": "North Avenue", "zipcode": 25087},
}

# Dictionary Length
print(len(person))  # 7

# Accessing Dictionary items - just call its key!
print(person["fname"])  # Daniel
print(person["address"])  # Prints the niner dictionary

# If the item is not present, then python raises an error
# The get() method solves these issues

print(person.get("country"))
print(person.get("city"))


# Adding items to a dictionary
person["job_title"] = "Tech"
person["skills"].append("C#")

print(person)

# Modifying the items in a dictionary
person["fname"] = "Bob"
person["age"] = 50
print(person)

# Checking Keys in a dictionary
print("fname" in person)
print("residencny" in person)

# Rmoving Key & Values from a dictionary
# pop(key) -> removes the item with the specific key name
# popitem() -> removes the last item
# del -> removes an item with specified key name

person.pop("fname")
person.popitem()
del person["is_married"]
print(person)

# Changing Dictionarry to a list of items
print(person.items())  # Separates pairs in a list of tuples

# Clearing a dictionary
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dct.clear())  # None

# Deleting a dictionary
del dct

# Copying a dictionary
clone = person.copy()

# Listing out the keys
print(person.keys())

# Listing values
print(person.values())

# ======================= Exercises Day 8 =============================
