# Palindrome: A word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses


def checkPalindrome(user_input):
  user_input = str(user_input)
  return user_input == user_input[::-1]


# user_input = input("Enter anything: ")

# if checkPalindrome(user_input):
#   print(user_input, "is PALINDROME.")
# else:
#   print(user_input, "is not PALINDROME.")

print("All the Palindrome numbers from 100 to 999 are: ")
for i in range(100, 1000):
  if checkPalindrome(i):
    print(i)
    