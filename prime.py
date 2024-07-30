from typing import ParamSpec


def checkPrime(num):
  if num <= 1:
    print('They are neither composite nor prime.')
    return False

  f = 0
  for i in range(2, num + 1):
    if num % i == 0:
      f = f + 1  # Shortcut: f += 1

  return f == 1


# num = int(input("Enter a number: "))

# if checkPrime(num):
#   print(num, "is an PRIME NUMBER.")
# else:
#   print(num, "is a COMPOSITE NUMBER.")
'''
For Examples

11 = 1, 11                     (PRIME)
24 = 1, 2, 3, 4, 6, 8, 12, 24  (COMPOSITE)
'''

end_range = int(input("Enter the ending range: "))
print("List af all prime numbers from 2 to", end_range)

for i in range(2, end_range + 1):
  if checkPrime(i):
    print(i)
