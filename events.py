from requirements import *
import dnd


# CLASSES FOR events - The nodes of our story graph
class Event:
    def __init__(self):
        self.description = ""
        self.requirements = []
        self.paths = []
        self.path_text = []

    def __repr__(self):
        return self.description

    def addPath(self, event):
        self.paths.append(event)

    def removePath(self, event):
        self.paths.remove(event)

    def addRequirement(self, requirement):
        self.requirements.append(requirement)

    def removeRequirement(self, requirement):
        self.requirements.remove(requirement)

    def resolve(self, character):  # took out path_choice <--
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
                # outputEvent(self.paths[path_choice]) <--
                path_choice = outputEvent(self)  # <--
                self.paths[path_choice].resolve(character)
            else:
                # Testing Code
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
            temp = "%d) %s" % (i + 1, event.path_text[i])
            temp1 = ""
            # TODO - modify to accommodate output of multiple requirements; currently only the first.
            if len(event.paths[i].requirements) > 0:
                temp1 = "<%s:%s>" % (
                event.paths[i].requirements[0].req_type, event.paths[i].requirements[0].req_type_sub)
            print(temp + temp1)
        userInput = input(":> ")
        if userInput.isdecimal() and (0 <= int(userInput) <= len(event.path_text)):
            valid = True
        else:
            print("Invalid Input, please enter a number between 1 and %d" % (len(event.path_text)))
    return int(userInput) - 1


def input_story(inputFile: str) -> list:
    f = open(inputFile)
    count = int(f.readline())
    nodes = []
    for i in range(count):
        print(f"node{i + 1}...")
        description = f.readline()
        temp = f.readline()
        requirements = []
        print("grabbing requirements")
        while (temp != '*\n'):
            requirements.append(temp)
            temp = f.readline()
        temp = f.readline()
        paths = []
        print("grabbing path descriptions")
        while (temp != '\n'):
            paths.append(temp)
            temp = f.readline()
        nodes.append((description, requirements, paths))
    f.close()
    return nodes


def build_story(eventInfo):
    events = []
    # Main loop to build each Event object
    for event in eventInfo:
        temp = Event()
        temp.description = event[0]
        events.append(temp)
        # Loop to build each requirement object for an Event
        for req in event[1]:
            temp = Requirement()
            text = req[:-1]
            text = text.split('-')
            temp.req_type = text[0]
            temp.req_type_sub = text[1]
            temp.req_rating = int(text[2])
            events[-1].requirements.append(temp)
        # Loop to insert each path(raw) to the Event
        for path in event[2]:
            events[-1].path_text.append(path[:-1])
        # Loop to clean up path(raw) and link associated events
    for event in events:
        for i in range(len(event.path_text)):
            temp = event.path_text[i].split('-')
            event.path_text[i] = temp[1]
            event.addPath(events[int(temp[0]) - 1])
    return events[0]
