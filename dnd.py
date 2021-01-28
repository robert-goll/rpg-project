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


def build_story(eventInfo):
  events = []
  requirements = []
  for event in eventinfo:
    temp = Event()
    temp.description = event[0]
    events.append(temp)
    reqs = []
    for req in event[1]:
      temp = Requirement()
      text = req[:-1]
      text = text.split('-')
      temp.req_type = text[0]
      temp.req_type_sub = text[1]
      temp.rating = int(text[2])
      reqs.append(temp)
    requirements.append(reqs)
    for path in event[2]:
      events[-1].path_text.append(pat[:-1])

# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ... 