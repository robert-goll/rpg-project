from random import randint
from math import fsum
import copy
from entity import *


# Types of events to consider:
# 1) DIalouge = interactions with NPCS
# 2) Combat  = turn based exchange of rolls and challenges
# 3) Skill Checks = i.e. climbing cliff swimming a raging river 

def rollDice(dice_count: int, dice_faces: int) -> list:  # 4d6 , 1d20
    rolls = []
    for roll in range(dice_count):
        rolls.append(randint(1, dice_faces))
    return rolls


def rollSum(dice_count: int, dice_faces: int) -> int:
    result = rollDice(dice_count, dice_faces)
    return int(fsum(result))


def combat_encounter(*args):
    initiative_order = combat_build_initiative(args)
    done = False
    while not done:
        for combatant in initiative_order:
            if isinstance(combatant, Player):  # <class 'entity.Player'>:
                #TODO - Add a menu for a choice of actions
                target = combat_target_menu(combatant,initiative_order)
                #TODO - Add a follow up menu for actions against the target
            else:
                pass

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
    
def combat_target_menu(player):
    valid = False
    action= None
    actions = []
    actions.extend(player.combat_actions)
    if len(player.character_gear["COMBAT"]) > 0:
        
    while not valid:
        for i in range(len(actions)):
            if action[i].character_name != "": 
                print(f"{i+1}) {actions[i].character_name}")
            elif action[i].description != "":
                print(f"{i+1}) {actions[i].description}")
            else:
                print(f"{i+1}) <GENERIC ENTITY>")
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

# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ...
