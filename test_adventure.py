from dnd import *


def build_test_adventure():
  #Create the events
  rootEvent = Event()  # The Start Point
  rootEvent.description = "Brandybuck Inn"

  oEvent1 = Event()
  oEvent1.description = "Battle on the Hill"


  oEvent2 = Event()
  oEvent2.description = "Journey through the Sewers"


  oEvent3 = Event()  # The End Point
  oEvent3.description = "Showdown at Quartz Ridge"
  #Create test requirements
  req1 = Requirement()
  req1.req_type = "ATTR"
  req1.req_type_sub = "CHA"
  req1.rating = 14
  #Add requirements to events
  oEvent1.requirements.append(req1)

  #Link the events
  rootEvent.path_text.append("In the corner a stalwart looking guard discusses tactics with his men.")
  rootEvent.addPath(oEvent1) # From the start we can go three places

  rootEvent.path_text.append("Some questionable looking indivduals are attempting to remain inconspicuous in the corner.")
  rootEvent.addPath(oEvent2)

  rootEvent.path_text.append("Lorentz, the Guild Mage, awaits near the bar.")
  rootEvent.addPath(oEvent3) 

  #Set up the path text for the choice menu shown to the Players

  # Two of the other paths link to the third themselves
  oEvent1.path_text.append("A massive battle is unfolding, attempt to charge into the fray.")
  oEvent1.addPath(oEvent3) 
  oEvent2.path_text.append("Laughing can be heard coming from deeper in the tunnel.")
  oEvent2.addPath(oEvent3)

  return rootEvent # Return the start of the story