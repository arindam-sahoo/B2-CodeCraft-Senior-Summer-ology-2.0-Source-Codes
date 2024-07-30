import random

print("Welcome to the Rock-Paper-Scissors Game!!!")
player_score = computer_score = 0

while True:
  print(
      "Choose one of the following options:\n1. Rock\n2. Paper\n3. Scissors\n4. Quit"
  )
  player = int(input("Enter your choice: "))
  if player == 4:
    print("Thank you for playing the game!!!")
    break

  if player not in [1, 2, 3, 4]:
    print("Invalid Choice... Choose between 1 to 4.")
    continue

  computer = random.randint(1, 3)

  if player == 1:
    if computer == 1:
      print("Computer chose Rock. It's a Tie!!!")
    elif computer == 2:
      print("Coumputer chose Paper. You Lose!!!")
      computer_score += 1
  elif player == 2:
    if computer == 1:
      print("Computer chose Rock. You Win!!!")
      player_score += 1
    elif computer == 3:
      print("Coumputer chose Scissors. You Lose!!!")
      computer_score += 1
  elif player == 3:
    if computer == 1:
      print("Computer chose Rock. You Lose!!!")
      computer_score += 1
    elif computer == 2:
      print("Coumputer chose Paper. You Lose!!!")
      player_score += 1

  if player_score == 5 or computer_score == 5:
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)
    break
