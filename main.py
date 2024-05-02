import random

def rock_paper_scissors():
  user = input("Escolha pedra, papel, tesoura: ")
  computer = random.choice(['pedra', 'papel', 'tesoura'])
  print(f"computer escolheu {computer}")

  if user == computer:
   return "EMPATE!"

  elif (user == "pedra" and computer == "tesoura")  or (user == "papel" and computer == "pedra") or (user == "tesoura" and computer == "papel"):
   return "YOU WINS!"

  else:
   return "YOU LOSE!"


print(rock_paper_scissors())