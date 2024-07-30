# Strings

# Definition: A string is a sequence of characters. It consists of letters, numbers, and symbols (special characters, space, and also some other characters).

# Create a String
# We can create a string by enclosing the characters in single quotes, double quotes, or triple quotes.

# Using single quotes
str1 = 'Hello World!'
print(str1)
# Using double quotes
str2 = "Hello World!"
print(str2)

# Using triple quotes
str3 = '''Hello Students,
We are here to learn Python.
Python is a Programming Language'''
str4 = """Hello Students,
We are here to learn Java.
Python is a Programming Language"""
print(str3)
print(str4)

# Finding out the length of a string
# We can find out the length of a string using the len() function.
x = len(str1)
print(f'The length of "{str1}" is {x}')

x = len(str3)
print(f'The length of "{str3}" is {x}')

# Accessing characters of a string
str1 = 'Hello World!'
print(str1[0])  # H
print(str1[10])  # d
print(str1[-1])  # !
print(str1[-3])  # l

# Slicing a string
# We can slice a string using the [start:end] notation.
print(str1[0:8])  # Hello Wo
print(str1[2:8])  # llo Wo
print(str1[2:])  # llo World!
print(str1[:6])  # Hello
print(str1[:])  # Hello World!
print(str1[0:8:2])  # HloW
print(str1[::3])  # HlWl
print(str1[::-1])  # !dlroW olleH (Reverse)

# String Methods
# We can use the following methods to work with strings.
# 1. lower()
print(str1.lower())
# 2. upper()
print(str1.upper())
# 3. strip() : Strip removes the white spaces from the beginning and the end of the string.
str5 = '         Python is a Programming Language.        '
print(str5)
str5 = str5.strip()
print(str5)  # Removes the spaces before and after the string.
# 4. replace()
print(str5.replace('Python', 'Java'))
# 5. find()
print(str5.find('Java'))
print(str5.find('Language'))
# 6. Splitting
print(str5)
print(str5.split())
# 7. Joining
l1 = ['JavaScript', 'is', 'a', 'Programming', 'Language.']
print(''.join(l1))
print(' '.join(l1))
print('_'.join(l1))

# String Operations
# Concatenations : Joining of 2 Strings
a = "Python"
b = "Programming"
print(a + b)

# Repeatation
w = "Pizza"
print(w * 4)

# Membership
print('P' in w)
print('p' in w)
print('Q' in w)

# String Formatting
# 1. Using f-strings
s = f"The length of {str1} is {len(str1)}"
print(s)
# 2. Using format() method
s = "The length of {} is {}".format(str1, len(str1))
print(s)
# 3. Using % operator
s = "The length of %s is %d" % (str1, len(str1))
print(s)
