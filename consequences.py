from dnd import *

class Consequence:
  def __init__(self):
    self.description = ""
    self.destination = None
    self.modify = False
    self.con_type = "" # - ATTR , SKILL, HP, GEAR, PARTY, XP
    self.con_sub_type = "" # e.g. ATTR -> {STR,CON,DEX,...}
    self.value = 0
    
    # health, equipment/currency/valuables, skills, attributes, NPC
    

  def resolve(self,character):
    # apply the changes if needed [modify]
    if self.modify:
        if self.con_type == 'ATTR':
            character.change_attribute(self.con_sub_type,self.value)
        elif self.con_type == 'SKILL':
            character.change_skill(self.con_sub_type,self.value)
        elif self.con_type == 'HP':
            character.change_HP(self.value)
        elif self.con_type == 'XP':
            character.change_XP(self.value)
        elif self.con_type == 'GEAR':
            pass
        elif self.con_type == 'PARTY':
            pass
    # control the event flow
    if self.destination:
        self.destination.resolve(character)