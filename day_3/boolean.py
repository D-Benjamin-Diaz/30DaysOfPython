# ---------------------------------------------------------------------------------------------------------------------
#                                               Day 3 Exrcises
# ---------------------------------------------------------------------------------------------------------------------

my_age = 23
my_height = 175.5
rare = 3 + 5j

base = int(input("Enter base: "))
height = int(input("Enter height: "))

print("The area of the trinagle is:", base * height * 0.5)

side_a = int(input("Enter the length of side A:"))
side_b = int(input("Enter the length of side B:"))
side_c = int(input("Enter the length of side C:"))
print("The perimeter is:", side_a + side_b + side_c)

rec_base = int(input("Enter the base: "))
rec_height = int(input("Enter the height: "))
print("Rectangle are is:", rec_base * rec_height)
print("Rectangle perimeter is:", 2 * (rec_base + rec_height))

radius = int(input("Enter radius of circle: "))
print("The area is :", 3.14 * radius**2)
print("The circumference is", 3.14 * 2 * radius)

# y = 2x - 2
print("Slope:", 2)
print("Y-intercept: ", -2)
print("X-intercept: ", 1)

# Given (2, 2) and (6, 10)
print("Slope:", (10 - 2) / (6 - 2))
print("Eucledian Distance: ", ((10 - 2) ** 2 + (6 - 2) ** 2) ** 0.5)

print("Slope Comparisson (Same?)", 2 == 2)

print("y = x^2 + 6x + 9")
print("Solution: x = ", -3)
print("Verification:", 0 == (-3) ** 2 + 6 * (-3) + 9)

print(len("python") != len("dragon"))

print("on" in "dragon" and "on" in "python")
print("jargon" in "I hope this course is not full of jargon")

print(not ("on" in "dragon" and "on" in "python"))

print(str(float(len("dragon"))))

number = int(input("Is your number divisible by 2? "))
print(number % 2 == 0)

print(7 // 3 == int(2.7))
print(type(10) == type("10"))
print(int(float("9.8")) == 10)


rate = float(input("Enter you rate: "))
print("Your pay is: ", rate * 40)

years = int(input("Enter a number of years: "))

print("You have lived for", years * 365 * 24 * 60 * 60, "seconds")

print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
