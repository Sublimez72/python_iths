from pprint import pprint

# Play with dir() function
# Create a script and define a few variables of all different types you know.
number = 12
letters = "Student"
boolean = True
list_of_strings = ["Student", "ITHS"]
dictionary_of_strings = {"Student": "ITHS"}
tuple_of_strings = ("Student", "ITHS")

print("Integer")
pprint(dir(number))
print("Strings")
pprint(dir(letters))
print("Boolean")
pprint(dir(boolean))
print("List of strings")
pprint(dir(list_of_strings))
print("Dictionary of strings")
pprint(dir(dictionary_of_strings))
print("Tuple of strings")
pprint(dir(tuple_of_strings))

# String substrings
# Get the characters from index 2 to index 4.
# If you have the string "abcdef" it should print out "cd"
string_to_substring = input("What string do you want to substring?: ")
print(string_to_substring[2:4])

# Palindrome program
# Task: Given a string, write a python script to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome.
def string_reverser(str):
    return str[::-1]

while True:
    print()
    print("Enter q to exit loop")
    palindrome_to_check = input("What string do you want to check if it's a palindrom?: ")
    if palindrome_to_check.lower() == "q" or palindrome_to_check.lower() == "quit" or palindrome_to_check.lower() == "exit":
        break
    if palindrome_to_check == string_reverser(palindrome_to_check):
        print(f"{palindrome_to_check} is a palindrome!\nReversed form: {string_reverser(palindrome_to_check)}")
    elif palindrome_to_check != string_reverser(palindrome_to_check):
        print(f"{palindrome_to_check} is not a palindrome!\nReversed form: {string_reverser(palindrome_to_check)}")
    
# User input
# Create a script that asks the user for some input and save it to a variable.
# Do this multiple times and save to multiple variables.
# Use the f-string rendering to print the contents of your variables to your terminal.
# For instance create a program that asks for your first and last name, then print your full name in one line.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
print(f"Your full name is {first_name} {last_name}")

# Variable comparisons
# Write a program where you define a number of variables and assign them to all the basic variables types, boolean, str, int, float.
# Now try to compare the different values between eachother using `==` and print the result. Try and see what happens if you attempt this with different variable types. For instance a string and a int.
# Next try to add variables to eachother and store them in a new variable. Print the content of the new variables to your terminal and try to figure out which values works with what other values.