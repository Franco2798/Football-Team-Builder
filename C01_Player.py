import random as r
import pandas as pd

from Enums import E, RequirementNotMet, AttributeDoesNotExist
from data.Complete_names import first_names, last_names

class Player():
    def __init__(self, position = r.choice(E.POSITIONS)):
        # Position must be set to a value that is in Enums.E.POSITIONS if not raise exception RequirementNotMet
        self.position = position
        if self.position not in E.POSITIONS:
            raise RequirementNotMet(str(position)+ ': is not in positions')
        
        self.attribute1 = r.randint(E.MIN,E.MAX)
        self.attribute2 = r.randint(E.MIN,E.MAX)
        self.attribute3 = r.randint(E.MIN,E.MAX)

        #   if 2000 names are generated none should match exactly. 
        self.first_name = str(first_names.sample(1).values[0])
        self.last_name = str(last_names.sample(1).values[0])
        self.name = self.first_name + ' ' + self.last_name
        self.number = r.randint(0, 99)          # this will be a reflection of position eventually and unique on a team for now it is simply initialized (0-99)
        
        #   game level variables these will change throughout the game
        self.location = position[0]        # this will change with time
        self.on_field = r.choice([True, False])       
        self.is_blitzing = r.choice([True, False])
        self.scheme_mod = r.choice([True, False])
        self.man_coverage = 0
        self.zone_coverage = 0

    def generate_random_name(self):
        # this is an optional function to generate a name so you don't clutter you initialize. 
        # you may make as many of these as you wish. Just know I will never call them directly.
        pass

    def get_attribute(self, enumed_attribute):
        # enumertions ATR1,ATR2,ATR3 exist in enums
        # based on the enumed attribute return the correct associated value
        # raise RequirementNotMet if the enumed_attribue is not ATR1 ATR2 or ATR3
        # for example if player.attribute1 = 100
        # then player.get_attribute_enumed_attribute(E.ATR1) should return 100

        if enumed_attribute == self.attribute1:
            return self.attribute1
        elif enumed_attribute == self.attribute2:
            return self.attribute2
        elif enumed_attribute == self.attribute3:
            return self.attribute3
        else:
            raise AttributeDoesNotExist 
    
    def get_col_row_from_location(self):
    
        players_map = {
            # DEFFENSE
            941: (1, 0), 931: (3, 0), 531: (5, 0), 942: (7, 0), 932: (10, 0), 943: (13, 0), 532: (15, 0), 933: (17, 0), 944: (19, 0), 
            201: (1, 1), 202: (2, 1), 203: (3, 1), 204: (4, 1),
            51: (6, 1), 52: (8, 1), 53: (10, 1), 54: (12, 1), 57: (14, 1),
            206: (16, 1), 207: (17, 1), 208: (18, 1), 209: (19, 1),
            90: (7, 2), 91: (8, 2), 92: (9, 2), 93: (10, 2), 94: (11, 2), 95: (12, 2), 96: (13, 2), 97: (14, 2),
            # OFFENSE
            801: (1, 3), 802: (2, 3), 803: (3, 3), 804: (4, 3),
            80: (7, 3), 71: (8, 3), 72: (9, 3), 73: (10, 3), 74: (11, 3), 75: (12, 3), 86: (13, 3),
            806: (16, 3), 807: (17, 3), 808: (18, 3), 809: (19, 3),
            701: (1, 4), 702: (2, 4), 703: (3, 4), 704: (4, 4), 13: (10, 4), 706: (16, 4), 707: (17, 4), 708: (18, 4), 709: (19, 4),
            42: (9, 5), 43: (10, 5), 44: (11, 5),
            21: (8, 6), 22: (9, 6), 23: (10, 6), 24: (11, 6), 25: (12, 6)
        }
        
        if self.location in players_map:
            col, row = players_map[self.location]
        else:
            col, row = None, None
        return col, row
    
    def compete(self, enumed_attribute):

        if self.get_attribute(enumed_attribute) in E.ATR1:
            return r.randint(E.MIN,E.MAX) + self.get_attribute(enumed_attribute)    
        elif self.get_attribute(enumed_attribute) in E.ATR2:
            return r.randint(E.MIN,E.MAX) + self.get_attribute(enumed_attribute)
        elif self.get_attribute(enumed_attribute) in E.ATR3:
            return r.randint(E.MIN,E.MAX) + self.get_attribute(enumed_attribute)
        else:
            raise AttributeDoesNotExist

def main_test_player():
    print('main test player:')
    p = Player(E.FB)    
    p.location = 43
    c,row = p.get_col_row_from_location()
    print("COL ROW",c,row)
    print(p.name)

