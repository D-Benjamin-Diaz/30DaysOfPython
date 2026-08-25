# ===================================== Day 7: Sets ===============================================

"""
A set is a collection of unordered and un-indexed
distinct elements. Pretty much like math. And it
has very similar set operations as in math.
"""

# ----------------------
# Creating a Set
# ----------------------

# Empty set
st = set()

# Set with initial items
fruits = {"banana", "orange", "mango", "lemon"}


# Length of a set
print(len(fruits))  # 4

# To access elements of a set, loops must be used. More on this later

# Checking presence
print("orange" in fruits)

# Adding one item to a set -> add(item)
fruits.add("lime")
print(fruits)

# Adding multiple items to a set
vegies = {"tomato", "potto", "cabbagge", "onion", "carrot"}

fruits.update(vegies)
print(fruits)

# Remove an specific item from a set -> remove(item)
fruits.remove("onion")
fruits.remove("potto")
fruits.remove("carrot")
fruits.remove("tomato")

print(fruits)

# Remove a random item from the set -> pop()
item = fruits.pop()

print(item)
print(fruits)
fruits.add(item)

# Clearing a set
vegies.clear()

# Deleting a set
del vegies

# Converting list to a set
vegies = ["tomato", "carrot", "onion", "tomato", "cabbagge"]
vegetables = set(vegies)
print(vegies)
print(vegetables)

# Joining sets -  All the following should print the same
print(fruits.union(vegetables))
print(fruits | vegetables)
print(fruits.update(vegetables))

# Finding Intersection items
whole = {0, 1, 2, 3, 4, 5, 67, 8, 9, 10}
even = {0, 2, 4, 6, 8, 10}

print(whole.intersection(even))

# Checking Sub sets and Super sets - containment of entirety
print(whole.issubset(even))  # FALSE
print(whole.issuperset(even))  # TRUE

# Checking the Difference between two sets - Elements of A not present in B
print(whole.difference(even))

# Finding symmetric Difference between two sets
# Elements from a A that aren't in B and Elements in B that aren't in A
numbers = {1, 2, 3, 4, 5}
print(whole.symmetric_difference(numbers))


# Joint and Disjoint sets

# joint -> They have common elements
# disjoint -> They have no common elements

odd = {1, 3, 5, 7, 9}

print(even.isdisjoint(odd))  # True
print(whole.isdisjoint(even))  # False


# ====================================== Exercises Day 7 ===========================================

# LEVEL 1
# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update({"Nvidea", "Anthropic", "Open AI"})
print(it_companies)
it_companies.remove("Google")
print(it_companies)


# Discard removes if object is found, if not, it ignores and produces no error
print(it_companies.discard("Space X"))

# LEVEL 2
joined = A | B
print(joined)
intersect = A.intersection(B)
print(intersect)

print(A.issubset(B))

print(A.isdisjoint(B))

joined_ = B | A
print(joined_)

print(A.symmetric_difference(B))
del A
del B
del joined_
del joined

# LEVEL 3
ages = set(age)

print(len(age), len(ages))

string = "I am a teacher and I love to inspire people and teac people"
print("Unique words: ", len(set(string.split())))
