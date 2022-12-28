import random
import os
clear = lambda: os.system('cls')
clear()

computer = 0
user = 0

def unit():
  global computer, user
  unit_op = ['rock', 'paper', 'scissors']
  random_choise = random.choice(unit_op)
  #print(random_choise)
  

  user_op = input('''
chose between:
- rock
- paper
- scissors
''')
  clear()

  if user_op == random_choise:
    print("It's a Draw")
  if user_op == "rock":
    if random_choise == "scissors":
      print("You Win!!!!!!!!!!")
      user = user + 1
    elif random_choise == "paper":
      print("Looseerrrrrr")
      computer = computer + 1
  elif user_op == "scissors":
    if random_choise == "rock":
      print("Looseeeerrr")
      computer = computer + 1
    elif random_choise == "paper":
      print("You Win!!!!!")
      user = user + 1
  elif user_op == "paper":
    if random_choise == "rock":
      print("You win!!!!")
      user = user + 1
    elif random_choise == "scissors":
      print("Loseerrrrrrrrr")
      computer = computer + 1
  else:
      print("elije una opcion correcta")



while user or computer < 3:
  unit()
  print(user, computer)
  if user == 2:
    print('You win againts the computer')
    break
  elif computer == 2:
    print('Computer wins')
    break