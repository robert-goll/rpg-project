from random import randint
from math import fsum

def rollDice(dice_count: int, dice_faces: int) -> list:  # 4d6 , 1d20
    rolls = []
    for roll in range(dice_count):
        rolls.append(randint(1, dice_faces))
    return rolls


def rollSum(dice_count: int, dice_faces: int) -> int:
    result = rollDice(dice_count, dice_faces)
    return int(fsum(result))