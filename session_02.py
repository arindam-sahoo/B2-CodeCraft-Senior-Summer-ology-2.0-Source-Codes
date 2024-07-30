# Variables
# Temporary | Memory Locations | Stores Values
x = 10

print(x)  # x without any quotations, then it is a variable.
print("x")  # x with quotations, then it is a string.

sport = "Soccer"
print("sport")  # sport
print(sport)  # Soccer

# Rules for Naming Variables
# 1. We can not start a variable name with a number.
# Eg. 123xyz, 3abc --> Invalid | abc123, a1b2c --> Valid
# 2. We can not use any special characters except _ (underscore).
# Eg. abc@, abc!, abc$ --> Invalid | abc_, abc_123 --> Valid
# 3. Variable Names can not have a space in between.
# abc def, ert 123 --> Invalid | abcDef, ert______________________123 --> Valid

# Output
# print(python)    # Variable does not exist. Error: name 'python' is not defined'
print("python")  # This is a string.

print(456646778)  # This is a number (int).

print(True)  # This is a boolean value.
print(False)  # This is a boolean value.

# Data Types
# The type of values we store in a variable is its data type.

# 1. String : It is a sequence of characters. It can be a letter, a word, a sentence, a paragraph, etc.
s = "Python"
print(s)  # Python
print(type(s))  # <class 'str'>

# 2. Integer : It is a non-decimal value.
x = 10234234123342343546547657657567
print(x)  # 10234234123342343546547657657567
print(type(x))  # <class 'int'>

# 3. Float : It is a decimal value.
x = 1243324234.23423542543
y = 2e4  # 2 x 10^4 = 2 x 10000 = 20000
print(x)
print(type(x))
print(y)
print(type(y))

# 4. Boolean : It is a value that can be either True or False.
x = True
print(x)
print(type(x))
y = False
print(y)
print(type(y))

# Primitive: Data Types that can have only one value.
# Non-Primitive: Data Types that can have multiple values. For Eg, Lists, Dictionaries, Sets, Tuples.

# Initialization : Giving a value to a variable during creation.
name = "Python"
print(name)
# Reassignment : Changing the value of a variable.
name = "Java"
print(name)

print("12" + "34")  # String Concatenation
print(12 + 34)

num1 = input("Enter anything:")  # input() takes input as a str.
print(type(num1))

# Type Casting : Changing the data type of a variable.
# |--> Implicit Type Casting : Which Python can do by itself.
# |--> Explicit Type Casting : Where Python needs Human intervention.

# Implicit Type Casting
a = 50  # It itself converts the int into float (50 turns into 50.0)
b = 10.56
print(a + b)

# Explicit Type Casting
a = float(
    "50")  #It requires human intervention, Python will not do it by itself.
b = 10.56
print(a + b)
