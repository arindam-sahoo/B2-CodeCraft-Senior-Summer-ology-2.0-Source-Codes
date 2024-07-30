def checkEven(num):
  return num % 2 == 0


num = int(input("Enter a number: "))

if checkEven(num):
  print(num, "is an EVEN NUMBER.")
else:
  print(num, "is an ODD NUMBER.")
