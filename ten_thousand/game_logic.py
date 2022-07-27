from collections import Counter
import random

from pip import main

class GameLogic:
  
  def __init__(self):
    pass

  @staticmethod
  def calculate_score(roll):

    roll_count = Counter(roll)


    if len(roll) == 0:
      return 0


    if len(roll) == 1:
      if roll_count[1] == 1:
        print("One 1: 100pts")
        return 100
      elif roll_count[5] == 1:
        return 50
      else:
        return 0


    if len(roll) == 2:
      if roll_count[1] == 2:
        return 200
      elif roll_count[5] == 2:
        return 100
      else:
        return 0


    if len(roll) == 3:
      if roll_count[1] == 3:
        return 1000
      elif roll_count[roll[0]] == 3:
        return roll[0] * 100


    if len(roll) == 4:
      if roll_count[1] == 4:
        return 2000
      if roll_count[roll[0]] == 4:
        return (roll[0] * 100) * (len(roll) -2)


    if len(roll) == 5:
      if roll_count[1] == 5:
        return 3000
      elif roll_count[roll[0]] == 5:
        return (roll[0] * 100) * (len(roll) -2)
    

    if len(roll) == 6:
      if roll_count[1] == 6:
        return 4000
      elif roll_count[roll[0]] == 6:
        return (roll[0] * 100) * (len(roll) -2)
      

      #2x 3 of a kind
      for i in range(6):
        if roll_count[i] == 3:
          for i in range(i+1, 6):
            if roll_count[i] == 3:
              return 1200
            else:
              return i * 100

      # Straight
      if roll == (1,2,3,4,5,6):
        return 1500

      # 3 pair
      pair_count = 0
      for i in range(7):
        print(i)
        if roll_count[i] == 2:
          pair_count += 1
          print(f"There's two {i}'s")
      print(f"Pair Count: {pair_count}")
      if pair_count == 3:
        return 1500
      else:
        return 0
        

  @staticmethod
  def roll_dice(dice):
    print(f"Rolling {dice} dice...")
    roll = []
    for _ in range(dice):
      roll.append(random.randint(1, 6))
    result = tuple(roll)
    print(f" *** {result} ***") # TODO get rid of ()
    return result 





print("Welcome to Ten Thousand")
print("(y)es to play or (n)o to decline")
wanna_play = input("> ")
if wanna_play == "n":
  print("OK. Maybe another time")
  exit()
if wanna_play == "y":
  print("Starting round 1")
  GameLogic.roll_dice(6)
print("Enter dice to keep, or (q)uit:")
keeps = input("> ")
if keeps == "q":
  print("Thanks for playing. You earned 0 points")
  exit()


