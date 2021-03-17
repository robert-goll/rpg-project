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

def combat_encounter(*args):
  initiative_order = combat_build_initiative(args)
  done = False
  while !done:
    for combatant in initiative_order:
      if type(combatant) == <class 'entity.Player'>:
        pass
      else:
        pass
      
''' combat actions:
        attack<specific weapon>
        
'''
    
    
def combat_build_initiative(args):
  initiative_order = []
  for combatant in args:
    i = combatant.getInitiative()
    index = 0
    for index in range(len(initiative_order)):
      if initiative_order[index][0] <= i:
        break
    initiative_order.insert(index,(i,combatant))
  return initiative_order
  
# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ... 