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
    self.character_gender = ""

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
  
self.character_gear = {
  "armor": [],
  "weapns": [],
  "consumables": [],
  "trinkets": []
}

  def getAttributeModifer(self, attribute):
    return (self.character_attributes[attribute] - 10) // 2

  def getArmorClass(self):
    return self.getAttributeModifier('DEX')

class Player(NPC):
  def __init__(self):
    NPC.__init__(self)

class Gear(Entity):
  def __init__(self):
    Entity.__init__(self)