from random import randint
from math import fsum

# Types of events to consider:
# 1) DIalouge = interactions with NPCS
# 2) Combat  = turn based exchange of rolls and challenges
# 3) Skill Checks = i.e. climbing cliff swimming a raging river 

def rollDice(dice_count: int,dice_faces: int) -> list: # 4d6 , 1d20
  rolls = []
  for roll in range(dice_count):
    rolls.append(randint(1,dice_faces))
  return rolls

def rollSum(dice_count: int,dice_faces: int) -> int:
  result = rollDice(dice_count,dice_faces)
  return int(fsum(result))
  
def input_story(inputFile: str) -> list:
  f = open(inputFile)
  count = int(f.readline())
  nodes = []
  for i in range(count):
    print(f"node{i+1}...")
    description = f.readline()
    temp = f.readline()
    requirements = []
    print("grabbing requirements")
    while(temp != '*\n'):
      requirements.append(temp)
      temp = f.readline()
    temp = f.readline()
    paths = []
    print("grabbing path descriptions")
    while(temp != '\n'):
      paths.append(temp)
      temp = f.readline()
    nodes.append((description,requirements,paths))
  f.close()
  return nodes

# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ... 