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