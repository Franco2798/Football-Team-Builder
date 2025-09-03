from Enums import E, RequirementNotMet
from C01_Player import Player as P
from C02_Team import Team as T
from C03_Formation import Formation 
from C06_Field import Field
from C04_Offensive_Formation import OffensiveFormation
import random as r

class DefensiveFormation(Formation):
    def __init__(self, name, dl, lbs, cbs, sfs, shotgun=False):
        super().__init__()
        
        # dl, lbs arguments are lists of locations
        # e.g. dl = [90,92,94,96] --> line up 4 DL at locations 90, 92,94,96
        # cbs and sfs are just the number on the field as their location is dependent on the offensive formation
        # NOTE: sometimes a lb will change location if man coverage but that doesn't need to be covered here
        
        self.name = name
        self.dl = dl
        self.lbs = lbs
        self.cbs = cbs
        self.sfs = sfs
        self.shotgun = shotgun

        
        self.set_positions()
        
    def set_positions(self):
        # fill self.positions with those positions in this formation
        self.positions.extend(['DL', 'LB', 'CB', 'S'])
        
    
    def lineup(self, team:T):
    
        if len(self.dl) != 0:
            amount_dls = 0
            for player in team.players:
                if player.position == E.DL:
                    if amount_dls < len(self.dl):
                        player.on_field = True
                        player.location = self.dl[amount_dls]
                        amount_dls += 1
                    else:
                        break

        if len(self.lbs) != 0:
            amount_lbs = 0
            for player in team.players:
                if player.position == E.LB:
                    if amount_lbs < len(self.lbs):
                        player.on_field = True
                        player.location = self.lbs[amount_lbs]
                        amount_lbs += 1
                    else:
                        break

        cb_locations = [201, 202, 203, 204, 206, 207, 208, 209]
        if self.cbs > 0:
            amount_cbs = 0
            for player in team.players:
                if player.position == E.CB:
                    if amount_cbs < self.cbs:
                        player.on_field = True
                        player.location = r.choice(cb_locations)
                        cb_locations.remove(player.location)
                        amount_cbs += 1
                    else:
                        break

        sf_locations = [932, 942, 943, 931, 933, 941, 944]
        if self.sfs > 0:
            amount_sfs = 0
            for player in team.players:
                if player.position == E.S:
                    if amount_sfs < self.sfs:
                        player.on_field = True
                        player.location = sf_locations[0]
                        sf_locations.pop(0)
                        amount_sfs += 1
                    else:
                        break

# FUNCTION TO CORRECT DEFFENSIVE LINEUP: a) corners shuld lineup againts receivers, if there's a receiver free lineup lb and finally with a safety
# b) lb preference is TE or FB or RB
# c) a safety prefers to stay in his position
# d) if theres a TE a DL faced with that TE is gonna be in front or outside him, same with the LT
    def adjust_lineup(self, ot:T, dt:T):

        offense_players_on_field = ot.get_players_on_field()
        defense_players_on_field = dt.get_players_on_field()
        
        pos_wr = []
        pos_te = []
        
        for player in offense_players_on_field:
            if player.position == E.WR:
                pos_wr.append(player.location)
            elif player.position == E.TE:
                pos_te.append(player.location)
        
        te_covered = False
        lt_covered = False
        if pos_te[0] == 80:
            for player in defense_players_on_field:
                if player.location == 90:
                    te_covered = True
                elif player.location == 91:
                    lt_covered = True
            if not te_covered:
                for player in defense_players_on_field:
                    if player.position == E.DL:
                        player.location = 90
                        te_covered = True
                        break
            if not lt_covered:
                for player in defense_players_on_field:
                    if player.position == E.DL and player.location != 90:
                        player.location = 91
                        lt_covered = True
                        break
        elif pos_te[0] == 86:
            for player in defense_players_on_field:
                if player.location == 96:
                    te_covered = True
                elif player.location == 91:
                    lt_covered = True
            if not te_covered:
                for player in reversed(defense_players_on_field):
                    if player.position == E.DL:
                        player.location = 96
                        te_covered = True
                        break
            if not lt_covered:
                for player in defense_players_on_field:
                    if player.position == E.DL:
                        player.location = 91
                        lt_covered = True
                        break
        
        updated_positions_covering = []
        defensive_row_covering = 200

        for pos in pos_wr:
            col_wr = pos%100
            new_pos_cb = defensive_row_covering + col_wr
            updated_positions_covering.append(new_pos_cb)
        for player in defense_players_on_field:
            if player.position == E.CB:
                player.location = updated_positions_covering[0]
                updated_positions_covering.pop(0)
        
        if updated_positions_covering:          
            for player in reversed(defense_players_on_field):
                if player.position == E.LB and updated_positions_covering:
                    player.location = updated_positions_covering[0]
                    updated_positions_covering.pop(0)


        


def test_formation(fo:OffensiveFormation, fd:DefensiveFormation, ot:T, dt:T):
    print("Lineups")
    fo.reset_on_field(ot)
    fo.lineup(ot)
    fd.reset_on_field(dt)
    fd.lineup(dt)
    field = Field()
    valid = field.update_grid(ot, dt)
    if valid:
        field.display_grid()
    # From now on it's my code
    print("Adjusted Lineup")
    fd.adjust_lineup(ot, dt)
    field = Field()
    valid = field.update_grid(ot, dt)
    if valid:
        field.display_grid()


def main_test_both_formations():    
    ot = T(name="49ers")
    ot.create_default_team()
    dt = T(name="Packers")
    dt.create_default_team()

    f1o = OffensiveFormation('Single Back',tes = [80], fbs = [], rbs = [23], wrs = [801,803,806])
    f2o = OffensiveFormation('I-Back', tes = [86], fbs=[43],rbs=[23],wrs=[801,806])
    f3o = OffensiveFormation('Trips Right', tes=[80],wrs=[804,806,807], rbs = [23], shotgun=True) 
    f1d = DefensiveFormation('4-4',dl = [90,92,94,96], lbs = [51,52,54,57],cbs = 2, sfs = 1)
    f2d = DefensiveFormation('6-2',dl = [90,91,92,94,95,96], lbs = [52,54],cbs = 2, sfs = 1)
    f3d = DefensiveFormation('3-4',dl = [90,93,96], lbs = [51,52,54,57],cbs = 2, sfs = 2)
    
    test_formation(f1o, f1d, ot, dt)
    print()
    test_formation(f2o, f2d, ot, dt)
    print()
    test_formation(f3o, f3d, ot, dt)


