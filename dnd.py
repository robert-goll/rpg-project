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
                ACTION_FUNCTIONS[action](combatant,target,friendly,hostile,battlefield,gear)
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

    
def combat_action_move(combatant, target, friendly, hostile, battlefield, gear):
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
        
def combat_action_attack(combatant, target, friendly, hostile, battlefield, gear):
    relation = None
    if combatant in friendly and target in friendly:
        relation = 0
    elif combatant in hostile and target in hostile:
        relation = 1
    elif combatant in friendly:
        relation = 2
    elif combatant in hostile:
        relation = 3
    
    combatant_pos = None
    target_pos = None
    
    match relation:
        case 0:
            if combatant in battlefield["FRIENDLY"]["SHORT"]:
                combatant_pos = 0
            else:
                combatant_pos = 1
            if target in battlefield["FRIENDLY"]["SHORT"]:
                target_pos = 0
            else:
                target_pos = 1
        case 1:
            if combatant in battlefield["HOSTILE"]["SHORT"]:
                combatant_pos = 2
            else:
                combatant_pos = 3
            if target in battlefield["HOSTILE"]["SHORT"]:
                target_pos = 2
            else:
                target_pos = 3
        case 2:
            if combatant in battlefield["FRIENDLY"]["SHORT"]:
                combatant_pos = 0
            else:
                combatant_pos = 1
            if target in battlefield["HOSTILE"]["SHORT"]:
                target_pos = 2
            else:
                target_pos = 3
        case 3:
            if target in battlefield["FRIENDLY"]["SHORT"]:
                target_pos = 0
            else:
                target_pos = 1
            if combatant in battlefield["HOSTILE"]["SHORT"]:
                combatant_pos = 2
            else:
                combatant_pos = 3
        if abs(combatant_pos-target_pos) > 2:
            if gear.sub_type  == "MELEE":
                print("The attack fails!")
                return           
        else:
            if gear.sub_type == "RANGED":
                print("The attack fails!")
                return
        target_ac = target.getArmorClass()
        attack_mod = None
        if gear.sub_type  == "MELEE":
            attack_mod = combatant.getAttributeModifier("STR")
        else:
            attack_mod = combatant.getAttributeModifier("DEX")
        combatant_attack = rollDice(1,20) + attack_mod + gear_modifier
        if combatant_attack >= target_ac:
            damage = gear.damage.split('d')
            damage = rollDice(damage[0],damage[1]
            target.changeHP(damage)
            print(f"{target.description} was hit for {damage} damage!")
        
# <General description / narrative description>
# 1) Option 1 <STR>
# 2) Option 2 <CHA>
# 3) Fight
#  ...
