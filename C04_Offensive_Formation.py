from Enums import E, RequirementNotMet
# these are necessary for testing but not for implementation
from C01_Player import Player as P
from C02_Team import Team as T
from C03_Formation import Formation 
from C06_Field import Field
import random as r

class OffensiveFormation(Formation):
    def __init__(self, name, tes=[], wrs=[], fbs=[], rbs=[], shotgun = False):
        super().__init__()
        
        # arguments are lists of locations
        # e.g. tes = [80,886] --> line up 2 tight ends at location 0 and 86
        #   translates to location information 80 and 886
        
        self.name = name
        self.tes = tes
        self.wrs = wrs
        self.fbs = fbs
        self.rbs = rbs
        self.shotgun = shotgun
        
        self.set_positions()
        
    def set_positions(self):
        # fill self.positions with those positions in this formation
        self.positions.extend(['TE', 'WR', 'FB', 'RB', 'LT', 'LG', 'CC', 'RG', 'RT', 'QB'])
        
    
    def lineup(self, team:T):
        # refer to Enums for location diagram
        # use instructions such as self.wrs to set player locations
        #   e.g. if self.wrs = [803,805] then set 1 player with position E.WR to location 803 and the other to 805
        # linemen [E.LT, E.LG, E.CC, E.RG, E.RT] are always in the same spot
        # E.QB is either behind center location (13) or if in shotgun back one row (location 23)

        for pos in [E.LT, E.LG, E.C, E.RG, E.RT]:
            for player in team.players:
                if player.position == pos:
                    player.on_field = True
                    break

        for player in team.players:
            if player.position == E.QB:
                player.on_field = True
                break
        if self.shotgun:
            if player.position == E.QB:
                player.location = 43
        
        if len(self.tes) != 0:
            amount_tes = 0
            for player in team.players:
                if player.position == E.TE:
                    if amount_tes < len(self.tes):
                        player.on_field = True
                        player.location = self.tes[amount_tes]
                        amount_tes += 1
                    else: 
                        break

        if len(self.wrs) != 0:
            amount_wrs = 0
            for player in team.players:
                if player.position == E.WR:
                    if amount_wrs < len(self.wrs):
                        player.on_field = True
                        player.location = self.wrs[amount_wrs]
                        amount_wrs += 1
                    else: 
                        break

        if len(self.fbs) != 0:
            amount_fbs = 0
            for player in team.players:
                if player.position == E.FB:
                    if amount_fbs < len(self.fbs):
                        player.on_field = True
                        player.location = self.fbs[amount_fbs]
                        amount_fbs += 1
                    else: 
                        break

        if len(self.rbs) != 0:
            amount_rbs = 0
            for player in team.players:
                if player.position == E.RB:
                    if amount_rbs < len(self.rbs):
                        player.on_field = True
                        player.location = self.rbs[amount_rbs]
                        amount_rbs += 1
                    else: 
                        break

        for player in team.players:
            if player.on_field == True:
                if player.location not in self.players_map:
                    player.on_field = False

        for player in team.players:
            if player.position == E.TE:
                if player.on_field == True:
                    xte, yte = player.get_col_row_from_location()
                    if xte < 10:
                        left = True
                    else:
                        left = False
        
        if left:
            for player in team.players:
                if player.on_field == True:
                    locations_left = [801, 802, 803, 804]
                    if player.location in locations_left:
                        player.location -= 100
                        break
        else:
            for player in team.players:
                if player.on_field == True:
                    locations_right = [806, 807, 808, 809]
                    if player.location in locations_right:
                        player.location -= 100
                        break
        players_in_first_line = []
        for player in team.players:
            if player.on_field == True:
                col, row = player.get_col_row_from_location()
                if row == 3:
                    players_in_first_line.append(player.position)
        if len(players_in_first_line) > 7:
            for player in team.players:
                if player.location in [801, 802, 803, 804, 806, 807, 808, 809]:
                    player.location -= 100
                    break
        

                   
        

    def get_eligible_receivers(self, team):
        # returns a list of eligible receivers in this formation
        # eligible positions are WR, TE, RB, FB
        eligible_positions = [E.WR, E.TE, E.RB, E.FB]
        eligible_receivers = []

        for player in team.players:
            if player.position in eligible_positions:
                eligible_receivers.append(player)

        return eligible_receivers
    

def test_formation(f,t):
    f.set_on_field(t)
    t.get_name_and_position_of_players_on_field()
    f.lineup(t)
    field = Field()
    valid = field.update_grid(t,None)
    if valid:
        field.display_grid()

def main_test_offensive_formation():
    print("main test offensive formation:")
    t = T()
    t.create_default_team()
    f1 = OffensiveFormation('Single Back',tes = [80], fbs = [], rbs = [23], wrs = [801,803,806])
    f2 = OffensiveFormation('I-Back', tes = [86], fbs=[43],rbs=[23],wrs=[801,806])
    f3 = OffensiveFormation('Trips Right', tes=[80],wrs=[804,806,807], rbs = [23], shotgun=True)
    # A trips single back formation has a tightend on the left, no fullbacks, a running back behind the qb and three wrs to the right
    test_formation(f1,t)
    test_formation(f2,t)
    test_formation(f3,t)


    

    


