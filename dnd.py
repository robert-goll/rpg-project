from random import randint
from math import fsum
import copy
from entity import *


# Types of events to consider:
# 1) DIalouge = interactions with NPCS
# 2) Combat  = turn based exchange of rolls and challenges
# 3) Skill Checks = i.e. climbing cliff swimming a raging river 


# ACTION_FUNCTIONS[action](combatant,target,battlefield,gear=None)

ACTION_FUNCTIONS = {
    "MOVE": combat_action_move,
    "INTERACT": pass,
    "EVADE": pass,
    "ASSIT": pass,
    "ATTACK": pass
}

def rollDice(dice_count: int, dice_faces: int) -> list:  # 4d6 , 1d20
    rolls = []
    for roll in range(dice_count):
        rolls.append(randint(1, dice_faces))
    return rolls


def rollSum(dice_count: int, dice_faces: int) -> int:
    result = rollDice(dice_count, dice_faces)
    return int(fsum(result))


def combat_encounter(friendly,hostile):
    initiative_order = combat_build_initiative(friendly.extend(hostile))
    battlefield = {
        "FRIENDLY": {
            "SHORT": [],
            "FAR":[].extend(friendly)
        },
        "HOSTILE":{
            "SHORT": [],
            "FAR":[].extend(hostile)
        }
    }
    done = False
    while not done:
        for combatant in initiative_order:
            if isinstance(combatant, Player):  # <class 'entity.Player'>:
                #TODO - Add a menu for a choice of actions
                action = combat_action_menu(combatant)
                target = combat_target_menu(combatant,initiative_order)
                #TODO - Add a follow up menu for actions against the target
                temp_action = action.split('-')
                gear = None
                if len(temp_action) > 1:
                    gear_description = temp_action[1]
                    for item in combatant.character_gear:
                        if item.description == gear_description:
                            gear = item
                            break
                action = temp_action[0]
                ACTION_FUNCTIONS[action](combatant,target,battlefield,gear)
            else:
                pass
                
    #TODO - Were going to need something to track distance

def combat_target_menu(player,targets):
    valid = False
    target= None
    while not valid:
        for i in range(len(targets)):
            if target[i].character_name != "": 
                print(f"{i+1}) {targets[i].character_name}")
            elif target[i].description != "":
                print(f"{i+1}) {targets[i].description}")
            else:
                print(f"{i+1}) <GENERIC ENTITY>")
        userInput = input(":> ")
        if userInput.isdecimal() and 1 <= int(userInput) <= len(targets):
            valid = True
            target = targets[int(userInput)]
        else:
            print(f"Invalid Input, please enter a number between 1 and {len(targets)}")
    return target
    
    
 #TODO - we need to finish this function: it is a copy-paste of combat_target_menu
def combat_action_menu(player):
    valid = False
    action= None
    actions = []
    actions.extend(player.combat_actions)
    if len(player.character_gear["COMBAT"]) > 0:
        for item in player.character_gear["COMBAT"]:
            for act in item.actions:
                actions.append(act + "-" +item.description)
    while not valid:
        for i in range(len(actions)):
            print(f"{i+1}) {actions[i]}")
        userInput = input(":> ")
        if userInput.isdecimal() and 1 <= int(userInput) <= len(actions):
            valid = True
            action = actions[int(userInput)]
        else:
            print(f"Invalid Input, please enter a number between 1 and {len(actions)}")
    return action
       

       
''' combat actions:
        attack<specific weapon> 
'''


def combat_build_initiative(args):
    initiative_order = []
    for combatant in args:
        i = combatant.getInitiative()
        index = 0
        for index in range(len(initiative_order)):
            if initiative_order[index][0] <= i:
                break
        initiative_order.insert(index, (i, combatant))
    return initiative_order

    
def combat_action_move(combatant, target, battlefield, gear):
    if combatant in battlefield["FRIENDLY"]["SHORT"]:
        battlefield["FRIENDLY"]["SHORT"].remove(combatant)
        battlefield["FRIENDLY"]["FAR"].append(combatant)
    elif combatant in battlefield["FRIENDLY"]["FAR"]:
        battlefield["FRIENDLY"]["FAR"].remove(combatant)
        battlefield["FRIENDLY"]["SHORT"].append(combatant)
    elif combatant in battlefield["HOSTILE"]["SHORT"]:
        battlefield["HOSTILE"]["SHORT"].remove(combatant)
        battlefield["HOSTILE"]["FAR"].append(combatant)
    elif combatant in battlefield["HOSTILE"]["FAR"]:
        battlefield["HOSTILE"]["FAR"].remove(combatant)
        battlefield["HOSTILE"]["SHORT"].append(combatant)
        
        
# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ...
