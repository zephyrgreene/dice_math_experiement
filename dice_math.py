from random import randint

def roll(num, val):
  total = 0
  for _ in range(num):
    total += randint(1,val)
  return total

def prompt():
  x = int(input("How many dice?"))
  y = int(input("How many sides?"))
  z = int(input("Accuracy/Evasion rating?"))
  return x, y, z

def roll_simulation():
  wins = 0
  
  print("Attacker's Dice:")
  a, b, c = prompt()
  print("Defender's Dice:")
  d, e, f = prompt()
  
  rolls_num = int(input("How many rolls to compare?"))
  for _ in range(rolls_num):
    attack_val = roll(a,b) + c
    defend_val = roll(d,e) + f
    if attack_val >= defend_val:
      wins += 1
    
  print(wins / rolls_num)

def roll_accuracy():
  wins = 0
  a, b, = 3, 6
  c = int(input("Attack Value?"))
  x, y = 2, 6
  z = int(input("Defense Value?"))
  
  for _ in range(100000):
    attack_val = roll(a,b) + c
    defend_val = roll(x,y) + z
    if attack_val > defend_val:
      wins += 1
      
  print(wins / 100000)

def roll_math():
  atk_wins_ties = 0
  def_wins_ties = 0
  accuracy = int(input("Attack Value?"))
  evasion = int(input("Defense Value?"))
  for die1 in range(6):
    for die2 in range(6):
      for die3 in range(6):
        for die4 in range(6):
          for die5 in range (6):
            defend_val = die1+1 + die2+1 + evasion
            attack_val = die3+1 + die4+1 + die5+1 + accuracy
            if attack_val >= defend_val:
              atk_wins_ties += 1
            if attack_val > defend_val:
              def_wins_ties += 1
  print("Ties go to attacker: ", atk_wins_ties/7776)
  print("Ties go to defender: ", def_wins_ties/7776)





