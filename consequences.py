from dnd import *

class Consequence:
  def __init__(self):
    self.description = ""
    self.destination = None
    self.modify = False
    self.con_type = "" # - ATTR , SKILL, HP, GEAR, PARTY, XP
    self.con_sub_type = "" # e.g. ATTR -> {STR,CON,DEX,...}
    
    # health, equipment/currency/valuables, skills, attributes, NPC
    

  def resolve(self,character):
    # apply the changes if needed [modify]
    if self.modify:
        if self.con_type == 'ATTR':
            pass
        elif self.con_type == 'SKILL':
            pass
        elif self.con_type == 'HP':
            pass
        elif self.con_type == 'XP':
            pass
        elif self.con_type == 'GEAR':
            pass
        elif self.con_type == 'PARTY':
            pass
    # control the event flow
    if self.destination:
        self.destination.resolve(character)