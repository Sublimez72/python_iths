#First part of Chapter 1 coding exercises


# Hello world
print("Hello world")

# Zen of python
import this


# Different prints
name = "Vangelis"
city = "Stockholm"
age = 24

print("Hello my name is {0} and I am {1} years old and live in {2}".format(name, age, city))
print(f"Hello my name is {name} and I live in {city}, and I am {age} years old")


# Format prints
pi = 3.14159

print("%d" % (pi))
print("%e" % (pi))
print("%s" % (pi))


# Basic PDB debugging
import pdb
pdb.set_trace()
print("done")