# =================== DAY 4 ============================

"""
Any text enclosed by single, double or triple quotes
are considered strings, they have their own methods
as well. For example len() to fin the length
"""

# Creating a String
letter = "A"  # Can be a single or a bunch of characters
print(letter)  # A
print(len(letter))  # 1

greeting = "Hello World!"
print(greeting)  # Hello World
print(len(greeting))  # 12 ... maybe

sentence = "I hope I like the rest of this python Challenge"
print(sentence)

# Multiline string creation
multiline_string = """This is a multiline string.
This is perfect if you are writing long paragrpahs.
Like for descriptions on websites. Quite interesting."""

print(multiline_string)

# Strign Concatenation
first_name = "Daniel"
last_name = "Diaz"

space = " "
full_name = first_name + space + last_name

print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))  # TRUE
print(len(full_name))

# Escape Sequences

"""
These are special characters that do something special to strings

\n  ->  new line
\t  ->  tab (8 spaces)
\\  ->  back slash
\'  ->  single quote
\"  ->  double quote
"""

# String Formatting (Old Style)
"""
The % operator is used to format a set of variables enclosed
in a tuple, together with a format string, which contains normal
text together with 'argument specifiers' , special symbols like:

"%s" -< String
"%d" -> Integers
"%f" -> Floating Points
"%.number of digitsf" -> Floating points with fixed precision
"""
# Strings only
first_name = "Benjamin"
last_name = "Posada"

formatted = "I am %s %s" % (first_name, last_name)
print(formatted)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formatted = "The are of a circle with radius %d is %.df." % (radius, area)

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formatted = "The following are python libraries:%s" % (python_libraries)
print(formatted)


# String fornatting (New Style - Past Pyhton 3)
# Replaces the % with .format right after the string
# Replaces everything between {}

formatted = "I am {} {}".format(first_name, last_name)
print(formatted)

# Number example
a = 4
b = 3
print("{} / {} = {:.2f}".format(a, b, a / b))


# String Interpolation - Python 3.6 and above
print(f"{a} / {b} = {a / b :.2f}")


# Strings as Sequences of Characters

''' Python strings are sequences of characters, and share
their basic methods of access with other Python ordered
sequences of objects - list and tuples. To extract them
we use the unpacking technique'''

language = 'Python'
a,b,c,d,e,f = language
print(a)    # P
print(b)    # y
print(c)    # t
print(d)    # h
print(e)    # o
print(f)    # n

# Indexing starts from zero, like in many other languages
# Negative indexing works in python, it just wraps around backwards


# Slicing Strings
first_three = language[0:3] # starts at zero and cuts up to and not including 3
print(first_three)

last_three = language[-3:] # emptiness means beggining/end depending on the side of the :

# Reversing a string:
print(greeting[::-1])

''' 
This works through String Slicing Skipping!! (Explained further below)

string[start : stop : step]

Here we start at the very beggining, then we end at the very 
end but stepping backwards by the use of the -1
'''

# Skipping while slicing
pto = language[0:6:2]
print(pto) # IT indeed prints Pto

'''

# ---------- String MEthods -----------------

1. capitalize() 

Convers the first character into a capital letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'



2. count()

Retunrs ocurrences of substring in string
count(substring, start=, end=)

start -> starting index for counting
end   -> last index to count

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2



3. endswith()

Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False



4. expandtabs()

Returns a copy of the string where all tab characters (\t)
are replaced with spaces based on dynamic tab stops

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'



5. find()

Retunrs the index of the first ocurrence of a substrin, if not returns -1

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0



6. rfind()

Returns the index of the last ocurrence of a substring. Otherwise -1

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17



7. format()

Formats a string into a nicer output...
See documentation for this one

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314



8. index()

Returns the lowest index of a substring, additional arguments
indicate starting and ending index (default 0 and string length -1)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error



9. rindex()

Returns the highest index of a substring, additional arguments
indicate starting and ending index (default 0 and string length -1)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19



10. isalnum()

Checks alphanumeric characters across all the string

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False



11. islapha()

Checks if all string elements are alphabet characters (a-z and A-Z)

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False



12. isdecimal()

Checks if all characters in a string are decimal (0-9)

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed



13. isdigit()

Checks if all characters in a string are numbers (0-9
and some unicode characters for numbers)

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True



14. isnumeric()

Checks if all characters in a string are numbers or number
relates (just like isdigit(), just accept more symbols lik 1/2)

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False



15. isidentifier()

Checks for a valid identifier - it checks if a string is a variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True



16. islower()

Checks if all alphabet characters in the string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False



17. isupper()

Checks if all alphabet characters in the string are uppercase

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True



18. join()

Returns a concatenated string

EXAMPLE 1
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

EXAMPLE 2
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'



19. strip()

Removes all given characters starting from
the beginning and end of string

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'



20. replace()

Replaces substring with a given string

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'



21. split()

Splits the string, using given string or space separator

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']



22. title()

Returns a copy of the string title cased

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python



23. swapcase()

Converts all uppercase to lowercases and all lowercase to upper

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON



24. startswith()

Checks if String Starts with specified substring

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
'''

# ================= Exercises Day 4 =======================
space = ' '

string_1 = 'Thirty'
string_2 = 'Days'
string_3 = 'Of'
string_4 = 'Python'
string_5 = 'Coding'
string_6 = 'For'
string_7 = 'All'

concatenated_1 = string_1 + space + string_2 + space + string_3 + space + string_4
concatenated_2 = string_5 + space + string_6 + space + string_7

print(concatenated_1)
print(concatenated_2)

company = 'Coding For All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[8:])

print(company.index('Coding'))
print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

print('Python for Everyone'.replace('Everyone', 'All'))

print(company.split())

print("FB, Google, MS, Apple, IBM, Oracle, Amazon".split(','))

print(company[0])

print(len(company)-1) # LAst index is the length - 1
print(company[10])

pfe = 'Python For Everyone'
separated = pfe.split()

print(separated[0][0] + separated[1][0] + separated[2][0])

company = company.split()
print(company[0][0] + company[1][0] + company[2][0])

company = 'Coding For All'
print(company.find('C'))
print(company.index('C'))
print(company.find('F'))
print(company.index('F'))
print(company.rfind('l'))
print(company.rindex('l'))


print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

