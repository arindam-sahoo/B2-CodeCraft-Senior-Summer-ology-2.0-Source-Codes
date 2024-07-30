# Importing the Random Library for generating random integers
import random

# Initializing the score as 0
score = 0

# Initializing the count of sixes thrown consecutively as 0
c = 0

while True:                          # Running an infinite loop
  print("Throwing the Dice")
  dice = random.randint(1, 6)        # Generating a random number from 1 to 6.
  print("You threw the dice and got ", dice)  # Showing what we threw
  if dice == 6:                      # If we got a 6, increases the count of consecutive sixes by 1
    c += 1
  if c==3:                           # If we get 3 consecutive sixes, our turn will be over
    print("You got 3 sixes in a row. Your turn ends.")
    print(score)
    break
  score += dice                      # Increasing the score
  print(score)                       # Displaying the score
  print("Your turn ends.")
  if dice !=6:                       # If we didn't get a 6, we are done with our turn
    break