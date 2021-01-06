from random import randint
from math import fsum

# Types of events to consider:
# 1) DIalouge = interactions with NPCS
# 2) Combat  = turn based exchange of rolls and challenges
# 3) Skill Checks = i.e. climbing cliff swimming a raging river 

def rollDice(dice_count,dice_faces): # 4d6 , 1d20
  rolls = []
  for roll in range(dice_count):
    rolls.append(randint(1,dice_faces))
  return rolls

def rollSum(dice_count,dice_faces):
  result = rollDice(dice_count,dice_faces)
  return int(fsum(result))

# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ... 