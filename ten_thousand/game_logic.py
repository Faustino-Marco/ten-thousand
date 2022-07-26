from collections import Counter
from curses import pair_content
import random

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
        
          # for x in range(i+1, 5):
          #   if roll_count[x] == 2:
          #     print(f"There's two {x}'s")
          #     if roll_count[6] == 2:
          #       return 1500
          #     else:
          #       return 0
          #   else:
          #     return 0
          #     for y in range(x+1, 6):
          #       if roll_count[y] == 2:
          #         print(f"There's two {y}'s")
          #         return 1500
          #       else:
          #         return 0
            # else:
            #   return 0














  # def calculate_score(roll):
  #   if len(roll) == 1:
  #     if roll[0] == 1:
  #       print("One 1: 100pts")
  #       return 100
  #     elif roll[0] == 5:
  #       return 50
  #     else:
  #       return 0
  #   elif len(roll) == 2:
  #     if roll[0] == roll[1] and roll[0] == 1:
  #       return 200
  #     elif roll[0] == roll[1] and roll[0] == 5:
  #       return 100
  #     else:
  #       return 0
  #   elif len(roll) == 3:
  #     if 






    # score_rules = [
    #   ((), 0),
    #   ((1,), 100),
    #   ((1, 1), 200),
    #   ((1, 1, 1), 1000),
    #   ((1, 1, 1, 1), 2000),
    #   ((1, 1, 1, 1, 1), 3000),
    #   ((1, 1, 1, 1, 1, 1), 4000),
    #   ((2,), 0),
    #   ((2, 2), 0),
    #   ((2, 2, 2), 200),
    #   ((2, 2, 2, 2), 400),
    #   ((2, 2, 2, 2, 2), 600),
    #   ((2, 2, 2, 2, 2, 2), 800),
    #   ((3,), 0),
    #   ((3, 3), 0),
    #   ((3, 3, 3), 300),
    #   ((3, 3, 3, 3), 600),
    #   ((3, 3, 3, 3, 3), 900),
    #   ((3, 3, 3, 3, 3, 3), 1200),
    #   ((4,), 0),
    #   ((4, 4), 0),
    #   ((4, 4, 4), 400),
    #   ((4, 4, 4, 4), 800),
    #   ((4, 4, 4, 4, 4), 1200),
    #   ((4, 4, 4, 4, 4, 4), 1600),
    #   ((5,), 50),
    #   ((5, 5), 100),
    #   ((5, 5, 5), 500),
    #   ((5, 5, 5, 5), 1000),
    #   ((5, 5, 5, 5, 5), 1500),
    #   ((5, 5, 5, 5, 5, 5), 2000),
    #   ((6,), 0),
    #   ((6, 6), 0),
    #   ((6, 6, 6), 600),
    #   ((6, 6, 6, 6), 1200),
    #   ((6, 6, 6, 6, 6), 1800),
    #   ((6, 6, 6, 6, 6, 6), 2400),
    #   ((1, 2, 3, 4, 5, 6), 1500),
    #   ((2, 2, 3, 3, 4, 6), 0),
    #   ((2, 2, 3, 3, 6, 6), 1500),
    #   ((1, 1, 1, 2, 2, 2), 1200),
    # ]
    # print(score_rules[3][1])
    # for i in len(score_rules):
    #   if roll == score_rules[i][0]:
    #     return score_rules[i][1]
    #   else:
    #     invalid = print("invalid score")
    #     return invalid
  




    # banked_score = tuple(roll)
    # if banked_score == ():
    #   return 0
    # elif banked_score == (1,):
    #   return 100
    # elif banked_score == (1, 1):
    #   return 200
    # elif banked_score == (1, 1, 1):
    #   return 1000
    # elif banked_score == (1, 1, 1, 1):
    #   return 2000
    # elif banked_score == (1, 1, 1, 1, 1):
    #   return 3000
    # elif banked_score == (1, 1, 1, 1, 1, 1):
    #   return 4000
    # elif banked_score == (2,):
    #   return 0
    # elif banked_score == (2,2):
    #   return 0
    # elif banked_score == (2,2,2):
    #   return 200
    # elif banked_score == (2,2,2,2):
    #   return 400
    # elif banked_score == (2,2,2,2,2):
    #   return 600
    # elif banked_score == (2,2,2,2,2,2):
    #   return 800
    # elif banked_score == (3,):
    #   return 0
    # elif banked_score == (3,3):
    #   return 0
    # elif banked_score == (3,3,3):
    #   return 300
    # elif banked_score == (3,3,3,3):
    #   return 600
    # elif banked_score == (3,3,3,3,3):
    #   return 900
    # elif banked_score == (3,3,3,3,3,3):
    #   return 1200
    # elif banked_score == (4,):
    #   return 0
    # elif banked_score == (4,4):
    #   return 0
    # elif banked_score == (4,4,4):
    #   return 400
    # elif banked_score == (4,4,4,4):
    #   return 800
    # elif banked_score == (4,4,4,4,4):
    #   return 1200
    # elif banked_score == (4,4,4,4,4,4):
    #   return 1600
    # elif banked_score == (5,):
    #   return 50
    # elif banked_score == (5,5):
    #   return 100
    # elif banked_score == (5,5,5):
    #   return 500
    # elif banked_score == (5,5,5,5):
    #   return 1000
    # elif banked_score == (5,5,5,5,5):
    #   return 1500
    # elif banked_score == (5,5,5,5,5,5):
    #   return 2000
    # elif banked_score == (6,):
    #   return 0
    # elif banked_score == (6,6):
    #   return 0
    # elif banked_score == (6,6,6):
    #   return 600
    # elif banked_score == (6,6,6,6):
    #   return 1200
    # elif banked_score == (6,6,6,6,6):
    #   return 1800
    # elif banked_score == (6,6,6,6,6,6):
    #   return 2400
    
    

  @staticmethod
  def roll_dice(dice):
    roll = []
    for _ in range(dice):
      roll.append(random.randint(1, 6))
    print(roll)
    result = tuple(roll)
    print(result)
    return result 