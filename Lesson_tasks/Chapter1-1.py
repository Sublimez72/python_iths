#First part of Chapter 1 coding exercises


# Hello world
print("Hello world")

# Zen of python
import this


# Different prints
school = "ITHS"
city = "Stockholm"
subject = "python"

print("Hello, I study at {0} in {1} and my current subject is {2}".format(school, city, subject))
print(f"Hello, I study at {school} in {city} and my current subject is {subject}")


# Format prints
pi = 3.14159

print("%d" % (pi))
print("%e" % (pi))
print("%s" % (pi))


# Basic PDB debugging
import pdb
pdb.set_trace()
print("done")