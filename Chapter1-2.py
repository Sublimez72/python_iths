# Second part of chapter 1 coding exercises

# Two inputs

name = input("Name: ")
age = input("Age: ")

# Calculate a math problem
import math

# Area of square
square_side = float(input("What is the side of your square?: "))
print(f"The area of your square is {square_side ** 2} \n")

# Calculate circumference
circle_diameter = float(input("What is the diameter of your cirlce?: "))
print(f"The circumference of your circle is {circle_diameter * math.pi} \n")

# Calculate area of a triangle
triangle_base = float(input("What is the base of your triangle?: "))
triangle_height = float(input("What is the height of your triangle?: "))
print(f"The area of your triangle is {(triangle_base * triangle_height) / 2} \n")

# Calculate the moms of a number
pre_moms = float(input("What is your gross price?: "))
post_moms = pre_moms * 1.25
moms = post_moms - pre_moms

print(f"Your price after moms is {post_moms}. The moms is {moms} \n")