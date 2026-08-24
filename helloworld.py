# Day 1 - 30DaysOfPython Challenge

print(2 + 3)  # addition (+)
print(3 - 1)  # subtraction (-)
print(2 * 3)  # multiplication (*)
print(3 / 2)  # division (/)
print(3 % 2)  # modulus (%)
print(3**2)  # exponential (**)
print(3 // 2)  # Floor division (//)

# Checking data types
print(type(10))  # Int
print(type(3.14))  # Float
print(type(1 + 3j))  # Copmlex number
print(type("Benjamin"))  # String
print(type([1, 3, 2]))  # List
print(type({"name": "Benjamin"}))  # Dictionary
print(type({9.8, 3.14, 2.7}))  # Set
print(type((9.8, 3.14, 2.7)))  # Tuple

# ---------------------------------------------------------------------------------
#                             Exercises of Day 1 Below 
# ---------------------------------------------------------------------------------


# ================================== LEVEL 1 ======================================

# Write 'python --version' on Terminal to check version

# Using interactive shell for operators, for strings and checking data types:

'''
C:\Users\BenjaminDiaz>python
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 3+4
7
>>> 4-3
1
>>> 3*4
12
>>> 4%3
1
>>> 4/3
1.3333333333333333
>>> 4**3
64
>>> 4//3
1
>>> 'Benjamin'
'Benjamin'
>>> 'Diaz
File "<stdin>", line 1
    'Diaz
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 'Diaz'
'Diaz'
>>> 'El Salvador'
'El Salvador'
>>> type(10)
<class 'int'>
>>> type(9.8)
<class 'float'>
>>> type(3.14)
<class 'float'>
>>> type(4-4j)
<class 'complex'>
>>> type(['Asabeneh', 'Python', 'Finland']
... )
<class 'list'>
>>> type('Daniel')
<class 'str'>
>>>
'''


# ==================================== LEVEL 2 =======================================

# Moving Exercise 1 into a file -> day_1/helloworld.py

# ==================================== LEVEL 3 =======================================


# ================== LEVEL 3 Copy ==========================

print(8 + 7)
print(9 - 2)
print(8 * 7)
print(27 / 8)
print(17 % 4)
print(9**4)
print("Javi")
print("Norway")
print("This is a string")
print("The following is a set of Natural Numbers")
print({1, 2, 3, 4, 5, 6, 7, 8, 9})
print({"number": 1, "letter": "a"})
print((1, 3, 5, 7, 9))
print([2, 4, 8, 16, 32])


# Euclidean Distance between (2,3) and (10,8)

print(((10 - 2) ** 2 + (8 - 3) ** 2) ** 0.5)
