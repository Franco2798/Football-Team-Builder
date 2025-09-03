from C06_Field import Field
from C02_Team import Team as T
from C01_Player import Player as P
from Enums import E
import math


class Formation:
    def __init__(self):
        self.positions = []
        self.locations = []
        self.players_map = {
            # DEFENSE
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

    def reset_on_field(self, team):
        # resets on_field to False for all players on team
        # sets on_field to True for players in positions in self.positions
        if not isinstance(team, T):
            raise TypeError("team must be a Team class")
    
        for player in team.players:
            player.on_field = False
        
    

    def get_players_within_d_distance_of_location(self, location, team, d):
        # returns a list of players within d distance of location
        # note this is distance in terms of both rows and columns
        # if location was 71 then x,y = 8,3
        if not isinstance(team, T):
            raise TypeError("team must be a Team class")
        
        players_within_distance = []
        

        if location in self.players_map:
            col_of_refference, row_of_refference = self.players_map[location]
        else:
            raise TypeError("location must be a valid location")

        for player in team.get_players_on_field():
            name = player.name
            x,y = player.get_col_row_from_location()
            if x is None or y is None:
                pass
            else:
                distance = math.sqrt((x-col_of_refference)**2 + (y-row_of_refference)**2)
                if distance <= d:
                    players_within_distance.append(player)

        return players_within_distance
        

def main_test_formation():
    print("main test formation:")
    

    players = [
        P(position=(13, 'QB', 2)),
        P(position=(800, 'WR', 5)),
        P(position=(20, 'RB', 3)),
        P(position=(90, 'DL', 6)),
        P(position=(50, 'LB', 6)),
        P(E.RT)
    ]
    
    team = T(name="Test Team", players=players)
    
    formation = Formation()
    formation.positions = ['QB', 'LT', 'RB', 'RT', 'KR']
    
    formation.reset_on_field(team)
    on_field_players = team.get_players_on_field()
    print("Players on field", [(p.name, p.position[1]) for p in on_field_players])

    location = 71
    d = 10  
    players_within_distance = formation.get_players_within_d_distance_of_location(location, team, d)
    print("Players within d distance:", [(p.name, p.position[1], p.location) for p in players_within_distance])

