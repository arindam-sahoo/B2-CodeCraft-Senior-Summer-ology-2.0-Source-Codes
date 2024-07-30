# Control Flow: Control Flow is the order in which the statements are executed in a program.

# The Control Flow can be interuppted by using only if-else statements and the iterative statements.

# If-Else Statements (Conditional Statements)
weather = "sunny"

# Using only 'if'
if weather == "rainy":
  print("Take an umbrella")

# If statements do not mention what to do if the condition is not met (false).

# Using 'if-else'
if weather == "rainy":
  print("Take an umbrella")
else:
  print("No need to take an umbrella")

# Using 'if-elif-else'. It can take more than one condition.
if weather == "rainy":
  print("Take an umbrella")
elif weather == "sunny":
  print("Take an umbrella")
else:
  print("No need to take an umbrella")

# Iterative Statements 
# Using For-Loops
# For-Loops are used to iterate over a sequence (that is either a list, a tuple, a dictionary

# For-Loop using one argument
print('For-Loop using one argument')
for i in range(15):
  print(i)

# For-Loop using two arguments
print('For-Loop using two arguments')
for i in range(20, 51):
  print(i)

# For-Loop using three arguments
print('For-Loop using three arguments')
for i in range(20, 51, 5):
  print(i)

# Reyansh's Task : Print all odd numbers from 1 to 20.
print("Reyansh's Task : Print all odd numbers from 1 to 20")
for i in range(1, 20, 2):
  print(i)

# Niranjan's Task : Print all even numbers from 1 to 20.
print("Niranjan's Task : Print all even numbers from 1 to 20")
for i in range(2, 21, 2):
  print(i)

# Using While-Loops
# While-Loops are used to execute a set of statements as long as a condition is true.

print("Using while loops for peinting 1 to 10")
i = 1

while i <= 10:
  print(i)
  i = i + 1

# Reyansh's Task : Print from 20 to 30.
print("Reyansh's Task : Print from 20 to 30")
i = 20

while i <= 30:
  print(i)
  i = i + 1

# Niranjan's Task : Print from 50 to 60.
print("Niranjan's Task : Print from 50 to 60")
i = 50

while i <= 60:
  print(i)
  i = i + 1

# Reverse For Loop
print("Reverse For Loop")
for i in range(10, 0, -1):
  print(i)
