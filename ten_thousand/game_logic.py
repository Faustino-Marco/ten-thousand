from collections import Counter
import random

class GameLogic:
  def __init__(self):
    pass

  @staticmethod
  def calculate_score(roll):
    banked_score = tuple(roll)
    if banked_score == (1,):
      return 100
    elif banked_score == (1, 1):
      return 200

  @staticmethod
  def roll_dice(dice):
    roll = []
    for _ in range(dice):
      roll.append(random.randint(1, 6))
    print(roll)
    result = tuple(roll)
    print(result)
    return result 