from dnd import *

class Consequence:
  def __init__(self):
    self.description = ""
    self.destination = None
    self.transfer = False
    self.modify = False
    

  def resolve(self,character):
    # apply the changes if needed [modify]
    if modify:
        pass
    # control the event flow
    if transfer:
        pass