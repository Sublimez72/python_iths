from pprint import pprint

# Play with dir() function
# Create a script and define a few variables of all different types you know.
number = 12
letters = "12"
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
def string_reverser(string):
    return string[::-1]

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
# Use the 
# string rendering to print the contents of your variables to your terminal.
# For instance create a program that asks for your first and last name, then print your full name in one line.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
print(f"Your full name is {first_name} {last_name}")

# Variable comparisons
# Write a program where you define a number of variables and assign them to all the basic variables types, boolean, str, int, float.
# Now try to compare the different values between eachother using `==` and print the result. 
# Try and see what happens if you attempt this with different variable types.
# For instance a string and a int.
# Next try to add variables to eachother and store them in a new variable. 
# Print the content of the new variables to your terminal and try to figure out which values works with what other values.
try:
    print("Integer equal to string")
    if number != letters:
        print("Not equal")
    else:
        print("Equal")

    print("List equal to tuples")
    if list_of_strings == tuple_of_strings:
        print("Equal")
    else:
        print("Not equal")
    
    print("List equal to integer")
    if list_of_strings != number:
        print("Not equal")
    else:
        print("Equal")
    

    print("Integer greater than string")
    if number > letters:
        print("Greater")
    else:
        print("Not Greater")
    

except Exception as e:
    print(str(e))


# Help command
# Python has a built in `help()` command where in your REPL or in your script, you can run help on any variable or object.
# Create a script and assign several variables different values from each basic data type, bool, str, int, float. 
# Then run help on each one of the variables and read through the output.
# What is different between each call to help when doing it with different variable types?
help(type(number))
print()
help(type(letters))
print()
help(type(list_of_strings))
print()
help(type(tuple_of_strings))
print()
help(type(boolean))
print()
help(type(dictionary_of_strings))
print()


# String escapes
# Python has several string escapes that can be put into a string variable to get different outputs.
# Create a script where you create several different string variables but you add in the following escape characters inside the strings. 


# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# Then print the strings to your terminal and observ the output from them.


single_quote = "\'single_quote "
backslash = "\\backslash "
new_line = "\nnew_line "
carriage_return = "\rcarriage_return "
tab = "\ttab "
backspace = "\bbackspace "
form_feed = "\fform_feed "

escape_characters = [
    single_quote,
    backslash,
    new_line,
    carriage_return,
    tab,
    backspace,
    form_feed
]

for escape_character in escape_characters:
    print(escape_character)



# String .format() vs f-strings
# Create a script and create several different string variables with different texts. 
# First use the `.format()` method to render a string into another string and print it to your terminal.
# Next use the f-strings to print and render a string into another string.
# Compare both methods and which one is simpler to use.
school = "ITHS"
city = "Stockholm"
subject = "python"

print("Hello, I study at {0} in {1} and my current subject is {2}".format(school, city, subject))
print(f"Hello, I study at {school} in {city} and my current subject is {subject}")


# Casting variables
# Create a script and create a few variables and assign them different values. 
# Now attempt to convert each different variable type to another and see where this fails and where this works.
# Use the following convert methods, `str()` `int()` `float()` `bool()`
# Which values can be casted to other values and which values do not work?

