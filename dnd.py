from random import randint
from math import fsum

races = {
  'human': {
    'name': 'Human',
    'attributes': [0,0,0,0,0,0],
    'features': 0
  },
  'elf': {
    'name': 'Elf',
    'attributes': [0,2,0,0,1,0],
    'features': 0
  }
}

classes = {
  'fighter': {
    'name': 'Fighter',
    'features': 0
  },
  'wizard': {
    'name': 'Wizard',
    'features': 0
  }
}

#CLASSES FOR ENTITIES
class Entity: #BASE CLASS FOR OUR GAME
  def __init__(self):
    self.description = "test"
    self.active = True

  def isAlive(self):
    return self.active

class NPC(Entity):
  def __init__(self):
    Entity.__init__(self)
    self.character_name = ""
    self.character_class = [""]
    self.character_level = [0]
    self.character_experience = 0
    self.character_alignment = "TN"
    self.character_race = [""]
    self.character_sex = ""

    self.character_attributes = {
      "STR" : 10,
      "DEX" : 10,
      "CON" : 10,
      "INT" : 10,
      "WIS" : 10,
      "CHA" : 10
    }
    self.character_totalHP = 10
    self.character_currentHP = 10

    self.character_skills = {
      "athletics" : 0,
      "acrobatics": 0,
      "endurance" : 0,
      "knowledge" : 0,
      "nature"    : 0,
      "social"    : 0
    }
  
  def getAttributeModifer(self, attribute):
    return (self.character_attributes[attribute] - 10) // 2

class Player(NPC):
  def __init__(self):
    NPC.__init__(self)

#CLASSES FOR events - The nodes of our story graph
class Event:
  def __init__(self):
    self.description = ""
    self.requirements = []
    self.paths = []
    self.path_text = []

  def __repr__(self):
    return self.description

  def addPath(self,event):
    self.paths.append(event)

  def removePath(self,event):
    self.paths.remove(event)

  def addRequirement(self,requirement):
    self.requirements.append(requirement)

  def removeRequirement(self,requirement):
    self.requirements.remove(requirement)

  def resolve(self,character): # took out path_choice <--
    success = False
    if len(self.requirements) > 0:
      for requirement in self.requirements:
        if not requirement.resolve(character):
          break
        if requirement == self.requirements[-1]:
          success = True 
    else:
      success = True  # added earlier
    if success:
      if len(self.paths) > 0:
        #outputEvent(self.paths[path_choice]) <--
        path_choice = outputEvent(self) #<--
        self.paths[path_choice].resolve(character)
      else:
        #Testing Code
        print("Reached the End!")
    else:
      print("Failed Requirements!")
    # add the code to resolve the event

class Requirement:
  def __init__(self):
    self.description = ""
    self.req_type = "ATTR" # 'ATTR' -> attribute, 'SKILL' -> skills
    self.req_type_sub = "STR"
    self.req_rating = 10

  def resolve(self,character):
    result = -1000
    if self.req_type == "ATTR":
      result = character.getAttributeModifer(self.req_type_sub) + rollSum(1,20)
    elif self.req_type == "SKILL":
      result = character.character_skills[self.req_type_sub] + rollSum(1,20)
    else:
      pass
    return result >= self.req_rating

class Consequences:
  def __init__(self):
    self.description = ""
    self.paths = []

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

def outputEvent(event):
  valid = False
  userInput = ""
  while not valid:
    print(event.description)
    for i in range(len(event.path_text)):
      print("%d) %s"%(i+1,event.path_text[i]))
    userInput = input(":> ")
    if userInput.isdecimal() and (0 <= int(userInput) <= len(event.path_text)):
      valid = True
    else:
      print("Invalid Input, please enter a number between 1 and %d"%(len(event.path_text)))
  return int(userInput) - 1


# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ... 