# Loops

# Definite Loops : We know how many times we want to repeat a loop.
'''
For Loop
'''

for i in range(10):
  print('i')  # Over here i is a String and thats why it prints i 10 times.

print('Zero to Nine')
for i in range(10):  # range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(
      i
  )  # Over here i is a variable and so it prints the value of the variable.

print('Ten to Nineteen')
for i in range(10,
               20):  # range(10, 20) = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  print(i)

print('Twenty to Twenty-Nine Stepped by Two')
for i in range(20, 30, 2):  # range(20,30, 2) = [20, 22, 24, 26, 28]
  print(i)

print('Ten to One')
for i in range(10, 0, -1):
  print(i)

# Tasks
'''
Aarna : Printing all even numbers from 1 to 20.
'''
print('Printing all even numbers from 1 to 20')
for i in range(2, 21, 2):
  print(i)
'''
Myra : Printing all odd numbers from 1 to 20.
'''
print('Printing all odd numbers from 1 to 20')
for i in range(1, 20, 2):
  print(i)

# Indefinite Loops : We don't know how many times we want to repeat a loop.
'''
While Loops
'''
print('Printing using while loops')
i = 1
while i <= 10:
  print(i)
  i = i + 1

# Infinite Loops : The loop never ends.
# i = 1
# while i >= -10:
#   print(i)
#   i = i + 1

print('Printing using while loops')
i = 10
while i >= 1:
  print(i)
  i = i - 1

#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *

print('5x5')
for row in range(1, 6):
  for column in range(1, 6):
    print("*", end=" ")
  print()

#   * * * * *
#   * * * * *
#   * * * * *

print('3x5')
for row in range(1, 4):
  for column in range(1, 6):
    print("*", end=" ")
  print()

#   * * *
#   * * *
#   * * *
#   * * *
#   * * *

print('5x3')
for row in range(0, 5):
  for column in range(0, 3):
    print("*", end=" ")
  print()
