from dnd import *
from test_adventure import *

if __name__=='__main__':
  '''
  myNPC = NPC() 
  print(myNPC.character_name)
  myNPC.character_name = "Steve"
  otherNPC = NPC()
  print(myNPC.character_name)
  otherNPC.character_name = "Uncle Bob"
  print(otherNPC.character_name)
  '''
  '''
  rootEvent = Event()
  rootEvent.description = "Brandybuck Inn"

  oEvent1 = Event()
  oEvent1.description = "Battle on the Hill"
  rootEvent.addPath(oEvent1)

  oEvent2 = Event()
  oEvent2.description = "Journey through the Sewers"
  rootEvent.addPath(oEvent2)

  oEvent3 = Event()
  oEvent3.description = "Showdown at Quartz Ridge"
  rootEvent.addPath(oEvent3)

  oEvent1.addPath(oEvent3)
  oEvent2.addPath(oEvent3)

  req1 = Requirement()
  req1.description = "Climb the cliff."
  req1.req_type = "SKILL"
  req1.req_type_sub = "athletics"
  req1.req_rating = 14
  req2 = Requirement()
  req3 = Requirement()
  '''

  '''
  print("Start of the journey at %s"%rootEvent.description)
  for path in rootEvent.paths:
    print("\tcontinued through %s"%path)
    for innerPath in path.paths:
      print('\t\t journey ends at %s'%innerPath)
      '''
      
  nodes = input_story("test_adventure.txt")
  print(nodes)
  player = Player()
  #story = build_test_adventure()
  story = build_story(nodes)
  story.resolve(player)
  
'''
  info = []
  f = open("test_adventure.txt")
  temp = None
  while temp != "":
    temp = f.readline()
    if temp != "":
        info.append(temp)
  f.close()
  
  for s in info:
    print(s)
'''