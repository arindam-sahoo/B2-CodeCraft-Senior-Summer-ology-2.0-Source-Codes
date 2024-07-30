import math
# The Math Library is used for carrying out mathematical operations. It has a lot of mathematical functions (floor, ceil, sqrt, pow) and constants.

# Mathematical Constants
print(math.pi)
print(math.e)

# Mathematical Functions
print(math.floor(65.7))
print(math.ceil(66.8))

print(math.sqrt(16))
print(math.sqrt(25.5))

print(math.pow(2, 3))
print(math.factorial(5))

import random
# The Random Library is used for working with random numbers.

print("Random Number:",random.random())
print("Random Integer:",random.randint(1,100))

fruits = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]
print("Random Choice:",random.choice(fruits))
# The random.shuffle() function shuffles the elements of a list.
print("Original List:",fruits)
random.shuffle(fruits)
print("Shuffled List:",fruits)