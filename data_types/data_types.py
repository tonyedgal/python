import math
# file naming convention in python
# 1. all lowercase
# 2. words separated by underscore
# 3. no spaces

# Data Types

# String data type

# LITERAL ASSIGNMENT
first = "Tony"
last = "Edgal"
print(type(first))
# print(type(last) == str)
# print(isinstance(last, str))


# CONSTRUCTOR FUNCTION
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# STRING CONCATENATION
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# CASTING A NUMBER TO A STRING
decade = str(1980)
print(type(decade))
print(decade)
statement = "I like rock music from the " + decade + "s"
print(statement)

# MULTIPLE LINE STRINGS
multiline = '''
Hey there!   

whats up?   

        Tony

'''
# print(multiline)

# ESCAPE SPECIAL CHARACTERS
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# STRING METHODS

print(first)
print(first.upper())
print(first.lower())

print(multiline.title())  # Capitalizes the first letter of each word
# Replaces the first argument with the second argument
print(multiline.replace("up", "good"))
print(multiline)

print(len(multiline))  # Returns the length of the string
multiline += "                  "
multiline = "             " + multiline
print(len(multiline))

print(len(multiline.strip()))  # Removes leading and trailing whitespaces
print(len(multiline.lstrip()))  # Removes leading whitespaces
print(len(multiline.rstrip()))  # Removes trailing whitespaces

print("")

# Build a menu
title = "menu".upper()  # string methods can be called on values directly
# Centers the string in the middle of 20 characters with = on both sides
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])  # value at the end is not included
print(first[1:])

# some methods return boolean data
print(first.startswith("T"))
print(first.endswith("f"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(myvalue))
print(isinstance(myvalue, bool))

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(3.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "90210"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data types
zip_value = int("New york")
