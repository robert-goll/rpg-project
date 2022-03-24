from dnd import *


class Requirement:
    def __init__(self):
        self.description = ""
        self.req_type = "ATTR"  # 'ATTR' -> attribute, 'SKILL' -> skills, 'COMBAT' - > You know what this is
        self.req_type_sub = "STR"
        self.req_rating = 10
        self.consequence = None
        self.hostiles = []

        def addConsequence(consequence):
            self.consequence = consequence

        def removeConsequence(consequence):
            self.consequence = None

    def resolve(self, character):
        result = -1000
        if self.req_type == "ATTR":
            result = character.getAttributeModifer(self.req_type_sub) + rollSum(1, 20)
        elif self.req_type == "SKILL":
            result = character.character_skills[self.req_type_sub] + rollSum(1, 20)
        elif self.req_type == "COMBAT":
            result = combat_encounter([character],self.hostiles)
        for gear in character.character_gear[self.req_type]:
            if gear.gear_subType == self.req_type_sub:
                result += gear.gear_modifier
            # TODO - Implement combat loop function
        else:
            pass
        #TODO - Consider removing this output if we end up using a graphic renderer
        print(f"...testing...{self.req_type}:{self.req_type_sub}:{self.req_rating}...")
        print(f"...rolled {result}...")
        if result >= self.req_rating:
            return True
        else:
            if self.consequence != None:
                self.consequence.resolve()
            else:
                return False
